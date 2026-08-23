from enum import Enum
from .memory_addresses import *
from . import WPContext as WPctx
from .dolphin_connection import DolphinClient, DolphinException

rel_to_name = {
    1: "boot",
    106: "inst",
    2: "loading",
    3: "menu",
    22: "Commuter Count",
    23: "Timber Topple",
    24: "Delivery Duel",
    26: "Roll to the Goal",
    27: "Channel Changers",
    28: "Spring Time",
    29: "Shepherd Scramble",
    30: "Poppin' Pilots",
    74: "Pop-Up Bandits",
    31: "Fruit Focus",
    32: "Flycycle Team",
    33: "Fishin' Buddies",
    34: "Bumper Crops",
    35: "Robot Factory",
    36: "Torchlit Terror",
    37: "Basket Bonanza",
    38: "Meet and Greet",
    39: "Paddle Pals",
    40: "Pop Coaster",
    41: "Tippy Traverse",
    42: "Pump Cart Panic",
    43: "Sheep Crossing",
    44: "Banana Blockade",
    45: "Spring Ringers",
    47: "Rodent Rundown",
    48: "Skipping Squad",
    49: "Bobsleigh Highway",
    50: "Colour Coordination",
    51: "Teamwork Temple",
    52: "Blastronauts",
    53: "Flying Fruit",
    54: "Lumber Whacks",
    55: "Splash Bash",
    56: "Poserobics",
    57: "Hide and Peek",
    58: "Derby Dash",
    59: "Smile Snap",
    60: "Chop Chops",
    61: "Walk-Off",
    62: "Shifty Gifts",
    63: "Hurdle Hover",
    64: "Jumbo Jump",
    65: "Lunar Landers",
    66: "Popgun Posse", # If 2 players, "Can Poppers"
    67: "Friendly Face-Off",
    68: "Flag Fracas", # If 2 players, "Flag Footrace"
    69: "Shutterpup",
    70: "Lucky Launch",
    71: "Saucer Snap",
    72: "Maze Daze",
    73: "Quicker Chipper",
    25: "Barrel Daredevil",
    75: "Face Flip",
    76: "Goal Getters",
    77: "Stop Watchers",
    78: "Chopper Hoppers",
    79: "Puzzle Pick-Up",
    80: "Feathered Frenzy",
    81: "Follow Your Face",
    82: "Strategy Steps",
    83: "Tropical Punch",
    84: "Zombie Tag",
    85: "Pearl Plunder",
    86: "Hammer Heads",
    87: "Ball Brawl",
    88: "Lofty Leap",
    89: "Space Brawl",
    90: "Dicey Descent",
    91: "Space Race",
    92: "Cry Babies",
    93: "Ram Jam",
    94: "Spotlight Fight",
    95: "Chin-Up Champ",
    96: "Risky Railway",
    97: "Balloon Buggies",
    98: "Back Attack",
    99: "Marching Orders",
    100: "Garden Gridlock",
    101: "Shifty Gifts",
    102: "Banana Blockade",
    46: "Hidden Charms",
    103: "About Face",
    4: "Board Game Island",
    5: "Spin-Off",
    6: "Globe Trot",
    7: "Mii of a Kind",
    8: "Balance Boat",
    9: "Balance Boat Time Attack",
    10: "Friend Connection",
    11: "Match-Up",
    12: "Buddy Quiz",
    13: "Time Bomb",
    14: "Word Bomb",
    15: "Animal Tracker",
    16: "Quick Draw",
    17: "Hide 'n' Hunt",
    18: "Bingo",
    19: "Rule Reversal",
    20: "Battle",
    21: "Solo",
    104: "openmess",
    105: "ranking",
}
"""A dictionary converting the rel ID to the rel name"""

