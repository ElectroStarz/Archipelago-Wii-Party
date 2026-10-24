from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING, Dict, List, NamedTuple
import re

from BaseClasses import Location, Region
from . import items
from .options import *
from .WPUtils import *

if TYPE_CHECKING:
    from . import WiiPartyWorld

class WPLocation(Location):
    game = "Wii Party"

class LocData(NamedTuple):
    id: int
    type: MinigameType | None
    group: WPGroup

class WPGroup(str, Enum):
    # === Party Games ===
    BOARD_GAME_ISLAND = "Board Game Island Locations"
    GLOBE_TROT = "Globe Trot Locations"
    MII_OF_A_KIND = "Mii Of A Kind Locations"
    SPIN_OFF = "Spin-Off Locations"
    BINGO = "Bingo Locations"

    # === House Party Games ===
    FRIEND_CONNECTION = "Friend Connection Locations"
    BALANCE_BOAT = "Balance Boat Locations"
    MATCH_UP = "Match Up Locations"

    # === Minigame Categories ===
    SKILL = "Skill"
    REACTION = "Reaction"
    LUCK = "Luck"
    PRECISION = "Precision"
    PUZZLE = "Puzzle"
    SKLUCK = "Skill and Luck"


class MinigameType(str, Enum):
    FOUR_PLAYER = "Four Player Locations"
    ONE_VS_THREE = "One vs Three Locations"
    ONE_VS_ONE = "One vs One Locations"
    PAIR = "Pair Locations"

def create_all_locations(world: "WiiPartyWorld") -> None:
    create_regular_locations(world)
    create_events(world)

base_id = 0

