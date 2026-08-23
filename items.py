from typing import Dict, NamedTuple, TYPE_CHECKING
from BaseClasses import Item, ItemClassification as IC
from enum import Enum
from .options import *

if TYPE_CHECKING:
    from . import WiiPartyWorld


class WPItem(Item):
    game = "Wii Party"

class ItemGroup(str, Enum):
    BGI = "Board Game Island"
    GLOBE_TROT = "Globe Trot"
    MII_OF_A_KIND = "Mii of a Kind"
    SPIN_OFF = "Spin-Off"
    BINGO = "Bingo"
    MINIGAME = "Minigame"
    FILLER = "Filler"
    TRAPS = "Traps"


class MinigameType(str, Enum):
    FOUR_PLAYER = "Four Player"
    ONE_VS_THREE = "One vs Three"
    ONE_VS_ONE = "One vs One"
    PAIR = "Pair"


class MinigameGroup(str, Enum):
    SKILL = "Skill"
    SKLUCK = "Skill and Luck"
    PRECISION = "Precision"
    REACTION = "Reaction"
    PUZZLE = "Puzzle"
    LUCK = "Luck"

class ItemData(NamedTuple):
    code: int
    classification: IC
    group: ItemGroup
    type: MinigameType | None = None
    wp_group: MinigameGroup | None = None
    quantity: int = 1

# --- ID Offsets ---
base_id = 1
base_game_id = 1000

# --- Board Game Mode Items ---
bgi_items = {
    "Board Game Island": ItemData(base_id + 0, IC.progression | IC.useful, ItemGroup.BGI),
    "Progressive Dice": ItemData(base_id + 1, IC.progression, ItemGroup.BGI, quantity=3),
    "+4 Space": ItemData(base_id + 2, IC.useful, ItemGroup.BGI),
    "+5 Space": ItemData(base_id + 3, IC.useful, ItemGroup.BGI),
    "+6 Space": ItemData(base_id + 4, IC.useful, ItemGroup.BGI),
    "-4 Space": ItemData(base_id + 5, IC.trap, ItemGroup.BGI),
    "Tornado Space": ItemData(base_id + 6, IC.useful, ItemGroup.BGI),
    "UFO Space": ItemData(base_id + 7, IC.useful, ItemGroup.BGI),
    "1 vs 3 Space": ItemData(base_id + 8, IC.useful, ItemGroup.BGI),
    "1 vs 1 Space": ItemData(base_id + 9, IC.useful, ItemGroup.BGI),
    "Dinosaur Space": ItemData(base_id + 10, IC.useful | IC.trap, ItemGroup.BGI),
    "Blue Statue Space": ItemData(base_id + 11, IC.useful, ItemGroup.BGI),
    "Red Statue Space": ItemData(base_id + 12, IC.trap, ItemGroup.BGI),
    "Volcano Space": ItemData(base_id + 13, IC.trap, ItemGroup.BGI),
    "Skull & Crossbones Space": ItemData(base_id + 14, IC.trap, ItemGroup.BGI),
}

gt_items = {
    "Globe Trot": ItemData(base_id + 100, IC.progression | IC.useful, ItemGroup.GLOBE_TROT),
    "Train Card": ItemData(base_id + 101, IC.useful, ItemGroup.GLOBE_TROT),
    "Taxi Card": ItemData(base_id + 102, IC.useful, ItemGroup.GLOBE_TROT),
    "Helicopter Card": ItemData(base_id + 103, IC.useful, ItemGroup.GLOBE_TROT),
    "Airplane Card": ItemData(base_id + 104, IC.useful, ItemGroup.GLOBE_TROT),
    "Hot Air Balloon Card": ItemData(base_id + 105, IC.useful, ItemGroup.GLOBE_TROT),
    "Super Mii": ItemData(base_id + 106, IC.useful, ItemGroup.GLOBE_TROT),
}

mii_of_a_kind_items = {
    "Mii of a Kind": ItemData(base_id + 200, IC.progression | IC.useful, ItemGroup.MII_OF_A_KIND),
    "Clear Mii": ItemData(base_id + 201, IC.useful, ItemGroup.MII_OF_A_KIND),
    "Trade Mii": ItemData(base_id + 202, IC.useful, ItemGroup.MII_OF_A_KIND),
    "Wild Mii": ItemData(base_id + 203, IC.useful, ItemGroup.MII_OF_A_KIND),
}

so_items = {
    "Spin-Off": ItemData(base_id + 300, IC.progression | IC.useful, ItemGroup.SPIN_OFF),
}

