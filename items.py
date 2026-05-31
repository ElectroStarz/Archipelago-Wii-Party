from typing import Dict, NamedTuple, TYPE_CHECKING
from BaseClasses import Item, ItemClassification as IC
from .options import *

# if TYPE_CHECKING:
#     from . import MSMWorld

class WPItem(Item):
    game: str = "Wii Party"

class ItemData(NamedTuple):
    code: int
    classification: IC
    count: int = 1

base_id = 1

# NOTE: Trap items in some categories will NOT be created when filling the item pool, they're classed as traps because
# of their negative effects/nature. Only traps in trap_items will be created when filling the item pool.

bgi_items = {
    "Board Game Island": ItemData(base_id + 0, IC.progression|IC.useful),
    "Progressive Dice": ItemData(base_id + 1, IC.progression, 3),
    "+4 Space": ItemData(base_id + 2, IC.useful),
    "+5 Space": ItemData(base_id + 3, IC.useful),
    "+6 Space": ItemData(base_id + 4, IC.useful),
    "-4 Space": ItemData(base_id + 5, IC.trap),
    "Tornado Space": ItemData(base_id + 6, IC.useful),
    "UFO Space": ItemData(base_id + 7, IC.useful),
    "1 vs 3 Space": ItemData(base_id + 8, IC.useful),
    "1 vs 1 Space": ItemData(base_id + 9, IC.useful),
    "Dinosaur Space": ItemData(base_id + 10, IC.useful|IC.trap),
    "Blue Statue Space": ItemData(base_id + 11, IC.useful),
    "Red Statue Space": ItemData(base_id + 12, IC.trap),
    "Volcano Space": ItemData(base_id + 13, IC.trap),
    "Skull & Crossbones Space": ItemData(base_id + 14, IC.trap),
}

gt_items = {
    "Globe Trot": ItemData(base_id + 100, IC.progression|IC.useful),
    "Train Card": ItemData(base_id + 101, IC.useful),
    "Taxi Card": ItemData(base_id + 102, IC.useful),
    "Helicopter Card": ItemData(base_id + 103, IC.useful),
    "Airplane Card": ItemData(base_id + 104, IC.useful),
    "Hot Air Balloon Card": ItemData(base_id + 105, IC.useful),
    "Super Mii": ItemData(base_id + 106, IC.useful),
}

sm_items = {
    "Swap Meet": ItemData(base_id + 200, IC.progression|IC.useful),
    "Clear Mii": ItemData(base_id + 201, IC.useful),
    "Trade Mii": ItemData(base_id + 202, IC.useful),
    "Wild Mii": ItemData(base_id + 203, IC.useful),
}

so_items = {
    "Spin-Off": ItemData(base_id + 300, IC.progression|IC.useful),
}

bingo_items = {
    "Bingo": ItemData(base_id + 400, IC.progression|IC.useful),
}

# === Minigames ===

skill_minigames = {
    "Derby Dash": ItemData(base_id + 1000, IC.useful),
    "Chop Chops": ItemData(base_id + 1001, IC.useful),
    "Zombie Tag": ItemData(base_id + 1002, IC.useful),
    "Space Brawl": ItemData(base_id + 1003, IC.useful),
    "Ball Brawl": ItemData(base_id + 1004, IC.useful),
    "Tropical Punch": ItemData(base_id + 1005, IC.useful),
    "Space Race": ItemData(base_id + 1006, IC.useful),
    "Lofty Leap": ItemData(base_id + 1007, IC.useful),
    "Chin-Up Champ": ItemData(base_id + 1008, IC.useful),
    "Back Attack": ItemData(base_id + 1009, IC.useful),
}


reaction_minigames = {
    "Flap Hurdles": ItemData(base_id + 1010, IC.useful),
    "Hurdle Hover": ItemData(base_id + 1011, IC.useful),
    "Flag Fracas": ItemData(base_id + 1012, IC.useful),
    "Smile Snap": ItemData(base_id + 1013, IC.useful),
    "Saucer Snap": ItemData(base_id + 1014, IC.useful),
    "Hammer Heads": ItemData(base_id + 1015, IC.useful),
    "Spotlight Fight": ItemData(base_id + 1016, IC.useful),
    "Shutterpup": ItemData(base_id + 1017, IC.useful),
}


luck_minigames = {
    "Dicey Descent": ItemData(base_id + 1018, IC.useful),
    "Strategy Steps": ItemData(base_id + 1019, IC.useful),
    "Pearl Plunder": ItemData(base_id + 1020, IC.useful),
    "Face Flip": ItemData(base_id + 1021, IC.useful),
    "Lucky Launch": ItemData(base_id + 1022, IC.useful),
    "Risky Railway": ItemData(base_id + 1023, IC.useful),
}


precision_minigames = {
    "Popgun Posse": ItemData(base_id + 1024, IC.useful),
    "Feathered Frenzy": ItemData(base_id + 1025, IC.useful),
    "Quicker Chipper": ItemData(base_id + 1026, IC.useful),
    "Barrel Daredevil": ItemData(base_id + 1027, IC.useful),
    "Cry Babies": ItemData(base_id + 1028, IC.useful),
    "Walk-Off": ItemData(base_id + 1029, IC.useful),
    "Stop Watchers": ItemData(base_id + 1030, IC.useful),
}


puzzle_minigames = {
    "Puzzle Pick-Up": ItemData(base_id + 1031, IC.useful),
    "Maze Daze": ItemData(base_id + 1032, IC.useful),
    "Friendly Face-Off": ItemData(base_id + 1033, IC.useful),
}

# Minigames that are some skill, some luck
skill_and_luck_minigames = {
    "Lunar Landers": ItemData(base_id + 1034, IC.useful),
    "Ram Jam": ItemData(base_id + 1035, IC.useful),
    "Goal Getters": ItemData(base_id + 1036, IC.useful),
    "Follow Your Face": ItemData(base_id + 1037, IC.useful),
    "Balloon Buggies": ItemData(base_id + 1038, IC.useful),
    "Chopper Hoppers": ItemData(base_id + 1039, IC.useful),
    "Jumbo Jump": ItemData(base_id + 1040, IC.useful),
}

item_table: Dict[str, ItemData] = {
    **bgi_items,
    **gt_items,
    **sm_items,
    **so_items,
    **bingo_items,
    **skill_minigames,
    **luck_minigames,
    **puzzle_minigames,
    **skill_and_luck_minigames,
}