minigame_locations = {
    # 4-Player (41)
    "Win Derby Dash":               LocData(base_id + 1, MinigameType.FOUR_PLAYER, WPGroup.SKILL),
    "Win Shifty Gifts":             LocData(base_id + 2, MinigameType.FOUR_PLAYER, WPGroup.SKLUCK),
    "Win Chop Chops":               LocData(base_id + 3, MinigameType.FOUR_PLAYER, WPGroup.SKILL),
    "Win Jumbo Jump":               LocData(base_id + 4, MinigameType.FOUR_PLAYER, WPGroup.SKLUCK),
    "Win Popgun Posse":             LocData(base_id + 5, MinigameType.FOUR_PLAYER, WPGroup.PRECISION),
    "Win Hurdle Hover":             LocData(base_id + 6, MinigameType.FOUR_PLAYER, WPGroup.REACTION),
    "Win Puzzle Pick-Up":           LocData(base_id + 7, MinigameType.FOUR_PLAYER, WPGroup.PUZZLE),
    "Win Lunar Landers":            LocData(base_id + 8, MinigameType.FOUR_PLAYER, WPGroup.SKLUCK),
    "Win Zombie Tag":               LocData(base_id + 9, MinigameType.FOUR_PLAYER, WPGroup.SKILL),
    "Win Flag Fracas":              LocData(base_id + 10, MinigameType.FOUR_PLAYER, WPGroup.REACTION),
    "Win Smile Snap":               LocData(base_id + 11, MinigameType.FOUR_PLAYER, WPGroup.REACTION),
    "Win Dicey Descent":            LocData(base_id + 12, MinigameType.FOUR_PLAYER, WPGroup.LUCK),
    "Win Ram Jam":                  LocData(base_id + 13, MinigameType.FOUR_PLAYER, WPGroup.SKLUCK),
    "Win Feathered Frenzy":         LocData(base_id + 14, MinigameType.FOUR_PLAYER, WPGroup.PRECISION),
    "Win Goal Getters":             LocData(base_id + 15, MinigameType.FOUR_PLAYER, WPGroup.SKLUCK),
    "Win Saucer Snap":              LocData(base_id + 16, MinigameType.FOUR_PLAYER, WPGroup.REACTION),
    "Win Quicker Chipper":          LocData(base_id + 17, MinigameType.FOUR_PLAYER, WPGroup.PRECISION),
    "Win Follow Your Face":         LocData(base_id + 18, MinigameType.FOUR_PLAYER, WPGroup.SKLUCK),
    "Win Maze Daze":                LocData(base_id + 19, MinigameType.FOUR_PLAYER, WPGroup.PUZZLE),
    "Win Chopper Hoppers":          LocData(base_id + 20, MinigameType.FOUR_PLAYER, WPGroup.SKLUCK),
    "Win Space Brawl":              LocData(base_id + 21, MinigameType.FOUR_PLAYER, WPGroup.SKILL),
    "Win Stop Watchers":            LocData(base_id + 22, MinigameType.FOUR_PLAYER, WPGroup.PRECISION),
    "Win Friendly Face-Off":        LocData(base_id + 23, MinigameType.FOUR_PLAYER, WPGroup.PUZZLE),
    "Win Barrel Daredevil":         LocData(base_id + 24, MinigameType.FOUR_PLAYER, WPGroup.PRECISION),
    "Win Ball Brawl":               LocData(base_id + 25, MinigameType.FOUR_PLAYER, WPGroup.SKILL),
    "Win Tropical Punch":           LocData(base_id + 26, MinigameType.FOUR_PLAYER, WPGroup.SKILL),
    "Win Strategy Steps":           LocData(base_id + 27, MinigameType.FOUR_PLAYER, WPGroup.LUCK),
    "Win Pearl Plunder":            LocData(base_id + 28, MinigameType.FOUR_PLAYER, WPGroup.LUCK),
    "Win Hammer Heads":             LocData(base_id + 29, MinigameType.FOUR_PLAYER, WPGroup.REACTION),
    "Win Space Race":               LocData(base_id + 30, MinigameType.FOUR_PLAYER, WPGroup.SKILL),
    "Win Lofty Leap":               LocData(base_id + 31, MinigameType.FOUR_PLAYER, WPGroup.SKILL),
    "Win Face Flip":                LocData(base_id + 32, MinigameType.FOUR_PLAYER, WPGroup.LUCK),
    "Win Spotlight Fight":          LocData(base_id + 33, MinigameType.FOUR_PLAYER, WPGroup.REACTION),
    "Win Shutterpup":               LocData(base_id + 34, MinigameType.FOUR_PLAYER, WPGroup.REACTION),
    "Win Cry Babies":               LocData(base_id + 35, MinigameType.FOUR_PLAYER, WPGroup.PRECISION),
    "Win Lucky Launch":             LocData(base_id + 36, MinigameType.FOUR_PLAYER, WPGroup.LUCK),
    "Win Back Attack":              LocData(base_id + 37, MinigameType.FOUR_PLAYER, WPGroup.SKILL),
    "Win Chin-Up Champ":            LocData(base_id + 38, MinigameType.FOUR_PLAYER, WPGroup.SKILL),
    "Win Walk-Off":                 LocData(base_id + 39, MinigameType.FOUR_PLAYER, WPGroup.PRECISION),
    "Win Balloon Buggies":          LocData(base_id + 40, MinigameType.FOUR_PLAYER, WPGroup.SKLUCK),
    "Win Risky Railway":            LocData(base_id + 41, MinigameType.FOUR_PLAYER, WPGroup.LUCK),

    # 1 vs 3 (5)
    "Win Splash Bash":              LocData(base_id + 42, MinigameType.ONE_VS_THREE, WPGroup.SKILL),
    "Win Lumber Whacks":            LocData(base_id + 43, MinigameType.ONE_VS_THREE, WPGroup.REACTION),
    "Win Flying Fruit":             LocData(base_id + 44, MinigameType.ONE_VS_THREE, WPGroup.PRECISION),
    "Win Poserobics":               LocData(base_id + 45, MinigameType.ONE_VS_THREE, WPGroup.REACTION),
    "Win Hide-and-Peek":            LocData(base_id + 46, MinigameType.ONE_VS_THREE, WPGroup.SKILL),

    # 1 vs 1 (11)
    "Win Commuter Count":           LocData(base_id + 47, MinigameType.ONE_VS_ONE, WPGroup.PRECISION),
    "Win Timber Topple":            LocData(base_id + 48, MinigameType.ONE_VS_ONE, WPGroup.SKILL),
    "Win Delivery Duel":            LocData(base_id + 49, MinigameType.ONE_VS_ONE, WPGroup.PRECISION),
    "Win Shepherd Scramble":        LocData(base_id + 50, MinigameType.ONE_VS_ONE, WPGroup.SKILL),
    "Win Channel Changers":         LocData(base_id + 51, MinigameType.ONE_VS_ONE, WPGroup.REACTION),
    "Win Spring Time":              LocData(base_id + 52, MinigameType.ONE_VS_ONE, WPGroup.SKILL),
    "Win Pop-Up Bandits":           LocData(base_id + 53, MinigameType.ONE_VS_ONE, WPGroup.LUCK),
    "Win Poppin' Pilots":           LocData(base_id + 54, MinigameType.ONE_VS_ONE, WPGroup.SKILL),
    "Win Flag Footrace":            LocData(base_id + 55, MinigameType.ONE_VS_ONE, WPGroup.REACTION),
    "Win Roll to the Goal":         LocData(base_id + 56, MinigameType.ONE_VS_ONE, WPGroup.PRECISION),
    "Win Fruit Focus":              LocData(base_id + 57, MinigameType.ONE_VS_ONE, WPGroup.PUZZLE),

    # Pair (22)
    "Win Bumper Crops":              LocData(base_id + 58, MinigameType.PAIR, WPGroup.PRECISION),
    "Win Robot Factory":             LocData(base_id + 59, MinigameType.PAIR, WPGroup.REACTION),
    "Win Paddle Pals":               LocData(base_id + 60, MinigameType.PAIR, WPGroup.SKILL),
    "Win Torchlit Terror":           LocData(base_id + 61, MinigameType.PAIR, WPGroup.SKILL),
    "Win Basket Bonanza":            LocData(base_id + 62, MinigameType.PAIR, WPGroup.PRECISION),
    "Win Tippy Traverse":            LocData(base_id + 63, MinigameType.PAIR, WPGroup.SKILL),
    "Win Meet and Greet":            LocData(base_id + 64, MinigameType.PAIR, WPGroup.PUZZLE),
    "Win Fishin' Buddies":           LocData(base_id + 65, MinigameType.PAIR, WPGroup.PRECISION),
    "Win Pop Coaster":               LocData(base_id + 66, MinigameType.PAIR, WPGroup.PRECISION),
    "Win Flycycle Team":             LocData(base_id + 67, MinigameType.PAIR, WPGroup.SKILL),
    "Win Sheep Crossing":            LocData(base_id + 68, MinigameType.PAIR, WPGroup.SKILL),
    "Win Pump Cart Panic":           LocData(base_id + 69, MinigameType.PAIR, WPGroup.SKILL),
    "Win Blastronauts":              LocData(base_id + 70, MinigameType.PAIR, WPGroup.PRECISION),
    "Win Rodent Rundown":            LocData(base_id + 71, MinigameType.PAIR, WPGroup.SKILL),
    "Win Can Poppers":               LocData(base_id + 72, MinigameType.PAIR, WPGroup.PRECISION),
    "Win Spring Ringers":            LocData(base_id + 73, MinigameType.PAIR, WPGroup.PRECISION),
    "Win Bobsleigh Highway":         LocData(base_id + 74, MinigameType.PAIR, WPGroup.SKILL),
    "Win Skipping Squad":            LocData(base_id + 75, MinigameType.PAIR, WPGroup.REACTION),
    "Win Teamwork Temple":           LocData(base_id + 76, MinigameType.PAIR, WPGroup.PUZZLE),
    "Win Colour Coordination":       LocData(base_id + 77, MinigameType.PAIR, WPGroup.REACTION),
    "Win Hidden Charms":             LocData(base_id + 78, MinigameType.PAIR, WPGroup.LUCK),
    "Win Banana Blockade":           LocData(base_id + 79, MinigameType.PAIR, WPGroup.SKILL),
}

