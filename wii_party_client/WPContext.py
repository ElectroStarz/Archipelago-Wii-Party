import asyncio
import logging
import traceback
from typing import Any, Optional

from CommonClient import ClientCommandProcessor, CommonContext
from MultiServer import mark_raw
from ..items import item_table
from .WPInterface import ConnectionState, WPInterface
from .memory_addresses import *

id_to_name = {data.code: name for name, data in item_table.items()}
CLIENT_VERSION = "0.0.1"
logger = logging.getLogger("Client")

status_messages = {
    ConnectionState.DISCONNECTED: "Unable to connect to the Dolphin instance, attempting to reconnect...",
    ConnectionState.CONNECTED: "Connected to Dolphin!",
}


class WPCommandProcessor(ClientCommandProcessor):
    ctx: "WPContext"

    def __init__(self, ctx: "WPContext"):
        super().__init__(ctx)

    def _cmd_status(self):
        """Display the current Dolphin connection status."""
        logger.info(f"Connection Status: {status_messages[self.ctx.connection_state]}")

    @mark_raw
    def _cmd_read_address(self, address: str, addr_type: str):
        """Read a raw Dolphin memory address. Types: Byte, Halfword, Word, Float, String."""
        try:
            numeric_address = int(address, 16)
        except ValueError:
            logger.error(f"Error: '{address}' is not a valid hexadecimal address.")
            return

        client = self.ctx.game_interface.dolphin_client
        result = ""

        match addr_type.lower():
            case "byte":
                result = client.read_byte(numeric_address)
            case "halfword":
                result = client.read_bytes(numeric_address, 2)
            case "word":
                result = client.read_word(numeric_address)
            case "float":
                result = client.read_float(numeric_address)
            case "string":
                result = client.read_string(numeric_address)
            case _:
                logger.error(f"Error: Unsupported address type '{addr_type}'")
                return

        logger.info(f"[Memory Read] {addr_type} at {hex(numeric_address)}. Result: {result}")


class WPContext(CommonContext):
    tags = {"AP"}
    game = "Wii Party"
    command_processor = WPCommandProcessor
    items_handling = 0b111
    want_slot_data = True

    game_interface: WPInterface
    connection_state = ConnectionState.DISCONNECTED
    slot_data: dict[str, Any] = {}
    last_error_message: Optional[str] = None

    def __init__(self, server_address: str, password: str):
        super().__init__(server_address, password)
        self.game_interface = WPInterface(logger)
        self.command_processor.ctx = self
        self.items_received = []
        self.items_handled = []
        self.seed: Optional[str] = None

        # Lists for items
        # Lists for items
        self.party_games = []
        self.free_play_games = []
        self.minigames = []


    def on_package(self, cmd: str, args: dict[str, Any]):
        if cmd == "Connected":
            self.slot_data = args.get("slot_data", {})
            generation_version = self.slot_data.get("version")
            if generation_version is not None and generation_version != CLIENT_VERSION:
                logger.info(
                    f"This seed was generated with Wii Party version {generation_version}; "
                    f"this client skeleton is version {CLIENT_VERSION}."
                )

        super().on_package(cmd, args)

    def update_connection_status(self):
        new_state = self.game_interface.get_connection_state()
        if new_state != self.connection_state:
            self.connection_state = new_state

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(WPContext, self).server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    async def disconnect(self, allow_autoreconnect: bool = False):
        self.game_interface.dolphin_client.disconnect()
        await super().disconnect(allow_autoreconnect)


    async def handle_received_items(self):
        party_games = ("Board Game Island", "Globe Trot", "Mii Of A Kind", "Spin-Off", "Bingo")

        for network_item in self.items_received:
            item_id = network_item.item
            item_name = id_to_name.get(item_id)
            if network_item not in self.items_handled:
                if item_name is None:
                    continue

                if item_name in party_games:
                    self.party_games.append(item_name)

    async def handle_button_unlocks(self):
        """Handles the button unlocks for the main menu and some subscreens"""
        unlock_value = 131064 # This subtracts the Minigames, Rankings and Suggestions Button from the original value 131071

        button_items = [*self.party_games] # Use * to unpack lists into 1 master list

        button_values = {
            "Board Game Island": 8,
            "Globe Trot": 16,
            "Mii Of A Kind": 32,
            "Spin-Off": 64,
            "Bingo": 128,
            "Friend Connection": 256,
            "Balance Boat": 512,
            "Match Up": 1024,
            "House Party": 2048,
            "Free Play": 4096,
            "Battle": 8192,
            "Solo": 16384,
            "Challenge": 32768,
            "Rule Reversal": 65536,
        }

        for button in button_items:
            if button in button_values:
                unlock_value &= ~button_values[button]

        self.game_interface.dolphin_client.write_word(MenuAddresses.button_unlock, unlock_value)




    async def dolphin_sync_task(self) -> None:
        """Main Dolphin loop. Add Wii Party memory reads/writes here as addresses are mapped."""
        while not self.exit_event.is_set():
            try:
                if not self.game_interface.dolphin_client.is_hooked_class():
                    await self.game_interface.dolphin_client.attempt_to_hook()

                if self.game_interface.dolphin_client.is_hooked_class():
                    self.update_connection_status()

                if not self.server or not self.server.socket or self.server.socket.closed:
                    message = "Waiting for player to connect to Archipelago server..."
                    if self.last_error_message != message:
                        logger.info(message)
                        self.last_error_message = message
                    await asyncio.sleep(1)
                    continue

                if not self.slot:
                    await asyncio.sleep(1)
                    continue

                self.last_error_message = None

                await self.handle_received_items()
                await self.handle_button_unlocks()

                # TODO: Route Wii Party-specific item and location handling here
                await asyncio.sleep(1)

            except Exception:
                logger.error(f"Sync Task Error:\n{traceback.format_exc()}")
                await asyncio.sleep(3)