minigame_data = {
    # 1 vs 1
    0x64: ("1 vs 1", "Commuter Count"),
    0x65: ("1 vs 1", "Timber Topple"),
    0x66: ("1 vs 1", "Delivery Duel"),
    0x68: ("1 vs 1", "Roll to the Goal"),
    0x6a: ("1 vs 1", "Channel Changers"),
    0x6b: ("1 vs 1", "Spring Time"),
    0x6c: ("1 vs 1", "Shepherd Scramble"),
    0x6d: ("1 vs 1", "Poppin' Pilots"),
    0x6e: ("1 vs 1", "Flag Footrace"),
    0x6f: ("1 vs 1", "Pop-Up Bandits"),
    0x70: ("1 vs 1", "Fruit Focus"),

    # Pair
    0xc8: ("Pair", "Flycycle Team"),
    0xc9: ("Pair", "Fishin' Buddies"),
    0xca: ("Pair", "Bumper Crops"),
    0xcb: ("Pair", "Robot Factory"),
    0xcc: ("Pair", "Torchlit Terror"),
    0xcd: ("Pair", "Basket Bonanza"),
    0xce: ("Pair", "Meet and Greet"),
    0xd0: ("Pair", "Paddle Pals"),
    0xd1: ("Pair", "Pop Coaster"),
    0xd2: ("Pair", "Tippy Traverse"),
    0xd3: ("Pair", "Pump Cart Panic"),
    0xd4: ("Pair", "Sheep Crossing"),
    0xd5: ("Pair", "Banana Blockade"),
    0xd6: ("Pair", "Spring Ringers"),
    0xd7: ("Pair", "Can Poppers"),
    0xd8: ("Pair", "Hidden Charms"),
    0xda: ("Pair", "Rodent Rundown"),
    0xdb: ("Pair", "Skipping Squad"),
    0xdd: ("Pair", "Bobsleigh Highway"),
    0xde: ("Pair", "Colour Coordination"),
    0xdf: ("Pair", "Teamwork Temple"),
    0xe0: ("Pair", "Blastronauts"),

    # 1 vs 3
    0x12c: ("1 vs 3", "Flying Fruit"),
    0x12d: ("1 vs 3", "Lumber Whacks"),
    0x12e: ("1 vs 3", "Splash Bash"),
    0x12f: ("1 vs 3", "Poserobics"),
    0x130: ("1 vs 3", "Hide-and-Peek"),

    # 4 Player
    0x190: ("4 Player", "Derby Dash"),
    0x191: ("4 Player", "Smiley Snap"),
    0x192: ("4 Player", "Chop Chops"),
    0x193: ("4 Player", "Walk-Off"),
    0x194: ("4 Player", "Shifty Gifts"),
    0x195: ("4 Player", "Hurdle Hover"),
    0x196: ("4 Player", "Jumbo Jump"),
    0x197: ("4 Player", "Lunar Landers"),
    0x198: ("4 Player", "Popgun Posse"),
    0x19a: ("4 Player", "Friendly Face-Off"),
    0x19b: ("4 Player", "Flag Fracas"),
    0x19c: ("4 Player", "Shutterpup"),
    0x19d: ("4 Player", "Lucky Launch"),
    0x19e: ("4 Player", "Saucer Snap"),
    0x19f: ("4 Player", "Maze Daze"),
    0x1a0: ("4 Player", "Quicker Chipper"),
    0x1a2: ("4 Player", "Barrel Daredevil"),
    0x1a3: ("4 Player", "Face Flip"),
    0x1a4: ("4 Player", "Goal Getters"),
    0x1a5: ("4 Player", "Stop Watchers"),
    0x1a6: ("4 Player", "Chopper Hoppers"),
    0x1a7: ("4 Player", "Puzzle Pick-Up"),
    0x1a8: ("4 Player", "Feathered Frenzy"),
    0x1aa: ("4 Player", "Follow Your Face"),
    0x1ab: ("4 Player", "Strategy Steps"),
    0x1ac: ("4 Player", "Tropical Punch"),
    0x1ae: ("4 Player", "Zombie Tag"),
    0x1af: ("4 Player", "Pearl Plunder"),
    0x1b0: ("4 Player", "Hammer Heads"),
    0x1b1: ("4 Player", "Ball Brawl"),
    0x1b2: ("4 Player", "Lofty Leap"),
    0x1b4: ("4 Player", "Space Brawl"),
    0x1b5: ("4 Player", "Dicey Descent"),
    0x1b6: ("4 Player", "Space Race"),
    0x1b7: ("4 Player", "Cry Babies"),
    0x1b8: ("4 Player", "Ram Jam"),
    0x1b9: ("4 Player", "Spotlight Fight"),
    0x1ba: ("4 Player", "Chin-Up Champ"),
    0x1bb: ("4 Player", "Risky Railway"),
    0x1bd: ("4 Player", "Balloon Buggies"),
    0x1be: ("4 Player", "Back Attack"),

    # Challenge
    0x1f5: ("Challenge", "Marching Orders"),
    0x1f6: ("Challenge", "Garden Gridlock"),
    0x1f7: ("Challenge", "Shifty Gifts"),
    0x1f8: ("Challenge", "Tippy Traverse"),
    0x1f9: ("Challenge", "Banana Blockade"),
    0x1fa: ("Challenge", "Clover Hunter"),
    0x1fb: ("Challenge", "About Face (Solo)"),
    0x1fc: ("Challenge", "About Face (4 Player)"),
    0x1fd: ("Challenge", "About Face (1 vs 1)"),
}
"""A dictionary of the minigame type and name from the minigame ID"""