bgi_locations = {
    "Win Board Game Island":         LocData(base_id + 100, None, WPGroup.BOARD_GAME_ISLAND),
    "Get past the Dragon Wall":      LocData(base_id + 101, None, WPGroup.BOARD_GAME_ISLAND),
    "Get past the Crates & Barrels": LocData(base_id + 102, None, WPGroup.BOARD_GAME_ISLAND),
    "Get past the Volcano Pit":      LocData(base_id + 103, None, WPGroup.BOARD_GAME_ISLAND),
    "Get past the Spike Ball":       LocData(base_id + 104, None, WPGroup.BOARD_GAME_ISLAND),
}

globe_trot_locations = {
    "Win Globe Trot":                LocData(base_id + 200, None, WPGroup.GLOBE_TROT),
}

ntscu_locations = {
    "Win Crash Balls":         LocData(base_id + 100000, MinigameType.FOUR_PLAYER, WPGroup.SKILL),
    "Win Cosmic Capers":       LocData(base_id + 100001, MinigameType.FOUR_PLAYER, WPGroup.SKILL),
    "Win Rope Sling":          LocData(base_id + 100002, MinigameType.FOUR_PLAYER, WPGroup.SKILL),
    "Win Risky Railroad":      LocData(base_id + 100003, MinigameType.FOUR_PLAYER, WPGroup.LUCK),
    "Win Jangle Wranglers":    LocData(base_id + 100004, MinigameType.ONE_VS_ONE, WPGroup.SKILL),
    "Win Flashlight Frights":  LocData(base_id + 100005, MinigameType.PAIR, WPGroup.SKILL),
    "Win Clover Hunt":         LocData(base_id + 100006, MinigameType.PAIR, WPGroup.LUCK),
    "Win Jump Rope Jam":       LocData(base_id + 100007, MinigameType.PAIR, WPGroup.REACTION),
    "Win Bobsled Highway":     LocData(base_id + 100008, MinigameType.PAIR, WPGroup.SKILL),
    "Win Color Coordination":  LocData(base_id + 100009, MinigameType.PAIR, WPGroup.REACTION),
    "Win Moon Landing":        LocData(base_id + 100010, MinigameType.FOUR_PLAYER, WPGroup.SKLUCK),
    "Win Flap Hurdles":        LocData(base_id + 100011, MinigameType.FOUR_PLAYER, WPGroup.REACTION),
}

