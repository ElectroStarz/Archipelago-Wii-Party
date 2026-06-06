from typing import Dict, NamedTuple, TYPE_CHECKING
from BaseClasses import Item, ItemClassification as IC
from enum import Enum
from .options import *

if TYPE_CHECKING:
    from . import WiiPartyWorld

class WPItem(Item):
    game: str = "Wii Party"

class ItemGroup(str, Enum):
    BGI = "Board Game Island"
    GLOBE_TROT = "Globe Trot"
    MII_OF_A_KIND = "Mii Of A Kind"
    SPIN_OFF = "Spin-Off"
    BINGO = "Bingo"

    # Minigames
    FOUR_PLAYER_MINIGAMES = "4 Player Minigames"
    ONE_VS_THREE_MINIGAMES = "1 vs 3 Minigames"
    ONE_VS_ONE_MINIGAMES = "1 vs 1 Minigames"
    PAIR_MINIGAMES = "Pair Minigames"

class ItemData(NamedTuple):
    code: int
    classification: IC
    group: ItemGroup
    count: int = 1


base_id = 1

# NOTE: Trap items in some categories will NOT be created when filling the item pool, they're classed as traps because
# of their negative effects/nature. Only traps in trap_items will be created when filling the item pool.

bgi_items = {
    "Board Game Island": ItemData(base_id + 0, IC.progression|IC.useful, ItemGroup.BGI),
    "Progressive Dice": ItemData(base_id + 1, IC.progression, ItemGroup.BGI, 3),
    "+4 Space": ItemData(base_id + 2, IC.useful, ItemGroup.BGI),
    "+5 Space": ItemData(base_id + 3, IC.useful, ItemGroup.BGI),
    "+6 Space": ItemData(base_id + 4, IC.useful, ItemGroup.BGI),
    "-4 Space": ItemData(base_id + 5, IC.trap, ItemGroup.BGI),
    "Tornado Space": ItemData(base_id + 6, IC.useful, ItemGroup.BGI),
    "UFO Space": ItemData(base_id + 7, IC.useful, ItemGroup.BGI),
    "1 vs 3 Space": ItemData(base_id + 8, IC.useful, ItemGroup.BGI),
    "1 vs 1 Space": ItemData(base_id + 9, IC.useful, ItemGroup.BGI),
    "Dinosaur Space": ItemData(base_id + 10, IC.useful|IC.trap, ItemGroup.BGI),
    "Blue Statue Space": ItemData(base_id + 11, IC.useful, ItemGroup.BGI),
    "Red Statue Space": ItemData(base_id + 12, IC.trap, ItemGroup.BGI),
    "Volcano Space": ItemData(base_id + 13, IC.trap, ItemGroup.BGI),
    "Skull & Crossbones Space": ItemData(base_id + 14, IC.trap, ItemGroup.BGI),
}

gt_items = {
    "Globe Trot": ItemData(base_id + 100, IC.progression|IC.useful, ItemGroup.GLOBE_TROT),
    "Train Card": ItemData(base_id + 101, IC.useful, ItemGroup.GLOBE_TROT),
    "Taxi Card": ItemData(base_id + 102, IC.useful, ItemGroup.GLOBE_TROT),
    "Helicopter Card": ItemData(base_id + 103, IC.useful, ItemGroup.GLOBE_TROT),
    "Airplane Card": ItemData(base_id + 104, IC.useful, ItemGroup.GLOBE_TROT),
    "Hot Air Balloon Card": ItemData(base_id + 105, IC.useful, ItemGroup.GLOBE_TROT),
    "Super Mii": ItemData(base_id + 106, IC.useful, ItemGroup.GLOBE_TROT),
}

mii_of_a_kind_items = {
    "Swap Meet": ItemData(base_id + 200, IC.progression|IC.useful, ItemGroup.MII_OF_A_KIND),
    "Clear Mii": ItemData(base_id + 201, IC.useful, ItemGroup.MII_OF_A_KIND),
    "Trade Mii": ItemData(base_id + 202, IC.useful, ItemGroup.MII_OF_A_KIND),
    "Wild Mii": ItemData(base_id + 203, IC.useful, ItemGroup.MII_OF_A_KIND),
}

so_items = {
    "Spin-Off": ItemData(base_id + 300, IC.progression|IC.useful, ItemGroup.SPIN_OFF),
}

bingo_items = {
    "Bingo": ItemData(base_id + 400, IC.progression|IC.useful, ItemGroup.BINGO),
}

# === 4 Player Minigames ===

