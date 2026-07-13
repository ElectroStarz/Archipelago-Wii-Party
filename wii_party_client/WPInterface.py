from enum import Enum
from .memory_addresses import *
from .dolphin_connection import DolphinClient, DolphinException

map_matches = {
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


class WPInterface:
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

            return ConnectionState.CONNECTED

        except (DolphinException, RuntimeError):
            return ConnectionState.DISCONNECTED

    def has_player_won(self):
        map_val = self.dolphin_client.read_byte(GameAddresses.current_map)
        placement = self.dolphin_client.read_byte(PlayerAddresses.placement)


        # # 4 player minigames use 0 has the player winning
        # if map_val in four_player_minigames:
        #     if placement == 0:
        #         return True
        #     else:
        #         return False
        #
        # # Any other minigame type uses 1 as the player winning
        # elif map_val in other_ids:
        #     if placement == 1:
        #         return True
        #     else:
        #         return False
        # else:
        #     return False

    def get_cpu_skill(self):
        """Returns the CPU Skill"""
        value = self.dolphin_client.read_byte(CPUAddresses.skill)

        return {0: "Beginner", 1: "Standard", 2: "Advanced", 3: "Expert", 4: "Master"}[value]

    def get_minigame(self):
        current_map = self.dolphin_client.read_byte(GameAddresses.current_map)
        return map_matches.get(current_map)

    def in_minigame(self):
        current_map = self.dolphin_client.read_byte(GameAddresses.current_map)
        string = map_matches.get(current_map)
        non_minigames = ["boot", "inst", "loading", "menu","Board Game Island", "Spin-Off", "Globe Trot",
        "Mii of a Kind", "Balance Boat", "Balance Boat Time Attack", "Friend Connection", "Match-Up", "Buddy Quiz",
        "Time Bomb", "Word Bomb", "Animal Tracker", "Quick Draw", "Hide 'n' Hunt", "Bingo", "Rule Reversal", "Battle",
        "Solo", "openmess", "ranking"]

        if string not in non_minigames:
            return True
        else:
            return False

    def is_in_menu(self):
        current_map = self.dolphin_client.read_byte(GameAddresses.current_map)
        string = map_matches.get(current_map)
        menu_strings = ["boot", "menu", "inst", "loading"]

        if string in menu_strings:
            return True
        else:
            return False

    def is_bgi(self):
        current_map = self.dolphin_client.read_byte(GameAddresses.current_map)
        string = map_matches.get(current_map)

        if string == "Board Game Island":
            return True
        else:
            return False

    def is_globe_trot(self):
        current_map = self.dolphin_client.read_byte(GameAddresses.current_map)
        string = map_matches.get(current_map)

        if string == "Globe Trot":
            return True
        else:
            return False

    def is_mii_of_a_kind(self):
        current_map = self.dolphin_client.read_byte(GameAddresses.current_map)
        string = map_matches.get(current_map)

        if string == "Mii of a Kind":
            return True
        else:
            return False

    def is_spin_off(self):
        current_map = self.dolphin_client.read_byte(GameAddresses.current_map)
        string = map_matches.get(current_map)

        if string == "Spin-Off":
            return True
        else:
            return False

    def is_bingo(self):
        current_map = self.dolphin_client.read_byte(GameAddresses.current_map)
        string = map_matches.get(current_map)

        if string == "Bingo":
            return True
        else:
            return False