free_locations = {f"Free {i}": LocData(base_id + 20000 + i, MinigameType.FOUR_PLAYER, WPGroup.SKILL) for i in range(50)}

location_table = {
    **minigame_locations,
    **bgi_locations,
    **ntscu_locations,
    **free_locations
}

LOCATION_NAME_TO_ID = {location_name: data.id for location_name, data in location_table.items()}

auto_location_groups = {}

for loc_name, loc_data in location_table.items():
    group_name = loc_data.group.value
    # If this group isn't in our dictionary yet, create an empty set for it
    if group_name not in auto_location_groups:
        auto_location_groups[group_name] = set()

    # Add the location's name into that group's set
    auto_location_groups[group_name].add(loc_name)

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: location_table[location_name].id for location_name in location_names}


def create_regular_locations(world: WiiPartyWorld) -> None:

    def add_location(location: str, region: Region):
        """Adds the location to the selected region based on the selected game region"""

        if world.options.game_region.value == GameRegion.option_NTSCU:
            for pal_pattern, ntscu_replacement in PAL_TO_NTSCU.items():
                location = re.sub(pal_pattern, ntscu_replacement, location)

        region.add_locations(get_location_names_with_ids([location]))


    main_menu = world.get_region("Main Menu")
    bgi = world.get_region("Board Game Island")
    four_minigames = world.get_region("4 Player Minigames")
    one_vs_three_minigames = world.get_region("1 vs 3 Minigames")
    one_vs_one_minigames = world.get_region("1 vs 1 Minigames")
    pair_minigames = world.get_region("Pair Minigames")

    # Map the player size enum to the actual Region object
    type_to_region = {
        MinigameType.FOUR_PLAYER: four_minigames,
        MinigameType.ONE_VS_THREE: one_vs_three_minigames,
        MinigameType.ONE_VS_ONE: one_vs_one_minigames,
        MinigameType.PAIR: pair_minigames,
    }

    # Map the player size enum to the player's toggle option object
    type_to_option = {
        MinigameType.FOUR_PLAYER: world.options.four_player_minigames,
        MinigameType.ONE_VS_THREE: world.options.one_vs_three_minigames,
        MinigameType.ONE_VS_ONE: world.options.one_vs_one_minigames,
        MinigameType.PAIR: world.options.pair_minigames,
    }

    # Map the group enum to the player's toggle option object
    group_to_option = {
        WPGroup.SKILL: world.options.skill_minigames,
        WPGroup.REACTION: world.options.reaction_minigames,
        WPGroup.LUCK: world.options.luck_minigames,
        WPGroup.PRECISION: world.options.precision_minigames,
        WPGroup.PUZZLE: world.options.puzzle_minigames,
        WPGroup.SKLUCK: world.options.skluck_minigames,
    }

    # Loop through minigames once, look up their specific data properties
    for minigame_name, data in minigame_locations.items():
        # Ensure data and its enums exist
        if not data or not data.type or not data.group:
            continue

        player_option = type_to_option[data.type]
        group_option = group_to_option[data.group]

        # Check .value to see if the user actually enabled both options in their YAML
        if player_option.value and group_option.value:
            region = type_to_region[data.type]
            add_location(minigame_name, region)


    world.get_region("Board Game Island").add_locations(get_location_names_with_ids([loc for loc in free_locations]))

    party_name_to_dict = {
        "Board Game Island": bgi_locations
    }

    party_name_to_region = {
        "Board Game Island": bgi
    }

    for party_game in world.options.party_games.value:
        for loc in party_name_to_dict[party_game]:

            add_location(loc, party_name_to_region[party_game])

def create_events(world: WiiPartyWorld) -> None:
    main_menu = world.get_region("Main Menu")
    bgi = world.get_region("Board Game Island")
    bgi.add_event("Win Board Game Island!", "Victory!", location_type=WPLocation, item_type=items.WPItem)