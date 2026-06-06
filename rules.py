from __future__ import annotations
from typing import TYPE_CHECKING

from rule_builder.rules import Has, HasAll, CanReachLocation, OptionFilter#, AtLeast
from .options import *

if TYPE_CHECKING:
    from . import WiiPartyWorld

def set_all_rules(world: WiiPartyWorld) -> None:
    # set_all_location_rules(world)
    # set_all_entrance_rules(world)
    # set_goal_rules(world)
    # set_completion_condition(world)
    pass

def set_goal_rules(world: WiiPartyWorld) -> None:
    bgi_rule = Has("Board Game Island")
    world.set_rule(world.get_location("Win All BGI!"), bgi_rule)