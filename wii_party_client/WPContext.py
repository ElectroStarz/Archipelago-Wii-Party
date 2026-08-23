import asyncio
import logging
import random
import traceback
from collections import deque
from typing import Dict, Set, Optional, Any
import subprocess

import Utils
from MultiServer import mark_raw
from NetUtils import ClientStatus, JSONMessagePart
from settings import get_settings
from .WPInterface import WPInterface, ConnectionState
from . import dolphin_connection as dc
from ..items import item_table
from ..locations import LOCATION_NAME_TO_ID
from .memory_addresses import *

tracker_loaded = False
try:

    from worlds.tracker.TrackerClient import TrackerGameContext as SuperContext, \
                                            TrackerCommandProcessor as SuperCommandProcessor
    tracker_loaded = True
except ModuleNotFoundError:
    from CommonClient import CommonContext as SuperContext, ClientCommandProcessor as SuperCommandProcessor


YAML_GAME_VERSION = None


id_to_name = {data.code: name for name, data in item_table.items()}
CLIENT_VERSION = "0.0.1"
COMPATIBLE_VERSIONS = []
CONSUMABLE_STORAGE_CATEGORY = "wii_party"
logger = logging.getLogger("Client")


status_messages = {
    ConnectionState.DISCONNECTED: "Unable to connect to the Dolphin instance, attempting to reconnect...",
    ConnectionState.CONNECTED: "Connected to Dolphin!",
    ConnectionState.BGI: "In Board Game Island",
    ConnectionState.GLOBE_TROT: "In Globe Trot",
    ConnectionState.MII_OF_A_KIND: "In Mii of a Kind/Swap Mii",
    ConnectionState.SPIN_OFF: "In Spin-Off",
    ConnectionState.BINGO: "In Bingo",
    ConnectionState.MINIGAME: "In a Minigame",
    ConnectionState.MINI_RESULTS: "In Minigame Results Screen",
    ConnectionState.PG_RESULTS: "In Party Game Results Screen"
}

class WPCommandProcessor(SuperCommandProcessor):
    ctx: "WPContext"

    def __init__(self, ctx: "WPContext"):
        super().__init__(ctx)

    def _cmd_status(self):
        """Display the current Dolphin connection status."""
        logger.info(f"Connection Status: {status_messages[self.ctx.connection_state]}")

    def _cmd_debug_mode(self):
        """Toggle client debugging on and off (Default off)"""
        if not self.ctx.DEBUGGING:
            self.ctx.DEBUGGING = True
            logger.info("Debugging on")
            self.ctx.debug_log(
                f"\n=========================================\n"
                f"Welcome to debug mode! This is what a debug message will look like!\n"
                f"Debug mode will tell you about things such as: Is the game ready_to_handle?\n"
                f"Has my item been stopped from swapping? What's the current forced_item_id?\n"
                f"You can use /change_debug_amount to change the amount of debug messages stored "
                f"at once so the client doesn't spam messages!"
                f"\n=========================================\n"
            )
        else:
            self.ctx.DEBUGGING = False
            logger.info("Debugging off")

    def _cmd_change_debug_amount(self, amount: str):
        """Change the amount of debug messages that are stored so they don't repeat

        :param amount: The amount of debug messages to store
        """
        try:
            new_amount = int(amount)
            from collections import deque
            self.ctx.last_debug_messages = deque(self.ctx.last_debug_messages, maxlen=new_amount)
            logger.info(f"Changed debug amount to {new_amount}")
        except ValueError:
            logger.info(f"Error: '{amount}' is not a valid number! Please enter an integer.")

    def _cmd_read_address(self, address: str, addr_type: str, pointers: str | None):
        """Read the value of any address - Used for diagnostic purposes.
        :param address: Should look like 0x80000000 (8 digits after 0x),
        :param addr_type: Any from Byte, Halfword, Word, Float or String.
        :param pointers: Optional and should look like 0x1F4, 0x8,"""

        try:
            numeric_address = int(address, 16)
        except ValueError:
            return f"Error: '{address}' is not a valid hexadecimal address."

        if pointers:
            new_pointers = []
            for p in pointers:
                # Strip out any brackets or commas
                clean_p = p.replace("[", "").replace("]", "").replace(",", "")

                # Skip any empty strings caused by extra spaces
                if not clean_p:
                    continue

                try:
                    new_pointers.append(int(clean_p, 16))
                except ValueError:
                    return f"Error: Pointer '{p}' is not valid hex."
            final_address = self.ctx.game_interface.dolphin_client.follow_pointers(numeric_address,
                                                                                   new_pointers)
        else:
            final_address = numeric_address

        client = self.ctx.game_interface.dolphin_client
        result = ""

        match addr_type.lower():
            case "byte":
                result = client.read_byte(final_address)
            case "halfword":
                result = client.read_bytes(final_address, 2)
            case "word":
                result = client.read_word(final_address)
            case "float":
                result = client.read_float(final_address)
            case "string":
                result = client.read_string(final_address)
            case _:
                error_msg = f"Error: Unsupported address type '{addr_type}'"
                logger.error(error_msg)
                return error_msg

        # Format final_address with hex() makes it easier to read back.
        logger.info(f"[Memory Read] {addr_type} at {hex(final_address)}. Result: {result}")
        return result