bingo_items = {
    "Bingo": ItemData(base_id + 400, IC.progression | IC.useful, ItemGroup.BINGO),
}

# --- Minigame Items ---
minigame_items = {
    # 4-Player (41)
    "Derby Dash":          ItemData(base_game_id + 1,  IC.filler, ItemGroup.MINIGAME, MinigameType.FOUR_PLAYER, MinigameGroup.SKILL),
    "Shifty Gifts":        ItemData(base_game_id + 2,  IC.filler, ItemGroup.MINIGAME, MinigameType.FOUR_PLAYER, MinigameGroup.SKLUCK),
    "Chop Chops":          ItemData(base_game_id + 3,  IC.filler, ItemGroup.MINIGAME, MinigameType.FOUR_PLAYER, MinigameGroup.SKILL),
    "Jumbo Jump":          ItemData(base_game_id + 4,  IC.filler, ItemGroup.MINIGAME, MinigameType.FOUR_PLAYER, MinigameGroup.SKLUCK),
    "Popgun Posse":        ItemData(base_game_id + 5,  IC.filler, ItemGroup.MINIGAME, MinigameType.FOUR_PLAYER, MinigameGroup.PRECISION),
    "Hurdle Hover":        ItemData(base_game_id + 6,  IC.filler, ItemGroup.MINIGAME, MinigameType.FOUR_PLAYER, MinigameGroup.REACTION),
    "Puzzle Pick-Up":      ItemData(base_game_id + 7,  IC.filler, ItemGroup.MINIGAME, MinigameType.FOUR_PLAYER, MinigameGroup.PUZZLE),
    "Lunar Landers":       ItemData(base_game_id + 8,  IC.filler, ItemGroup.MINIGAME, MinigameType.FOUR_PLAYER, MinigameGroup.SKLUCK),
    "Zombie Tag":          ItemData(base_game_id + 9,  IC.filler, ItemGroup.MINIGAME, MinigameType.FOUR_PLAYER, MinigameGroup.SKILL),
    "Flag Fracas":         ItemData(base_game_id + 10, IC.filler, ItemGroup.MINIGAME, MinigameType.FOUR_PLAYER, MinigameGroup.REACTION),
    "Smile Snap":          ItemData(base_game_id + 11, IC.filler, ItemGroup.MINIGAME, MinigameType.FOUR_PLAYER, MinigameGroup.REACTION),
    "Dicey Descent":       ItemData(base_game_id + 12, IC.filler, ItemGroup.MINIGAME, MinigameType.FOUR_PLAYER, MinigameGroup.LUCK),
    "Ram Jam":             ItemData(base_game_id + 13, IC.filler, ItemGroup.MINIGAME, MinigameType.FOUR_PLAYER, MinigameGroup.SKLUCK),
    "Feathered Frenzy":    ItemData(base_game_id + 14, IC.filler, ItemGroup.MINIGAME, MinigameType.FOUR_PLAYER, MinigameGroup.PRECISION),
    "Goal Getters":        ItemData(base_game_id + 15, IC.filler, ItemGroup.MINIGAME, MinigameType.FOUR_PLAYER, MinigameGroup.SKLUCK),
    "Saucer Snap":         ItemData(base_game_id + 16, IC.filler, ItemGroup.MINIGAME, MinigameType.FOUR_PLAYER, MinigameGroup.REACTION),
    "Quicker Chipper":     ItemData(base_game_id + 17, IC.filler, ItemGroup.MINIGAME, MinigameType.FOUR_PLAYER, MinigameGroup.PRECISION),
    "Follow Your Face":    ItemData(base_game_id + 18, IC.filler, ItemGroup.MINIGAME, MinigameType.FOUR_PLAYER, MinigameGroup.SKLUCK),
    "Maze Daze":           ItemData(base_game_id + 19, IC.filler, ItemGroup.MINIGAME, MinigameType.FOUR_PLAYER, MinigameGroup.PUZZLE),
    "Chopper Hoppers":     ItemData(base_game_id + 20, IC.filler, ItemGroup.MINIGAME, MinigameType.FOUR_PLAYER, MinigameGroup.SKLUCK),
    "Space Brawl":         ItemData(base_game_id + 21, IC.filler, ItemGroup.MINIGAME, MinigameType.FOUR_PLAYER, MinigameGroup.SKILL),
    "Stop Watchers":       ItemData(base_game_id + 22, IC.filler, ItemGroup.MINIGAME, MinigameType.FOUR_PLAYER, MinigameGroup.PRECISION),
    "Friendly Face-Off":   ItemData(base_game_id + 23, IC.filler, ItemGroup.MINIGAME, MinigameType.FOUR_PLAYER, MinigameGroup.PUZZLE),
    "Barrel Daredevil":    ItemData(base_game_id + 24, IC.filler, ItemGroup.MINIGAME, MinigameType.FOUR_PLAYER, MinigameGroup.PRECISION),
    "Ball Brawl":          ItemData(base_game_id + 25, IC.filler, ItemGroup.MINIGAME, MinigameType.FOUR_PLAYER, MinigameGroup.SKILL),
    "Tropical Punch":      ItemData(base_game_id + 26, IC.filler, ItemGroup.MINIGAME, MinigameType.FOUR_PLAYER, MinigameGroup.SKILL),
    "Strategy Steps":      ItemData(base_game_id + 27, IC.filler, ItemGroup.MINIGAME, MinigameType.FOUR_PLAYER, MinigameGroup.LUCK),
    "Pearl Plunder":       ItemData(base_game_id + 28, IC.filler, ItemGroup.MINIGAME, MinigameType.FOUR_PLAYER, MinigameGroup.LUCK),
    "Hammer Heads":        ItemData(base_game_id + 29, IC.filler, ItemGroup.MINIGAME, MinigameType.FOUR_PLAYER, MinigameGroup.REACTION),
    "Space Race":          ItemData(base_game_id + 30, IC.filler, ItemGroup.MINIGAME, MinigameType.FOUR_PLAYER, MinigameGroup.SKILL),
    "Lofty Leap":          ItemData(base_game_id + 31, IC.filler, ItemGroup.MINIGAME, MinigameType.FOUR_PLAYER, MinigameGroup.SKILL),
    "Face Flip":           ItemData(base_game_id + 32, IC.filler, ItemGroup.MINIGAME, MinigameType.FOUR_PLAYER, MinigameGroup.LUCK),
    "Spotlight Fight":     ItemData(base_game_id + 33, IC.filler, ItemGroup.MINIGAME, MinigameType.FOUR_PLAYER, MinigameGroup.REACTION),
    "Shutterpup":          ItemData(base_game_id + 34, IC.filler, ItemGroup.MINIGAME, MinigameType.FOUR_PLAYER, MinigameGroup.REACTION),
    "Cry Babies":          ItemData(base_game_id + 35, IC.filler, ItemGroup.MINIGAME, MinigameType.FOUR_PLAYER, MinigameGroup.PRECISION),
    "Lucky Launch":        ItemData(base_game_id + 36, IC.filler, ItemGroup.MINIGAME, MinigameType.FOUR_PLAYER, MinigameGroup.LUCK),
    "Back Attack":         ItemData(base_game_id + 37, IC.filler, ItemGroup.MINIGAME, MinigameType.FOUR_PLAYER, MinigameGroup.SKILL),
    "Chin-Up Champ":       ItemData(base_game_id + 38, IC.filler, ItemGroup.MINIGAME, MinigameType.FOUR_PLAYER, MinigameGroup.SKILL),
    "Walk-Off":            ItemData(base_game_id + 39, IC.filler, ItemGroup.MINIGAME, MinigameType.FOUR_PLAYER, MinigameGroup.PRECISION),
    "Balloon Buggies":     ItemData(base_game_id + 40, IC.filler, ItemGroup.MINIGAME, MinigameType.FOUR_PLAYER, MinigameGroup.SKLUCK),
    "Risky Railway":       ItemData(base_game_id + 41, IC.filler, ItemGroup.MINIGAME, MinigameType.FOUR_PLAYER, MinigameGroup.LUCK),

    # 1 vs 3 (5)
    "Splash Bash":         ItemData(base_game_id + 42, IC.filler, ItemGroup.MINIGAME, MinigameType.ONE_VS_THREE, MinigameGroup.SKILL),
    "Lumber Whacks":       ItemData(base_game_id + 43, IC.filler, ItemGroup.MINIGAME, MinigameType.ONE_VS_THREE, MinigameGroup.REACTION),
    "Flying Fruit":        ItemData(base_game_id + 44, IC.filler, ItemGroup.MINIGAME, MinigameType.ONE_VS_THREE, MinigameGroup.PRECISION),
    "Poserobics":          ItemData(base_game_id + 45, IC.filler, ItemGroup.MINIGAME, MinigameType.ONE_VS_THREE, MinigameGroup.REACTION),
    "Hide-and-Peek":       ItemData(base_game_id + 46, IC.filler, ItemGroup.MINIGAME, MinigameType.ONE_VS_THREE, MinigameGroup.SKILL),

    # 1 vs 1 (11)
    "Commuter Count":      ItemData(base_game_id + 47, IC.filler, ItemGroup.MINIGAME, MinigameType.ONE_VS_ONE, MinigameGroup.PRECISION),
    "Timber Topple":       ItemData(base_game_id + 48, IC.filler, ItemGroup.MINIGAME, MinigameType.ONE_VS_ONE, MinigameGroup.SKILL),
    "Delivery Duel":       ItemData(base_game_id + 49, IC.filler, ItemGroup.MINIGAME, MinigameType.ONE_VS_ONE, MinigameGroup.PRECISION),
    "Shepherd Scramble":   ItemData(base_game_id + 50, IC.filler, ItemGroup.MINIGAME, MinigameType.ONE_VS_ONE, MinigameGroup.SKILL),
    "Channel Changers":    ItemData(base_game_id + 51, IC.filler, ItemGroup.MINIGAME, MinigameType.ONE_VS_ONE, MinigameGroup.REACTION),
    "Spring Time":         ItemData(base_game_id + 52, IC.filler, ItemGroup.MINIGAME, MinigameType.ONE_VS_ONE, MinigameGroup.SKILL),
    "Pop-Up Bandits":      ItemData(base_game_id + 53, IC.filler, ItemGroup.MINIGAME, MinigameType.ONE_VS_ONE, MinigameGroup.LUCK),
    "Poppin' Pilots":      ItemData(base_game_id + 54, IC.filler, ItemGroup.MINIGAME, MinigameType.ONE_VS_ONE, MinigameGroup.SKILL),
    "Flag Footrace":       ItemData(base_game_id + 55, IC.filler, ItemGroup.MINIGAME, MinigameType.ONE_VS_ONE, MinigameGroup.REACTION),
    "Roll to the Goal":    ItemData(base_game_id + 56, IC.filler, ItemGroup.MINIGAME, MinigameType.ONE_VS_ONE, MinigameGroup.PRECISION),
    "Fruit Focus":         ItemData(base_game_id + 57, IC.filler, ItemGroup.MINIGAME, MinigameType.ONE_VS_ONE, MinigameGroup.PUZZLE),

    # Pair (22)
    "Bumper Crops":        ItemData(base_game_id + 58, IC.filler, ItemGroup.MINIGAME, MinigameType.PAIR, MinigameGroup.PRECISION),
    "Robot Factory":       ItemData(base_game_id + 59, IC.filler, ItemGroup.MINIGAME, MinigameType.PAIR, MinigameGroup.REACTION),
    "Paddle Pals":         ItemData(base_game_id + 60, IC.filler, ItemGroup.MINIGAME, MinigameType.PAIR, MinigameGroup.SKILL),
    "Torchlit Terror":     ItemData(base_game_id + 61, IC.filler, ItemGroup.MINIGAME, MinigameType.PAIR, MinigameGroup.SKILL),
    "Basket Bonanza":      ItemData(base_game_id + 62, IC.filler, ItemGroup.MINIGAME, MinigameType.PAIR, MinigameGroup.PRECISION),
    "Tippy Traverse":      ItemData(base_game_id + 63, IC.filler, ItemGroup.MINIGAME, MinigameType.PAIR, MinigameGroup.SKILL),
    "Meet and Greet":      ItemData(base_game_id + 64, IC.filler, ItemGroup.MINIGAME, MinigameType.PAIR, MinigameGroup.PUZZLE),
    "Fishin' Buddies":     ItemData(base_game_id + 65, IC.filler, ItemGroup.MINIGAME, MinigameType.PAIR, MinigameGroup.PRECISION),
    "Pop Coaster":         ItemData(base_game_id + 66, IC.filler, ItemGroup.MINIGAME, MinigameType.PAIR, MinigameGroup.PRECISION),
    "Flycycle Team":       ItemData(base_game_id + 67, IC.filler, ItemGroup.MINIGAME, MinigameType.PAIR, MinigameGroup.SKILL),
    "Sheep Crossing":      ItemData(base_game_id + 68, IC.filler, ItemGroup.MINIGAME, MinigameType.PAIR, MinigameGroup.SKILL),
    "Pump Cart Panic":     ItemData(base_game_id + 69, IC.filler, ItemGroup.MINIGAME, MinigameType.PAIR, MinigameGroup.SKILL),
    "Blastronauts":        ItemData(base_game_id + 70, IC.filler, ItemGroup.MINIGAME, MinigameType.PAIR, MinigameGroup.PRECISION),
    "Rodent Rundown":      ItemData(base_game_id + 71, IC.filler, ItemGroup.MINIGAME, MinigameType.PAIR, MinigameGroup.SKILL),
    "Can Poppers":         ItemData(base_game_id + 72, IC.filler, ItemGroup.MINIGAME, MinigameType.PAIR, MinigameGroup.PRECISION),
    "Spring Ringers":      ItemData(base_game_id + 73, IC.filler, ItemGroup.MINIGAME, MinigameType.PAIR, MinigameGroup.PRECISION),
    "Bobsleigh Highway":   ItemData(base_game_id + 74, IC.filler, ItemGroup.MINIGAME, MinigameType.PAIR, MinigameGroup.SKILL),
    "Skipping Squad":      ItemData(base_game_id + 75, IC.filler, ItemGroup.MINIGAME, MinigameType.PAIR, MinigameGroup.REACTION),
    "Teamwork Temple":     ItemData(base_game_id + 76, IC.filler, ItemGroup.MINIGAME, MinigameType.PAIR, MinigameGroup.PUZZLE),
    "Colour Coordination": ItemData(base_game_id + 77, IC.filler, ItemGroup.MINIGAME, MinigameType.PAIR, MinigameGroup.REACTION),
    "Hidden Charms":       ItemData(base_game_id + 78, IC.filler, ItemGroup.MINIGAME, MinigameType.PAIR, MinigameGroup.LUCK),
    "Banana Blockade":     ItemData(base_game_id + 79, IC.filler, ItemGroup.MINIGAME, MinigameType.PAIR, MinigameGroup.SKILL),
}

