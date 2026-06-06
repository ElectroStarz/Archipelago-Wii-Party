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

    # === Minigame Types ===
    FOUR_PLAYER = "Four Player Locations"
    ONE_V_THREE = "One v Three Locations"
    ONE_V_ONE = "One v One Locations"
    PAIR = "Pair Locations"

def create_all_locations(world: "WiiPartyWorld") -> None:
    # create_regular_locations(world)
    # create_events(world)
    pass

base_loc_id = 1

bgi_locations: Dict[str, LocationData] = {
    "Test 1": LocationData(base_loc_id + 0, WPGroup.BOARD_GAME_ISLAND),
    "Test 2": LocationData(base_loc_id + 1, WPGroup.BOARD_GAME_ISLAND),
    "Test 3": LocationData(base_loc_id + 2, WPGroup.BOARD_GAME_ISLAND),
    "Test 4": LocationData(base_loc_id + 3, WPGroup.BOARD_GAME_ISLAND),
    "Test 5": LocationData(base_loc_id + 4, WPGroup.BOARD_GAME_ISLAND),
    "Test 6": LocationData(base_loc_id + 5, WPGroup.BOARD_GAME_ISLAND),
    "Test 7": LocationData(base_loc_id + 6, WPGroup.BOARD_GAME_ISLAND),
    "Test 8": LocationData(base_loc_id + 7, WPGroup.BOARD_GAME_ISLAND),
    "Test 9": LocationData(base_loc_id + 8, WPGroup.BOARD_GAME_ISLAND),
    "Test 10": LocationData(base_loc_id + 9, WPGroup.BOARD_GAME_ISLAND),
    "Test 11": LocationData(base_loc_id + 10, WPGroup.BOARD_GAME_ISLAND),
    "Test 12": LocationData(base_loc_id + 11, WPGroup.BOARD_GAME_ISLAND),
    "Test 13": LocationData(base_loc_id + 12, WPGroup.BOARD_GAME_ISLAND),
    "Test 14": LocationData(base_loc_id + 13, WPGroup.BOARD_GAME_ISLAND),
    "Test 15": LocationData(base_loc_id + 14, WPGroup.BOARD_GAME_ISLAND),
    "Test 16": LocationData(base_loc_id + 15, WPGroup.BOARD_GAME_ISLAND),
    "Test 17": LocationData(base_loc_id + 16, WPGroup.BOARD_GAME_ISLAND),
    "Test 18": LocationData(base_loc_id + 17, WPGroup.BOARD_GAME_ISLAND),
    "Test 19": LocationData(base_loc_id + 18, WPGroup.BOARD_GAME_ISLAND),
    "Test 20": LocationData(base_loc_id + 19, WPGroup.BOARD_GAME_ISLAND),
    "Test 21": LocationData(base_loc_id + 20, WPGroup.BOARD_GAME_ISLAND),
    "Test 22": LocationData(base_loc_id + 21, WPGroup.BOARD_GAME_ISLAND),
    "Test 23": LocationData(base_loc_id + 22, WPGroup.BOARD_GAME_ISLAND),
    "Test 24": LocationData(base_loc_id + 23, WPGroup.BOARD_GAME_ISLAND),
    "Test 25": LocationData(base_loc_id + 24, WPGroup.BOARD_GAME_ISLAND),
    "Test 26": LocationData(base_loc_id + 25, WPGroup.BOARD_GAME_ISLAND),
    "Test 27": LocationData(base_loc_id + 26, WPGroup.BOARD_GAME_ISLAND),
    "Test 28": LocationData(base_loc_id + 27, WPGroup.BOARD_GAME_ISLAND),
    "Test 29": LocationData(base_loc_id + 28, WPGroup.BOARD_GAME_ISLAND),
    "Test 30": LocationData(base_loc_id + 29, WPGroup.BOARD_GAME_ISLAND),
    "Test 31": LocationData(base_loc_id + 30, WPGroup.BOARD_GAME_ISLAND),
    "Test 32": LocationData(base_loc_id + 31, WPGroup.BOARD_GAME_ISLAND),
    "Test 33": LocationData(base_loc_id + 32, WPGroup.BOARD_GAME_ISLAND),
    "Test 34": LocationData(base_loc_id + 33, WPGroup.BOARD_GAME_ISLAND),
    "Test 35": LocationData(base_loc_id + 34, WPGroup.BOARD_GAME_ISLAND),
    "Test 36": LocationData(base_loc_id + 35, WPGroup.BOARD_GAME_ISLAND),
    "Test 37": LocationData(base_loc_id + 36, WPGroup.BOARD_GAME_ISLAND),
    "Test 38": LocationData(base_loc_id + 37, WPGroup.BOARD_GAME_ISLAND),
    "Test 39": LocationData(base_loc_id + 38, WPGroup.BOARD_GAME_ISLAND),
    "Test 40": LocationData(base_loc_id + 39, WPGroup.BOARD_GAME_ISLAND),
    "Test 41": LocationData(base_loc_id + 40, WPGroup.BOARD_GAME_ISLAND),
    "Test 42": LocationData(base_loc_id + 41, WPGroup.BOARD_GAME_ISLAND),
    "Test 43": LocationData(base_loc_id + 42, WPGroup.BOARD_GAME_ISLAND),
    "Test 44": LocationData(base_loc_id + 43, WPGroup.BOARD_GAME_ISLAND),
    "Test 45": LocationData(base_loc_id + 44, WPGroup.BOARD_GAME_ISLAND),
    "Test 46": LocationData(base_loc_id + 45, WPGroup.BOARD_GAME_ISLAND),
    "Test 47": LocationData(base_loc_id + 46, WPGroup.BOARD_GAME_ISLAND),
    "Test 48": LocationData(base_loc_id + 47, WPGroup.BOARD_GAME_ISLAND),
    "Test 49": LocationData(base_loc_id + 48, WPGroup.BOARD_GAME_ISLAND),
    "Test 50": LocationData(base_loc_id + 49, WPGroup.BOARD_GAME_ISLAND),
    "Test 51": LocationData(base_loc_id + 50, WPGroup.BOARD_GAME_ISLAND),
    "Test 52": LocationData(base_loc_id + 51, WPGroup.BOARD_GAME_ISLAND),
    "Test 53": LocationData(base_loc_id + 52, WPGroup.BOARD_GAME_ISLAND),
    "Test 54": LocationData(base_loc_id + 53, WPGroup.BOARD_GAME_ISLAND),
    "Test 55": LocationData(base_loc_id + 54, WPGroup.BOARD_GAME_ISLAND),
    "Test 56": LocationData(base_loc_id + 55, WPGroup.BOARD_GAME_ISLAND),
    "Test 57": LocationData(base_loc_id + 56, WPGroup.BOARD_GAME_ISLAND),
    "Test 58": LocationData(base_loc_id + 57, WPGroup.BOARD_GAME_ISLAND),
    "Test 59": LocationData(base_loc_id + 58, WPGroup.BOARD_GAME_ISLAND),
    "Test 60": LocationData(base_loc_id + 59, WPGroup.BOARD_GAME_ISLAND),
}