class RegionMismatchError(Exception):
    pass

# noinspection PyDeprecation
# noinspection PyAttributeOutsideInit
class WPContext(SuperContext):
    tags = {"AP"}
    game = "Wii Party"
    command_processor = WPCommandProcessor
    items_handling = 0b111
    want_slot_data = True

    game_interface: WPInterface
    connection_state = ConnectionState.DISCONNECTED
    slot_data: dict[str, Any] = {}
    last_error_message: Optional[str] = None
    auto_open: bool = get_settings()["wp_settings"]["auto_open"]

    def __init__(self, server_address: str, password: str):
        super().__init__(server_address, password)
        self.game_interface = WPInterface(logger)
        self.items_received = []
        self.items_handled = set()
        self.seed: Optional[str] = None

        # Lists for items
        self.party_games = []
        self.minigames = []

        self.filler_to_give = deque()
        self.traps_to_give = deque()


        self.queued_consumable_indices: Set[int] = set()
        self.handled_consumable_indices: Set[int] = set()
        # Set when a Get/SetReply for handled consumables has been applied this session.
        self._consumables_load_event = asyncio.Event()

        # Debug Stuff
        self.DEBUGGING: bool = False
        self.last_debug_messages = deque(maxlen=5)  # Stores up to 5 messages at a time at default
        self._toggle_log_states = {}
        self._log_once_states = {}
        self._rate_log_states = {}

    # --- Consumable persistence (filler + traps) ---
    # These are one-shot items tracked by AP received-item index and saved to server storage
    # so reconnects don't hand them out again. Key is scoped per slot.

    @property
    def consumable_storage_key(self) -> Optional[str]:
        if self.seed is None or self.slot is None:
            return None
        return f"{CONSUMABLE_STORAGE_CATEGORY}_{self.slot}"

    def _on_consumables_storage_update(self, value: Any) -> None:
        """Apply server storage for handled filler/trap indices and drop any stale queue entries."""
        if value is None:
            self.handled_consumable_indices = set()
        elif isinstance(value, list):
            self.handled_consumable_indices = {int(index) for index in value}
        else:
            logger.warning(f"Unexpected handled consumables value type: {type(value)}")
            return

        handled = self.handled_consumable_indices
        self.filler_to_give = deque(
            entry for entry in self.filler_to_give
            if not (isinstance(entry, tuple) and entry[0] in handled)
        )
        self.traps_to_give = deque(
            entry for entry in self.traps_to_give
            if not (isinstance(entry, tuple) and entry[0] in handled)
        )
        self.queued_consumable_indices -= handled
        self._consumables_load_event.set()
        self.debug_log(f"Loaded {len(self.handled_consumable_indices)} handled consumables")

    async def load_handled_consumables(self, initialise: bool = False) -> None:
        """Load handled filler/trap indices from AP storage before queuing ReceivedItems."""
        key = self.consumable_storage_key
        if key is None or self._consumables_load_event.is_set():
            return

        self._consumables_load_event.clear()
        if initialise:
            # First connect for this seed/slot: create the key if missing, then subscribe to updates.
            await self.send_msgs([{
                "cmd": "Set",
                "key": key,
                "default": [],
                "want_reply": False,
                "operations": [{"operation": "default", "value": 0}],
            }])
            self.set_notify(key)
        else:
            await self.send_msgs([{"cmd": "Get", "keys": [key]}])

        try:
            await asyncio.wait_for(self._consumables_load_event.wait(), timeout=10.0)
        except asyncio.TimeoutError:
            logger.warning("Timed out loading handled consumables from server storage")
            self._consumables_load_event.set()

    async def mark_consumable_handled(self, item_index: Optional[int]) -> None:
        if item_index is None:
            return

        self.queued_consumable_indices.discard(item_index)
        self.handled_consumable_indices.add(item_index)
        # Save after the effect is applied so a disconnect mid-queue doesn't eat the item.
        await self.save_handled_consumables()
        self.debug_log(f"Saved handled consumable index {item_index}")

    async def save_handled_consumables(self) -> None:
        key = self.consumable_storage_key
        if key is None:
            return
        await self.send_msgs([{
            "cmd": "Set",
            "key": key,
            "default": [],
            "want_reply": True,
            "operations": [{
                "operation": "replace",
                "value": sorted(self.handled_consumable_indices)
            }]
        }])
        self.debug_log(f"Saving handled consumables: {sorted(self.handled_consumable_indices)}")

    async def _handle_received_items_consumables(self, args: dict) -> None:
        # Wait for storage before queuing — otherwise reconnects re-fire already-handled items.
        await self.load_handled_consumables()

        start_index = args["index"]
        if start_index == 0:
            # CommonContext replaced items_received with a full inventory snapshot.
            # Keep that list and rebuild only unlock state from it.
            self.reset_local_item_state(clear_received=False)

        self.debug_log(
            f"ReceivedItems packet start={start_index}, count={len(args['items'])}, "
            f"handled_consumables={len(self.handled_consumable_indices)}"
        )

        for offset, item in enumerate(args["items"]):
            item_index = start_index + offset

            if item_index in self.handled_consumable_indices or item_index in self.queued_consumable_indices:
                self.debug_log(f"Skipping already queued/handled consumable index {item_index}")
                continue

            item_id = item.item if hasattr(item, "item") else item[0]
            item_name = id_to_name.get(item_id)

            if not item_name:
                self.debug_log(f"Skipping unknown item id {item_id} at index {item_index}")
                continue

            if item_name.startswith("1") or "Charge" in item_name:
                self.filler_to_give.append((item_index, item_name))
                self.queued_consumable_indices.add(item_index)
                logger.info(f"Queued filler: {item_name}")
                self.debug_log(f"Filler queue size is now {len(self.filler_to_give)}")

            elif "Trap" in item_name:
                self.traps_to_give.append((item_index, item_name))
                self.queued_consumable_indices.add(item_index)
                logger.info(f"Queued trap: {item_name}")
                self.debug_log(f"Trap queue size is now {len(self.traps_to_give)}")

        await self.handle_received_items()

    def reset_game_session_state(self, game_active: bool = False) -> None:
        """Reset runtime-only state when the game process/title exits or restarts."""
        pass

    def reset_local_item_state(self, clear_received: bool = False, clear_consumed: bool = False) -> None:
        if clear_received:
            self.items_received.clear()
        pass

        if clear_consumed:
            self.filler_to_give.clear()
            self.traps_to_give.clear()
            self.queued_consumable_indices.clear()
            self.handled_consumable_indices.clear()
            self._consumables_load_event.clear()

    def reset_location_state(self) -> None:
        self.locations_checked.clear()
        self.checked_locations.clear()

    def on_package(self, cmd: str, args: dict):
        super().on_package(cmd, args)
        if cmd == "Connected":
            ap_locations_checked = args["checked_locations"]
            self.locations_checked.update(ap_locations_checked)

            self.slot_data = args.get("slot_data", {})

            global YAML_GAME_VERSION
            YAML_GAME_VERSION = self.slot_data.get("game_region", None)

            # Slot is known now - load/create the per-slot consumable save before items arrive.
            asyncio.create_task(self.load_handled_consumables(initialise=True))
            if self.locations_checked:
                asyncio.create_task(
                    self.send_msgs([{"cmd": "LocationChecks", "locations": sorted(self.locations_checked)}])
                )

            generation_version = self.slot_data.get("version", "0.0.1")

            # Client World mismatch handler
            if generation_version in COMPATIBLE_VERSIONS:
                logger.info(
                    f"This seed was generated on {generation_version}, however client version {CLIENT_VERSION} is compatible!"
                )
            elif CLIENT_VERSION != generation_version:
                logger.error(
                    f"\n=========================================\n"
                    f"VERSION MISMATCH DETECTED!\n"
                    f"Seed was generated on version: {generation_version}\n"
                    f"Your Client version: {CLIENT_VERSION}. This version is not compatible with version generated on!\n"
                    f"Please update, downgrade your client, or regenerate the seed as things may break!\n"
                    f"========================================="
                )
            else:
                logger.info(f"Version check passed! (v{CLIENT_VERSION})")

        elif cmd == "RoomInfo":
            new_seed = args.get("seed_name", "unknown")
            if self.seed != new_seed:
                # New seed - don't carry consumable or location state from the previous room.
                pass

            self.seed = new_seed

        elif cmd == "ReceivedItems":
            asyncio.create_task(self._handle_received_items_consumables(args))


        elif cmd in ("Retrieved", "SetReply"):
            key = self.consumable_storage_key
            if key:
                if cmd == "Retrieved" and key in args.get("keys", {}):
                    self._on_consumables_storage_update(args["keys"][key])
                elif cmd == "SetReply" and args.get("key") == key:
                    self._on_consumables_storage_update(args.get("value"))

    def update_connection_status(self):
        self.connection_state = self.game_interface.get_connection_state()

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(WPContext, self).server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    async def disconnect(self, allow_autoreconnect: bool = False):
        self.game_interface.dolphin_client.disconnect()
        await super().disconnect(allow_autoreconnect)

    def make_gui(self):
        ui = super().make_gui()
        ui.base_title = f"Archipelago Wii Party Client (Version {CLIENT_VERSION}) | AP Version"
        return ui

    # --- Log types ---

    def debug_log(self, message: str) -> None:
        """Sends messages to the client if debugging is on"""

        if self.DEBUGGING:
            if message not in self.last_debug_messages:
                self.last_debug_messages.append(message)
                logger.info(f"[Wii Party Debug] {message}")

    def toggle_log(self, key: str, message_true: str, message_false: str, condition: bool, debug_mode: bool):
        """2 messages, one for true, one for false. Checks the key and if the condition has changed, sends the message"""

        if not hasattr(self, "_toggle_log_states"):
            self._toggle_log_states = {}

        previous = self._toggle_log_states.get(key)

        if previous is None or previous != condition:
            if debug_mode:
                self.debug_log(message_true if condition else message_false)
            else:
                logger.info(message_true if condition else message_false)
            self._toggle_log_states[key] = condition

    def log_once(self, key: str, message: str, debug_mode: bool):
        """Logs a message only if it differs from the last one logged for this key."""
        if not hasattr(self, "_log_once_states"):
            self._log_once_states = {}

        if self._log_once_states.get(key) != message:
            if debug_mode:
                self.debug_log(message)
            else:
                logger.info(message)
            self._log_once_states[key] = message

    def rate_log(self, key: str, message: str, interval: float, debug_mode: bool):
        """Logs a message at most once per interval (in seconds) for a given key."""
        if not hasattr(self, "_rate_log_states"):
            self._rate_log_states = {}

        now = asyncio.get_event_loop().time()
        last_logged = self._rate_log_states.get(key, 0.0)

        if now - last_logged >= interval:
            if debug_mode:
                self.debug_log(message)
            else:
                logger.info(message)
            self._rate_log_states[key] = now

    def log_colour(self, text: str, colour: str):
        if self.ui is not None:
            message: JSONMessagePart = {"type": "color", "text": text, "color": colour}
            self.ui.print_json([message])


    # === Utility Functions ===


    # === Receiving Items ===


    async def handle_received_items(self):
        party_games = ("Board Game Island", "Globe Trot", "Mii of a Kind", "Spin-Off", "Bingo")

        for network_item in self.items_received:
            item_id = network_item.item
            item_name = id_to_name.get(item_id)

            if network_item not in self.items_handled:
                if item_name is None:
                    continue

                if item_name in party_games:
                    self.party_games.append(item_name)


            self.items_handled.add(network_item)

        await self.handle_button_unlocks()


    async def handle_button_unlocks(self):
        """Handles the button unlocks for the main menu and some subscreens"""
        unlock_value = 131065 # This subtracts the Minigames, Suggestions and Rankings button from the original
                              # value 131071

        button_items = [*self.party_games] # Use * to unpack lists into 1 master list

        button_values = {
            "Suggestions":       1, # Isn't subtracted due to people possibly accessing things they shouldn't be able to
            "Rankings":          2, # ALREADY SUBTRACTED
            "Minigames":         4, # ALREADY SUBTRACTED
            "Board Game Island": 8,
            "Globe Trot":        16,
            "Mii of a Kind":     32,
            "Spin-Off":          64,
            "Bingo":             128,
            "Friend Connection": 256,
            "Balance Boat":      512,
            "Match Up":          1024,
            "House Party":       2048,
            "Free Play":         4096,
            "Battle":            8192,
            "Solo":              16384,
            "Challenge":         32768,
            "Rule Reversal":     65536,
        }

        for button in button_items:
            if button in button_values:
                unlock_value &= ~button_values[button]

        self.game_interface.dolphin_client.write_word(MenuAddresses.button_unlock, unlock_value)


    # === Misc Stuff idk where to put ===


    async def dolphin_sync_task(self) -> None:
        """Main Dolphin loop. Add Wii Party memory reads/writes here as addresses are mapped."""
        while not self.exit_event.is_set():
            try:
                if self.game_interface.dolphin_client.check_for_dolphin() == 0 and self.auto_open:
                    self.run_wii_party()
                    await asyncio.sleep(2)

                if not self.game_interface.dolphin_client.is_hooked():
                    await self.game_interface.dolphin_client.attempt_to_hook()

                if self.game_interface.dolphin_client.is_hooked():
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

                self.update_connection_status()

                if self.connection_state == ConnectionState.BGI:
                    await self.handle_in_bgi()
                elif self.connection_state == ConnectionState.GLOBE_TROT:
                    await self.handle_in_globe_trot()
                elif self.connection_state == ConnectionState.MII_OF_A_KIND:
                    await self.handle_in_mii()
                elif self.connection_state == ConnectionState.SPIN_OFF:
                    await self.handle_in_spin_off()
                elif self.connection_state == ConnectionState.BINGO:
                    await self.handle_in_bingo()
                elif self.connection_state == ConnectionState.MINIGAME:
                    await self.handle_in_minigame()
                elif self.connection_state == ConnectionState.MINI_RESULTS:
                    await self.handle_in_mini_results()
                elif self.connection_state == ConnectionState.PG_RESULTS:
                    await self.handle_in_pg_results()

                await self.handle_received_items()

                # Needs to be happening all the time
                # self.game_interface.dolphin_client.write_word(0x8042fd444, 0x800013B0)
                # self.game_interface.dolphin_client.write_word(0x8042fd440, 0x800014B0)

                await asyncio.sleep(0.1)


            except Exception as e:
                if "Dolphin" in str(e):
                    logger.error(f"Dolphin Connection Error: {e}")
                    self.update_connection_status()

                else:
                    logger.error(f"Sync Task Error:\n{traceback.format_exc()}")
                await asyncio.sleep(3)

    @staticmethod
    def run_wii_party():
        """Automatically runs Wii Party with our patches though a command"""

        dolphin_exe_path: str = get_settings()["wp_settings"]["dolphin_exe_path"]
        path_to_json: str = "NONE - PLEASE REPLACE LATER"

        subprocess.run([f"{dolphin_exe_path} --exec={path_to_json} -b --config=Dolphin.Core.EnableCheats=False "
                        f"--config=Achievements.Achievements.Enabled=False"])



    # === Location Handling ===


    async def check_location(self, location_name: str):
        """Checks if you've already got the location, if not, notifies AP about getting the location"""

        location_id = LOCATION_NAME_TO_ID.get(location_name)

        if location_id is None:
            self.debug_log(f"No AP location found: {location_name}")
            return

        if location_id in self.locations_checked:
            self.debug_log(f"Location: {location_name} in locations checked!")
            return

        await self.send_msgs([{"cmd": "LocationChecks", "locations": [location_id]}])
        self.locations_checked.add(location_id)
        self.debug_log(f"Checked location: name={location_name}, id={location_id}")

    async def handle_minigame_checks(self):
        """Handles sending minigame checks"""

        if not self.game_interface.mini_player_won():
            print("not win")
            return

        _, minigame_name = self.game_interface.get_current_minigame()

        await self.check_location(f"Win {minigame_name}")


    async def handle_win_pg_checks(self):
        """Handles sending the win Party Game checks"""

        if not self.game_interface.pg_player_won():
            return

        mode = self.game_interface.get_active_mode()

        await self.check_location(f"Win {mode}")

    # === Where to handle what ===


    async def handle_in_bgi(self):
        pass

    async def handle_in_globe_trot(self):
        pass

    async def handle_in_mii(self):
        pass

    async def handle_in_spin_off(self):
        pass

    async def handle_in_bingo(self):
        pass

    async def handle_in_minigame(self):
        pass

    async def handle_in_mini_results(self):
        await self.handle_minigame_checks()

    async def handle_in_pg_results(self):
        await self.handle_win_pg_checks()