skill_4_minigames = {
    "Derby Dash": ItemData(base_id + 1000, IC.useful, ItemGroup.FOUR_PLAYER_MINIGAMES),
    "Chop Chops": ItemData(base_id + 1001, IC.useful, ItemGroup.FOUR_PLAYER_MINIGAMES),
    "Zombie Tag": ItemData(base_id + 1002, IC.useful, ItemGroup.FOUR_PLAYER_MINIGAMES),
    "Space Brawl": ItemData(base_id + 1003, IC.useful, ItemGroup.FOUR_PLAYER_MINIGAMES),
    "Ball Brawl": ItemData(base_id + 1004, IC.useful, ItemGroup.FOUR_PLAYER_MINIGAMES),
    "Tropical Punch": ItemData(base_id + 1005, IC.useful, ItemGroup.FOUR_PLAYER_MINIGAMES),
    "Space Race": ItemData(base_id + 1006, IC.useful, ItemGroup.FOUR_PLAYER_MINIGAMES),
    "Lofty Leap": ItemData(base_id + 1007, IC.useful, ItemGroup.FOUR_PLAYER_MINIGAMES),
    "Chin-Up Champ": ItemData(base_id + 1008, IC.useful, ItemGroup.FOUR_PLAYER_MINIGAMES),
    "Back Attack": ItemData(base_id + 1009, IC.useful, ItemGroup.FOUR_PLAYER_MINIGAMES),
}

reaction_4_minigames = {
    "Flap Hurdles": ItemData(base_id + 1010, IC.useful, ItemGroup.FOUR_PLAYER_MINIGAMES),
    "Hurdle Hover": ItemData(base_id + 1011, IC.useful, ItemGroup.FOUR_PLAYER_MINIGAMES),
    "Flag Fracas": ItemData(base_id + 1012, IC.useful, ItemGroup.FOUR_PLAYER_MINIGAMES),
    "Smile Snap": ItemData(base_id + 1013, IC.useful, ItemGroup.FOUR_PLAYER_MINIGAMES),
    "Saucer Snap": ItemData(base_id + 1014, IC.useful, ItemGroup.FOUR_PLAYER_MINIGAMES),
    "Hammer Heads": ItemData(base_id + 1015, IC.useful, ItemGroup.FOUR_PLAYER_MINIGAMES),
    "Spotlight Fight": ItemData(base_id + 1016, IC.useful, ItemGroup.FOUR_PLAYER_MINIGAMES),
    "Shutterpup": ItemData(base_id + 1017, IC.useful, ItemGroup.FOUR_PLAYER_MINIGAMES),
}

luck_4_minigames = {
    "Dicey Descent": ItemData(base_id + 1018, IC.useful, ItemGroup.FOUR_PLAYER_MINIGAMES),
    "Strategy Steps": ItemData(base_id + 1019, IC.useful, ItemGroup.FOUR_PLAYER_MINIGAMES),
    "Pearl Plunder": ItemData(base_id + 1020, IC.useful, ItemGroup.FOUR_PLAYER_MINIGAMES),
    "Face Flip": ItemData(base_id + 1021, IC.useful, ItemGroup.FOUR_PLAYER_MINIGAMES),
    "Lucky Launch": ItemData(base_id + 1022, IC.useful, ItemGroup.FOUR_PLAYER_MINIGAMES),
    "Risky Railway": ItemData(base_id + 1023, IC.useful, ItemGroup.FOUR_PLAYER_MINIGAMES),
}

precision_4_minigames = {
    "Popgun Posse": ItemData(base_id + 1024, IC.useful, ItemGroup.FOUR_PLAYER_MINIGAMES),
    "Feathered Frenzy": ItemData(base_id + 1025, IC.useful, ItemGroup.FOUR_PLAYER_MINIGAMES),
    "Quicker Chipper": ItemData(base_id + 1026, IC.useful, ItemGroup.FOUR_PLAYER_MINIGAMES),
    "Barrel Daredevil": ItemData(base_id + 1027, IC.useful, ItemGroup.FOUR_PLAYER_MINIGAMES),
    "Cry Babies": ItemData(base_id + 1028, IC.useful, ItemGroup.FOUR_PLAYER_MINIGAMES),
    "Walk-Off": ItemData(base_id + 1029, IC.useful, ItemGroup.FOUR_PLAYER_MINIGAMES),
    "Stop Watchers": ItemData(base_id + 1030, IC.useful, ItemGroup.FOUR_PLAYER_MINIGAMES),
}

