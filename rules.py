from __future__ import annotations
from typing import TYPE_CHECKING
import re

from rule_builder.rules import *
from .options import *
from .items import minigame_items, MinigameGroup, MinigameType
from .WPUtils import *

if TYPE_CHECKING:
    from . import WiiPartyWorld


def get_correct_name(name: str, world:  WiiPartyWorld):
    """Returns the correct name based on the selected game region"""

    if world.options.game_region.value == GameRegion.option_NTSCU:
        for pal_pattern, ntscu_replacement in PAL_TO_NTSCU.items():
            name = re.sub(pal_pattern, ntscu_replacement, name)

    return name

def set_rule(location: str, rule, world: WiiPartyWorld):
    """I'm tired of writing get_correct_name so much, but I STILL have to
    write it for the rules

    User convenience is a pain in the ass but this is Wii Party AP it must be amazing"""

    world.set_rule(world.get_location(get_correct_name(location, world)), rule)

def set_all_rules(world: WiiPartyWorld) -> None:
    set_all_location_rules(world)
    # set_all_entrance_rules(world)
    set_goal_rules(world)
    set_completion_condition(world)

def set_all_location_rules(world: WiiPartyWorld) -> None:
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

    # Minigame Rules
    for minigame, data in minigame_items.items():

        if not data.type or not data.wp_group:
            continue

        player_option = type_to_option[data.type]
        group_option = group_to_option[data.wp_group]

        if player_option.value and group_option.value:
            set_rule(f"Win {minigame}", Has(get_correct_name(minigame, world)), world)

def set_goal_rules(world: WiiPartyWorld) -> None:
    bgi_rule = Has("Board Game Island")
    world.set_rule(world.get_location("Win Board Game Island!"), bgi_rule)

def set_completion_condition(world: WiiPartyWorld) -> None:
    world.set_completion_rule(Has("Victory!"))