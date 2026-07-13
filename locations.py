from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING, Dict, List, NamedTuple

from BaseClasses import Location
from . import items
from .options import *

if TYPE_CHECKING:
    from . import WiiPartyWorld

class WPLocation(Location):
    game = "Wii Party"

class LocationData(NamedTuple):
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

base_loc_id = 0

minigame_locations = {
# 4-Player (41)
    "Win Derby Dash":          LocationData(base_loc_id + 1,  MinigameType.FOUR_PLAYER, WPGroup.SKILL),
    "Win Shifty Gifts":        LocationData(base_loc_id + 2,  MinigameType.FOUR_PLAYER, WPGroup.SKLUCK),
    "Win Chop Chops":          LocationData(base_loc_id + 3,  MinigameType.FOUR_PLAYER, WPGroup.SKILL),
    "Win Jumbo Jump":          LocationData(base_loc_id + 4,  MinigameType.FOUR_PLAYER, WPGroup.SKLUCK),
    "Win Popgun Posse":        LocationData(base_loc_id + 5,  MinigameType.FOUR_PLAYER, WPGroup.PRECISION),
    "Win Hurdle Hover":        LocationData(base_loc_id + 6,  MinigameType.FOUR_PLAYER, WPGroup.REACTION),
    "Win Puzzle Pick-Up":      LocationData(base_loc_id + 7,  MinigameType.FOUR_PLAYER, WPGroup.PUZZLE),
    "Win Lunar Landers":       LocationData(base_loc_id + 8,  MinigameType.FOUR_PLAYER, WPGroup.SKLUCK),
    "Win Zombie Tag":          LocationData(base_loc_id + 9,  MinigameType.FOUR_PLAYER, WPGroup.SKILL),
    "Win Flag Fracas":         LocationData(base_loc_id + 10, MinigameType.FOUR_PLAYER, WPGroup.REACTION),
    "Win Smile Snap":          LocationData(base_loc_id + 11, MinigameType.FOUR_PLAYER, WPGroup.REACTION),
    "Win Dicey Descent":       LocationData(base_loc_id + 12, MinigameType.FOUR_PLAYER, WPGroup.LUCK),
    "Win Ram Jam":             LocationData(base_loc_id + 13, MinigameType.FOUR_PLAYER, WPGroup.SKLUCK),
    "Win Feathered Frenzy":    LocationData(base_loc_id + 14, MinigameType.FOUR_PLAYER, WPGroup.PRECISION),
    "Win Goal Getters":        LocationData(base_loc_id + 15, MinigameType.FOUR_PLAYER, WPGroup.SKLUCK),
    "Win Saucer Snap":         LocationData(base_loc_id + 16, MinigameType.FOUR_PLAYER, WPGroup.REACTION),
    "Win Quicker Chipper":     LocationData(base_loc_id + 17, MinigameType.FOUR_PLAYER, WPGroup.PRECISION),
    "Win Follow Your Face":    LocationData(base_loc_id + 18, MinigameType.FOUR_PLAYER, WPGroup.SKLUCK),
    "Win Maze Daze":           LocationData(base_loc_id + 19, MinigameType.FOUR_PLAYER, WPGroup.PUZZLE),
    "Win Chopper Hoppers":     LocationData(base_loc_id + 20, MinigameType.FOUR_PLAYER, WPGroup.SKLUCK),
    "Win Space Brawl":         LocationData(base_loc_id + 21, MinigameType.FOUR_PLAYER, WPGroup.SKILL),
    "Win Stop Watchers":       LocationData(base_loc_id + 22, MinigameType.FOUR_PLAYER, WPGroup.PRECISION),
    "Win Friendly Face-Off":   LocationData(base_loc_id + 23, MinigameType.FOUR_PLAYER, WPGroup.PUZZLE),
    "Win Barrel Daredevil":    LocationData(base_loc_id + 24, MinigameType.FOUR_PLAYER, WPGroup.PRECISION),
    "Win Ball Brawl":          LocationData(base_loc_id + 25, MinigameType.FOUR_PLAYER, WPGroup.SKILL),
    "Win Tropical Punch":      LocationData(base_loc_id + 26, MinigameType.FOUR_PLAYER, WPGroup.SKILL),
    "Win Strategy Steps":      LocationData(base_loc_id + 27, MinigameType.FOUR_PLAYER, WPGroup.LUCK),
    "Win Pearl Plunder":       LocationData(base_loc_id + 28, MinigameType.FOUR_PLAYER, WPGroup.LUCK),
    "Win Hammer Heads":        LocationData(base_loc_id + 29, MinigameType.FOUR_PLAYER, WPGroup.REACTION),
    "Win Space Race":          LocationData(base_loc_id + 30, MinigameType.FOUR_PLAYER, WPGroup.SKILL),
    "Win Lofty Leap":          LocationData(base_loc_id + 31, MinigameType.FOUR_PLAYER, WPGroup.SKILL),
    "Win Face Flip":           LocationData(base_loc_id + 32, MinigameType.FOUR_PLAYER, WPGroup.LUCK),
    "Win Spotlight Fight":     LocationData(base_loc_id + 33, MinigameType.FOUR_PLAYER, WPGroup.REACTION),
    "Win Shutterpup":          LocationData(base_loc_id + 34, MinigameType.FOUR_PLAYER, WPGroup.REACTION),
    "Win Cry Babies":          LocationData(base_loc_id + 35, MinigameType.FOUR_PLAYER, WPGroup.PRECISION),
    "Win Lucky Launch":        LocationData(base_loc_id + 36, MinigameType.FOUR_PLAYER, WPGroup.LUCK),
    "Win Back Attack":         LocationData(base_loc_id + 37, MinigameType.FOUR_PLAYER, WPGroup.SKILL),
    "Win Chin-Up Champ":       LocationData(base_loc_id + 38, MinigameType.FOUR_PLAYER, WPGroup.SKILL),
    "Win Walk-Off":            LocationData(base_loc_id + 39, MinigameType.FOUR_PLAYER, WPGroup.PRECISION),
    "Win Balloon Buggies":     LocationData(base_loc_id + 40, MinigameType.FOUR_PLAYER, WPGroup.SKLUCK),
    "Win Risky Railway":       LocationData(base_loc_id + 41, MinigameType.FOUR_PLAYER, WPGroup.LUCK),

    # 1 vs 3 (5)
    "Win Splash Bash":         LocationData(base_loc_id + 42, MinigameType.ONE_VS_THREE, WPGroup.SKILL),
    "Win Lumber Whacks":       LocationData(base_loc_id + 43, MinigameType.ONE_VS_THREE, WPGroup.REACTION),
    "Win Flying Fruit":        LocationData(base_loc_id + 44, MinigameType.ONE_VS_THREE, WPGroup.PRECISION),
    "Win Poserobics":          LocationData(base_loc_id + 45, MinigameType.ONE_VS_THREE, WPGroup.REACTION),
    "Win Hide-and-Peek":       LocationData(base_loc_id + 46, MinigameType.ONE_VS_THREE, WPGroup.SKILL),

    # 1 vs 1 (11)
    "Win Commuter Count":      LocationData(base_loc_id + 47, MinigameType.ONE_VS_ONE, WPGroup.PRECISION),
    "Win Timber Topple":       LocationData(base_loc_id + 48, MinigameType.ONE_VS_ONE, WPGroup.SKILL),
    "Win Delivery Duel":       LocationData(base_loc_id + 49, MinigameType.ONE_VS_ONE, WPGroup.PRECISION),
    "Win Shepherd Scramble":   LocationData(base_loc_id + 50, MinigameType.ONE_VS_ONE, WPGroup.SKILL),
    "Win Channel Changers":    LocationData(base_loc_id + 51, MinigameType.ONE_VS_ONE, WPGroup.REACTION),
    "Win Spring Time":         LocationData(base_loc_id + 52, MinigameType.ONE_VS_ONE, WPGroup.SKILL),
    "Win Pop-Up Bandits":      LocationData(base_loc_id + 53, MinigameType.ONE_VS_ONE, WPGroup.LUCK),
    "Win Poppin' Pilots":      LocationData(base_loc_id + 54, MinigameType.ONE_VS_ONE, WPGroup.SKILL),
    "Win Flag Footrace":       LocationData(base_loc_id + 55, MinigameType.ONE_VS_ONE, WPGroup.REACTION),
    "Win Roll to the Goal":    LocationData(base_loc_id + 56, MinigameType.ONE_VS_ONE, WPGroup.PRECISION),
    "Win Fruit Focus":         LocationData(base_loc_id + 57, MinigameType.ONE_VS_ONE, WPGroup.PUZZLE),

    # Pair (22)
    "Win Bumper Crops":        LocationData(base_loc_id + 58, MinigameType.PAIR, WPGroup.PRECISION),
    "Win Robot Factory":       LocationData(base_loc_id + 59, MinigameType.PAIR, WPGroup.REACTION),
    "Win Paddle Pals":         LocationData(base_loc_id + 60, MinigameType.PAIR, WPGroup.SKILL),
    "Win Torchlit Terror":     LocationData(base_loc_id + 61, MinigameType.PAIR, WPGroup.SKILL),
    "Win Basket Bonanza":      LocationData(base_loc_id + 62, MinigameType.PAIR, WPGroup.PRECISION),
    "Win Tippy Traverse":      LocationData(base_loc_id + 63, MinigameType.PAIR, WPGroup.SKILL),
    "Win Meet and Greet":      LocationData(base_loc_id + 64, MinigameType.PAIR, WPGroup.PUZZLE),
    "Win Fishin' Buddies":     LocationData(base_loc_id + 65, MinigameType.PAIR, WPGroup.PRECISION),
    "Win Pop Coaster":         LocationData(base_loc_id + 66, MinigameType.PAIR, WPGroup.PRECISION),
    "Win Flycycle Team":       LocationData(base_loc_id + 67, MinigameType.PAIR, WPGroup.SKILL),
    "Win Sheep Crossing":      LocationData(base_loc_id + 68, MinigameType.PAIR, WPGroup.SKILL),
    "Win Pump Cart Panic":     LocationData(base_loc_id + 69, MinigameType.PAIR, WPGroup.SKILL),
    "Win Blastronauts":        LocationData(base_loc_id + 70, MinigameType.PAIR, WPGroup.PRECISION),
    "Win Rodent Rundown":      LocationData(base_loc_id + 71, MinigameType.PAIR, WPGroup.SKILL),
    "Win Can Poppers":         LocationData(base_loc_id + 72, MinigameType.PAIR, WPGroup.PRECISION),
    "Win Spring Ringers":      LocationData(base_loc_id + 73, MinigameType.PAIR, WPGroup.PRECISION),
    "Win Bobsleigh Highway":   LocationData(base_loc_id + 74, MinigameType.PAIR, WPGroup.SKILL),
    "Win Skipping Squad":      LocationData(base_loc_id + 75, MinigameType.PAIR, WPGroup.REACTION),
    "Win Teamwork Temple":     LocationData(base_loc_id + 76, MinigameType.PAIR, WPGroup.PUZZLE),
    "Win Colour Coordination": LocationData(base_loc_id + 77, MinigameType.PAIR, WPGroup.REACTION),
    "Win Hidden Charms":       LocationData(base_loc_id + 78, MinigameType.PAIR, WPGroup.LUCK),
    "Win Banana Blockade":     LocationData(base_loc_id + 79, MinigameType.PAIR, WPGroup.SKILL),
}

location_table = {
    **minigame_locations,
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
    main_menu = world.get_region("Main Menu")
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

        player_option = type_to_option.get(data.type)
        group_option = group_to_option.get(data.group)

        # Check .value to see if the user actually enabled both options in their YAML
        if player_option and player_option.value and group_option and group_option.value:
            region = type_to_region[data.type]
            region.add_locations(get_location_names_with_ids([minigame_name]))

def create_events(world: WiiPartyWorld) -> None:
    main_menu = world.get_region("Main Menu")
    bgi = world.get_region("Board Game Island")
    bgi.add_event("Win All BGI!", "Victory!", location_type=WPLocation, item_type=items.WPItem)