location_table = {
    **bgi_locations,
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

def create_all_locations(world: WiiPartyWorld):
    create_regular_locations(world)
    create_events(world)

def create_regular_locations(world: WiiPartyWorld) -> None:
    main_menu = world.get_region("Main Menu")
    bgi = world.get_region("Board Game Island")

    bgi_locations_l = get_location_names_with_ids([
        "Test 1", "Test 2", "Test 3", "Test 4", "Test 5",
        "Test 6", "Test 7", "Test 8", "Test 9", "Test 10",
        "Test 11", "Test 12", "Test 13", "Test 14", "Test 15",
        "Test 16", "Test 17", "Test 18", "Test 19", "Test 20",
        "Test 21", "Test 22", "Test 23", "Test 24", "Test 25",
        "Test 26", "Test 27", "Test 28", "Test 29", "Test 30",
        "Test 31", "Test 32", "Test 33", "Test 34", "Test 35",
        "Test 36", "Test 37", "Test 38", "Test 39", "Test 40",
        "Test 41", "Test 42", "Test 43", "Test 44", "Test 45",
        "Test 46", "Test 47", "Test 48", "Test 49", "Test 50",
        "Test 51", "Test 52", "Test 53", "Test 54", "Test 55",
        "Test 56", "Test 57", "Test 58", "Test 59", "Test 60"
    ])
    bgi.add_locations(bgi_locations_l)

def create_events(world: WiiPartyWorld) -> None:
    main_menu = world.get_region("Main Menu")
    bgi = world.get_region("Board Game Island")
    bgi.add_event("Win All BGI!", "Victory!", location_type=WPLocation, item_type=items.WPItem)