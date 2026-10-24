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
    "Rule Reversal": "Spot the Sneak"
}
"""Converts PAL names to the NTSC-U equivalent"""

REL_TO_NAME = {
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

MINIGAME_DATA = {
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
    0x191: ("4 Player", "Smile Snap"),
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

    # Challenge - Not Implemented Yet
    # 0x1f5: ("Challenge", "Marching Orders"),
    # 0x1f6: ("Challenge", "Garden Gridlock"),
    # 0x1f7: ("Challenge", "Shifty Gifts"),
    # 0x1f8: ("Challenge", "Tippy Traverse"),
    # 0x1f9: ("Challenge", "Banana Blockade"),
    # 0x1fa: ("Challenge", "Clover Hunter"),
    # 0x1fb: ("Challenge", "About Face (Solo)"),
    # 0x1fc: ("Challenge", "About Face (4 Player)"),
    # 0x1fd: ("Challenge", "About Face (1 vs 1)"),
}
"""A dictionary of the minigame type and name from the minigame ID"""

MINIGAME_NAME_TO_ID = {data[1]: id for id, data in MINIGAME_DATA.items()}

# === Minigame roulette pool ===
# Addresses are for the PAL build. Each entry is 0x20 bytes: +0x00 = ID, +0x08 = type, +0x19 = in-pool flag.
# Clearing the in-pool flag stops the roulette from ever picking that minigame.
MINIGAME_TABLE_BASE = 0x801DD0E0
MINIGAME_TABLE_STRIDE = 0x20
MINIGAME_IN_POOL_OFFSET = 0x19

MINIGAME_TABLE_ORDER = [
    # 1 vs 1
    100, 101, 102, 104, 106, 107, 108, 109, 110, 111, 112,
    # Pair
    200, 201, 202, 203, 204, 205, 206, 208, 209, 210, 211, 212, 213, 214, 215, 216, 218, 219, 221, 222, 223, 224,
    # 1 vs 3
    300, 301, 302, 303, 304,
    # 4 Player
    400, 401, 402, 403, 404, 405, 406, 407, 408, 410, 411, 412, 413, 414, 415, 416, 418, 419, 420, 421, 422,
    423, 424, 426, 427, 428, 430, 431, 432, 433, 434, 436, 437, 438, 439, 440, 441, 442, 443, 445, 446,
    # The table continues with the Challenge entries (501 to 509). Add them here once they're in MINIGAME_DATA.
]
"""Minigame IDs (decimal, same numbers as the keys in MINIGAME_DATA) in the order they sit in the game's table"""

MINIGAME_ID_TO_POOL_ADDRESS = {
    minigame_id: MINIGAME_TABLE_BASE + index * MINIGAME_TABLE_STRIDE + MINIGAME_IN_POOL_OFFSET
    for index, minigame_id in enumerate(MINIGAME_TABLE_ORDER)
}
"""Minigame ID -> address of its in-pool byte"""

MINIGAME_IDS_BY_TYPE = {}
for _id, (_type, _name) in MINIGAME_DATA.items():
    MINIGAME_IDS_BY_TYPE.setdefault(_type, []).append(_id)
"""Minigame type -> list of minigame IDs we manage"""

NTSCU_TO_PAL = {ntsc: pal for pal, ntsc in PAL_TO_NTSCU.items()}


def minigame_name_to_id(name: str) -> int | None:
    """Minigame ID for a PAL or NTSC-U minigame name. None if the name isn't a minigame we manage."""
    return MINIGAME_NAME_TO_ID.get(NTSCU_TO_PAL.get(name, name))