puzzle_4_minigames = {
    "Puzzle Pick-Up": ItemData(base_id + 1031, IC.useful, ItemGroup.FOUR_PLAYER_MINIGAMES),
    "Maze Daze": ItemData(base_id + 1032, IC.useful, ItemGroup.FOUR_PLAYER_MINIGAMES),
    "Friendly Face-Off": ItemData(base_id + 1033, IC.useful, ItemGroup.FOUR_PLAYER_MINIGAMES),
}

# Minigames that are some skill, some luck
skill_and_luck_4_minigames = {
    "Lunar Landers": ItemData(base_id + 1034, IC.useful, ItemGroup.FOUR_PLAYER_MINIGAMES),
    "Ram Jam": ItemData(base_id + 1035, IC.useful, ItemGroup.FOUR_PLAYER_MINIGAMES),
    "Goal Getters": ItemData(base_id + 1036, IC.useful, ItemGroup.FOUR_PLAYER_MINIGAMES),
    "Follow Your Face": ItemData(base_id + 1037, IC.useful, ItemGroup.FOUR_PLAYER_MINIGAMES),
    "Balloon Buggies": ItemData(base_id + 1038, IC.useful, ItemGroup.FOUR_PLAYER_MINIGAMES),
    "Chopper Hoppers": ItemData(base_id + 1039, IC.useful, ItemGroup.FOUR_PLAYER_MINIGAMES),
    "Jumbo Jump": ItemData(base_id + 1040, IC.useful, ItemGroup.FOUR_PLAYER_MINIGAMES),
}

# === 1 vs 3 Minigames ===



filler = {}

traps = {}

item_table: Dict[str, ItemData] = {
    **bgi_items,
    **gt_items,
    **mii_of_a_kind_items,
    **so_items,
    **bingo_items,
    **skill_4_minigames,
    **luck_4_minigames,
    **puzzle_4_minigames,
    **skill_and_luck_4_minigames,
}

ITEM_NAME_TO_ID: Dict[str, int] = {item_name: data.code for item_name, data in item_table.items()}

auto_item_groups = {}

# Loop through every single location
for item_name, item_data in item_table.items():

    group_name = item_data.group.value
    # If this group isn't in our dictionary yet, create an empty set for it
    if group_name not in auto_item_groups:
        auto_item_groups[group_name] = set()

    # Add the location's name into that group's set
    auto_item_groups[group_name].add(item_name)

def get_random_filler_item_name(world: "WiiPartyWorld") -> str:
    traps_list = [name for name, data in traps.items()]
    filler_list = [name for name, data in filler.items()]
    if world.random.randint(0, 99) < world.options.trap_chance:
        return world.random.choice(traps_list)
    return world.random.choice(filler_list)

def create_all_items(world: "WiiPartyWorld") -> None:
    itempool = []

    minigame_type_options = [SkillMinigames, LuckMinigames, SkluckMinigames, PrecisionMinigames, PuzzleMinigames]

    party_game_mapping = {
        "Board Game Island": bgi_items,
        "Globe Trot": gt_items,
        "Mii Of A Kind": mii_of_a_kind_items,
        "Spin-Off": so_items,
        "Bingo": bingo_items
    }

    world_to_var = {
        SkillMinigames: world.options.skill_minigames,
        LuckMinigames: world.options.luck_minigames,
        SkluckMinigames: world.options.skluck_minigames,
        PrecisionMinigames: world.options.precision_minigames,
        PuzzleMinigames: world.options.puzzle_minigames,
    }

    for name in world.options.party_games.value:
        if name in party_game_mapping:
            game_item_dict = party_game_mapping[name]

            for item_name, data in game_item_dict:
                ap_item = world.create_item(item_name)
                itempool.append(ap_item)

    four_minigame_type_mapping = {
        SkillMinigames: skill_4_minigames,
        LuckMinigames: luck_4_minigames,
        SkluckMinigames: skill_and_luck_4_minigames,
        PrecisionMinigames: precision_4_minigames,
        PuzzleMinigames: puzzle_4_minigames,
    }

    if world.options.four_player_minigames == FourPlayerMinigames.option_true:
        for type in minigame_type_options:
            world_var = world_to_var[type]
            if world_var == type.option_true:
                minigame_item_dict = four_minigame_type_mapping[type]

                for item_name in minigame_item_dict:
                    ap_item = world.create_item(item_name)
                    itempool.append(ap_item)





    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    # Submit to multiworld
    #print(itempool)
    world.multiworld.itempool += itempool


def create_item_with_correct_classification(world: "WiiPartyWorld", name: str) -> WPItem:
    classification = item_table[name].classification

    return WPItem(name, classification, ITEM_NAME_TO_ID[name], world.player)