PAL_TO_NTSCU = {
    "Lunar Landers": "Moon Landing",
    "Hurdle Hover": "Flap Hurdles",
    "Ball Brawl": "Crash Balls",
    "Space Race": "Cosmic Capers",
    "Lofty Leap": "Rope Sling",
    "Risky Railway": "Risky Railroad",
    "Shepherd Scramble": "Jangle Wranglers",
    "Torchlit Terror": "Flashlight Frights",
    "Hidden Charms": "Clover Hunt",
    "Skipping Squad": "Jump Rope Jam",
    "Bobsleigh Highway": "Bobsled Highway",
    "Colour Coordination": "Color Coordination",
}
"""Converts PAL names to the NTSC-U equivalent"""

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

        type, name = minigame_data[self.dolphin_client.read_word(GameAddresses.minigame_id)]

        if WPctx.YAML_GAME_VERSION == 2: # 2 = NTSC-U
            name = PAL_TO_NTSCU[name]

        return type, name

    def get_cpu_skill(self) -> tuple[int, str]:
        """Returns the CPU Skill int and string"""

        value = self.dolphin_client.read_byte(CPUAddresses.skill)

        return value, {0: "Beginner", 1: "Standard", 2: "Advanced", 3: "Expert", 4: "Master"}[value]


    def in_minigame(self) -> bool:
        """Checks if the current rel loaded is a minigame"""

        current_map = self.dolphin_client.read_byte(GameAddresses.current_rel)
        string = rel_to_name.get(current_map)
        non_minigames = ["boot", "loading", "inst", "menu", "Board Game Island", "Spin-Off", "Globe Trot",
        "Mii of a Kind", "Balance Boat", "Balance Boat Time Attack", "Friend Connection", "Match-Up", "Buddy Quiz",
        "Time Bomb", "Word Bomb", "Animal Tracker", "Quick Draw", "Hide 'n' Hunt", "Bingo", "Rule Reversal", "Battle",
        "Solo", "openmess", "ranking"]

        return string not in non_minigames


    def is_in_menu(self) -> bool:
        """Checks the current rel loaded to see if we're in the menu"""

        current_map = self.dolphin_client.read_byte(GameAddresses.current_rel)
        string = rel_to_name.get(current_map)

        return string == "menu"

    def is_bgi(self) -> bool:
        """Checks the current rel loaded to see if BGI is loaded"""

        current_map = self.dolphin_client.read_byte(GameAddresses.current_rel)
        string = rel_to_name.get(current_map)

        return string == "Board Game Island"

    def is_globe_trot(self) -> bool:
        """Checks the current rel loaded to see if Globe Trot is loaded"""

        current_map = self.dolphin_client.read_byte(GameAddresses.current_rel)
        string = rel_to_name.get(current_map)

        return string == "Globe Trot"

    def is_mii_of_a_kind(self) -> bool:
        """Checks the current rel loaded to see if Mii of a Kind (Swap Meet) is loaded"""

        current_map = self.dolphin_client.read_byte(GameAddresses.current_rel)
        string = rel_to_name.get(current_map)

        return string == "Mii of a Kind"

    def is_spin_off(self) -> bool:
        """Checks the current rel loaded to see if Spin-Off is loaded"""

        current_map = self.dolphin_client.read_byte(GameAddresses.current_rel)
        string = rel_to_name.get(current_map)

        return string == "Spin-Off"

    def is_bingo(self) -> bool:
        """Checks the current rel loaded to see if Bingo is loaded"""

        current_map = self.dolphin_client.read_byte(GameAddresses.current_rel)
        string = rel_to_name.get(current_map)

        return string == "Bingo"

    def is_loading(self) -> bool:
        """Checks the current rel loaded to see if we're in some sort of loading screen"""

        current_map = self.dolphin_client.read_byte(GameAddresses.current_rel)
        string = rel_to_name.get(current_map)

        return string in ["loading", "boot"]

    def is_instructions(self) -> bool:
        """Checks the current rel loaded to see if we're in the instructions (WITHOUT RESULTS)"""

        current_map = self.dolphin_client.read_byte(GameAddresses.current_rel)
        string = rel_to_name.get(current_map)
        mini_in_results = self.dolphin_client.read_bytes(GameAddresses.mini_in_results, 2)
        pg_in_results = self.dolphin_client.read_bytes(GameAddresses.pg_in_results, 2)

        return string == "inst" and not mini_in_results and not pg_in_results

    def in_results(self) -> int:
        """Checks if we're in the results screen for either Party Games or Minigames
        Returns 1 if we're in the minigame results, 2 if we're in the party game results, 0 if none"""

        mini_in_results = self.dolphin_client.read_bytes(GameAddresses.mini_in_results, 2)
        pg_in_results = self.dolphin_client.read_bytes(GameAddresses.pg_in_results, 2)
        current_map = self.dolphin_client.read_byte(GameAddresses.current_rel)
        rel = rel_to_name.get(current_map)

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