filler = {
    "Test Filler": ItemData(base_id + 10000, IC.filler, ItemGroup.FILLER)
}

traps = {
    "Test Trap": ItemData(base_id + 1025, IC.trap, ItemGroup.TRAPS),
}

item_table: Dict[str, ItemData] = {
    **bgi_items,
    **gt_items,
    **mii_of_a_kind_items,
    **so_items,
    **bingo_items,
    **minigame_items,
    **filler,
    **traps,
}

ITEM_NAME_TO_ID: Dict[str, int] = {item_name: item_data.code for item_name, item_data in item_table.items()}

auto_item_groups = {}

for item_name, item_data in item_table.items():
    group_name = item_data.group.value
    if group_name not in auto_item_groups:
        auto_item_groups[group_name] = set()
    auto_item_groups[group_name].add(item_name)


def get_random_filler_item_name(world: "WiiPartyWorld") -> str:
    traps_list = list(traps.keys())
    filler_list = list(filler.keys())
    if world.random.randint(0, 99) < world.options.trap_chance.value:
        return world.random.choice(traps_list)
    return world.random.choice(filler_list)


def create_all_items(world: "WiiPartyWorld") -> None:
    itempool = []

    party_game_mapping = {
        "Board Game Island": bgi_items,
        "Globe Trot": gt_items,
        "Mii of a Kind": mii_of_a_kind_items,
        "Spin-Off": so_items,
        "Bingo": bingo_items
    }

    type_to_option = {
        MinigameType.FOUR_PLAYER: world.options.four_player_minigames,
        MinigameType.ONE_VS_THREE: world.options.one_vs_three_minigames,
        MinigameType.ONE_VS_ONE: world.options.one_vs_one_minigames,
        MinigameType.PAIR: world.options.pair_minigames,
    }

    group_to_option = {
        MinigameGroup.SKILL: world.options.skill_minigames,
        MinigameGroup.REACTION: world.options.reaction_minigames,
        MinigameGroup.LUCK: world.options.luck_minigames,
        MinigameGroup.PRECISION: world.options.precision_minigames,
        MinigameGroup.PUZZLE: world.options.puzzle_minigames,
        MinigameGroup.SKLUCK: world.options.skluck_minigames,
    }

    # Add Mode Items if enabled in Party Games options
    for name in world.options.party_games.value:
        if name in party_game_mapping:
            game_item_dict = party_game_mapping[name]
            for item_name, item_data in game_item_dict.items():
                for _ in range(item_data.quantity):
                    itempool.append(world.create_item(item_name))

    # Add Minigame items if their player size type and group category options are both active
    for item_name, data in minigame_items.items():
        if not data.type or not data.wp_group:
            continue

        player_option = type_to_option[data.type]
        group_option = group_to_option[data.wp_group]

        if player_option.value and group_option.value:
            for _ in range(data.quantity):
                itempool.append(world.create_item(item_name))


    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    # Submit to multiworld
    # print(itempool)
    world.multiworld.itempool += itempool

def create_item_with_correct_classification(world: "WiiPartyWorld", name: str) -> WPItem:
    classification = item_table[name].classification

    return WPItem(name, classification, ITEM_NAME_TO_ID[name], world.player)