from enum import Enum
from .memory_addresses import *
from . import WPContext as WPctx
from .dolphin_connection import DolphinClient, DolphinException
from ..WPUtils import *

class ConnectionState(Enum):
    DISCONNECTED = 0
    CONNECTED = 1
    MENU = 2
    BGI = 3
    GLOBE_TROT = 4
    MII_OF_A_KIND = 5
    SPIN_OFF = 6
    BINGO = 7
    MINIGAME = 8
    MINI_RESULTS = 9
    PG_RESULTS = 10


class WPInterface:
    """Interfaces directly with Wii Party, returning information about the status of the game"""

    dolphin_client: DolphinClient

    def __init__(self, logger):
        self.logger = logger
        self.dolphin_client = DolphinClient(logger)

    def get_connection_state(self) -> ConnectionState:
        try:
            if not self.dolphin_client.is_hooked():
                return ConnectionState.DISCONNECTED

            if self.is_in_menu():
                return ConnectionState.MENU

            if self.is_bgi():
                return ConnectionState.BGI

            if self.is_globe_trot():
                return ConnectionState.GLOBE_TROT

            if self.is_mii_of_a_kind():
                return ConnectionState.MII_OF_A_KIND

            if self.is_spin_off():
                return ConnectionState.SPIN_OFF

            if self.is_bingo():
                return ConnectionState.BINGO

            if self.in_minigame():
                return ConnectionState.MINIGAME

            if self.in_results() == 1:
                return ConnectionState.MINI_RESULTS

            if self.in_results() == 2:
                return ConnectionState.PG_RESULTS

            return ConnectionState.CONNECTED

        except (DolphinException, RuntimeError):
            return ConnectionState.DISCONNECTED

    def get_active_mode(self) -> str:
        """Returns the active mode, regardless whether the rel is loaded"""

        mode = self.dolphin_client.read_word(GameAddresses.game_mode)

        mode_to_string = {
            0x00: "Board Game Island",
            0x01: "Spin-Off",
            0x03: "Globe Trot",
            0x04: "Mii of a Kind",
            0x05: "Balance Boat - Double Up",
            0x06: "Balance Boat - Time Attack",
            0x07: "Friend Connection",
            0x08: "Match-Up",
            0x09: "Buddy Quiz",
            0x0b: "Time Bomb",
            0x0c: "Word Bomb",
            0x0d: "Animal Tracker",
            0x0f: "Hide 'n' Hunt",
            0x10: "Bingo",
            0x11: "Rule Reversal",
            0x12: "Free Play",
            0x14: "Battle",
            0x16: "Solo",
            0x17: "Challenge",
        }

        return mode_to_string[mode]

    def mini_player_won(self) -> bool | None:
        """Evaluates if the player has won a minigame, returns None if the results haven't been decided"""

        in_results = self.dolphin_client.read_bytes(GameAddresses.mini_in_results, 2)
        current_rel = self.dolphin_client.read_byte(GameAddresses.current_rel)
        placement = self.dolphin_client.read_byte(PlayerAddresses.minigame_placement)

        if not in_results and current_rel != 106:
            # Results not decided
            return None

        type, _ = self.get_current_minigame()

        if type == "4 Player":
            return placement == 0
        else:
            return placement == 1

    def pg_player_won(self) -> bool | None:
        """Evaluates if the player has won a party game, returns None if the results haven't been decided"""

        in_results = self.dolphin_client.read_bytes(GameAddresses.pg_in_results, 2)

        # NEED TO FIND PG PLACEMENT
        placement = self.dolphin_client.read_byte(PlayerAddresses.minigame_placement)

        if not in_results:
            # Results not decided
            return None

        return placement == 0

    def get_current_minigame(self) -> tuple[str, str]:
        """Returns the Minigame Type, Minigame Name"""

        type, name = MINIGAME_DATA[self.dolphin_client.read_word(GameAddresses.minigame_id)]

        if WPctx.YAML_GAME_VERSION == 2: # 2 = NTSC-U
            name = PAL_TO_NTSCU[name]

        return type, name

    def get_cpu_skill(self) -> tuple[int, str]:
        """Returns the CPU Skill int and string"""

        value = self.dolphin_client.read_byte(CPUAddresses.current_skill)

        return value, {0: "Beginner", 1: "Standard", 2: "Advanced", 3: "Expert", 4: "Master"}[value]


    def in_minigame(self) -> bool:
        """Checks if the current rel loaded is a minigame"""

        current_map = self.dolphin_client.read_byte(GameAddresses.current_rel)
        string = REL_TO_NAME.get(current_map)
        non_minigames = ["boot", "loading", "inst", "menu", "Board Game Island", "Spin-Off", "Globe Trot",
        "Mii of a Kind", "Balance Boat", "Balance Boat Time Attack", "Friend Connection", "Match-Up", "Buddy Quiz",
        "Time Bomb", "Word Bomb", "Animal Tracker", "Quick Draw", "Hide 'n' Hunt", "Bingo", "Rule Reversal", "Battle",
        "Solo", "openmess", "ranking"]

        return string not in non_minigames


    def is_in_menu(self) -> bool:
        """Checks the current rel loaded to see if we're in the menu"""

        current_map = self.dolphin_client.read_byte(GameAddresses.current_rel)
        string = REL_TO_NAME.get(current_map)

        return string == "menu"

    def is_bgi(self) -> bool:
        """Checks the current rel loaded to see if BGI is loaded"""

        current_map = self.dolphin_client.read_byte(GameAddresses.current_rel)
        string = REL_TO_NAME.get(current_map)

        return string == "Board Game Island"

    def is_globe_trot(self) -> bool:
        """Checks the current rel loaded to see if Globe Trot is loaded"""

        current_map = self.dolphin_client.read_byte(GameAddresses.current_rel)
        string = REL_TO_NAME.get(current_map)

        return string == "Globe Trot"

    def is_mii_of_a_kind(self) -> bool:
        """Checks the current rel loaded to see if Mii of a Kind (Swap Meet) is loaded"""

        current_map = self.dolphin_client.read_byte(GameAddresses.current_rel)
        string = REL_TO_NAME.get(current_map)

        return string == "Mii of a Kind"

    def is_spin_off(self) -> bool:
        """Checks the current rel loaded to see if Spin-Off is loaded"""

        current_map = self.dolphin_client.read_byte(GameAddresses.current_rel)
        string = REL_TO_NAME.get(current_map)

        return string == "Spin-Off"

    def is_bingo(self) -> bool:
        """Checks the current rel loaded to see if Bingo is loaded"""

        current_map = self.dolphin_client.read_byte(GameAddresses.current_rel)
        string = REL_TO_NAME.get(current_map)

        return string == "Bingo"

    def is_loading(self) -> bool:
        """Checks the current rel loaded to see if we're in some sort of loading screen"""

        current_map = self.dolphin_client.read_byte(GameAddresses.current_rel)
        string = REL_TO_NAME.get(current_map)

        return string in ["loading", "boot"]

    def is_instructions(self) -> bool:
        """Checks the current rel loaded to see if we're in the instructions (WITHOUT RESULTS)"""

        current_map = self.dolphin_client.read_byte(GameAddresses.current_rel)
        string = REL_TO_NAME.get(current_map)
        mini_in_results = self.dolphin_client.read_bytes(GameAddresses.mini_in_results, 2)
        pg_in_results = self.dolphin_client.read_bytes(GameAddresses.pg_in_results, 2)

        mini_flag = int.from_bytes(mini_in_results, byteorder="big")
        pg_flag = int.from_bytes(pg_in_results, byteorder="big")

        return string == "inst" and not mini_flag and not pg_flag

    def in_results(self) -> int:
        """Checks if we're in the results screen for either Party Games or Minigames
        Returns 1 if we're in the minigame results, 2 if we're in the party game results, 0 if none"""

        mini_in_results = self.dolphin_client.read_bytes(GameAddresses.mini_in_results, 2)
        pg_in_results = self.dolphin_client.read_bytes(GameAddresses.pg_in_results, 2)
        current_map = self.dolphin_client.read_byte(GameAddresses.current_rel)
        rel = REL_TO_NAME.get(current_map)

        mini_flag = int.from_bytes(mini_in_results, byteorder="big")
        pg_flag = int.from_bytes(pg_in_results, byteorder="big")

        party_games = ["Board Game Island", "Globe Trot", "Mii of a Kind", "Spin-Off", "Bingo"]

        if mini_flag and rel == "inst":
            # Minigame Results
            return 1
        elif pg_flag and self.get_active_mode() in party_games and rel == self.get_active_mode():
            # Party Game Result
            return 2
        else:
            # None
            return 0
