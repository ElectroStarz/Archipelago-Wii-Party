from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING, Dict, List, NamedTuple

from BaseClasses import Location
#from . import items
from .options import *

# if TYPE_CHECKING:
#     from . import WiiPartyWorld

class WPLocation(Location):
    game = "Wii Party"

class WPLocationData(NamedTuple):
    loc_id: int
    loc_group: WPGroup

class WPGroup(Enum):
    Board_Game_Island = 1
    Globe_Trot = 2
    Swap_Meet = 3
    Spin_Off = 4
    Bingo = 5
    Friend_Connection = 6
    Balance_Boat = 7
    Match_Up = 8
    Four_Player = 9
    One_v_Three = 10
    One_v_One = 11
    Pair = 12


base_loc_id = 0

bgi_locations: Dict[str, WPLocationData] = {
    "Win BGI": WPLocationData(base_loc_id + 1, WPGroup.Board_Game_Island), # Don't use this, just a placeholder
}

location_table = {
    **bgi_locations,
}