from collections.abc import Mapping
from typing import Any, ClassVar
from BaseClasses import Tutorial
import pkgutil
import json
import os
import Utils
from worlds.AutoWorld import WebWorld, World
from .options import wii_party_option_groups, WiiPartyOptions
from . import items, locations, regions, rules
from .items import auto_item_groups, ITEM_NAME_TO_ID
from .locations import auto_location_groups, LOCATION_NAME_TO_ID
from . import settings as wp_settings
from worlds.LauncherComponents import Component, Type, components, launch, icon_paths


def run_client(*args: str) -> None:
    from .wii_party_client.main_client import launch_wii_party_client as launch_wp_client
    launch(launch_wp_client, name="Wii Party Client", args=args)

components.append(
    Component(
        "Wii Party Client",
        func=run_client,
        game_name="Wii Party",
        component_type=Type.CLIENT,
        supports_uri=True,
    )
)

# Find world version

# Read the file data from the APWorld
data = pkgutil.get_data(__name__, "archipelago.json")

if data is not None:
    file = json.loads(data.decode("utf-8"))
    WORLD_VERSION = file["world_version"]
else:
    raise FileNotFoundError("Could not find archipelago.json in the APWorld!")


class WiiPartyWebWorld(WebWorld):
    game = "Wii Party"

    # dirt, grass, grassFlowers, ice, jungle, ocean, partyTime, and stone.
    theme = "partyTime"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Wii Party for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["ElectroStarz"],
    )
    tutorials = [setup_en]

    option_groups = wii_party_option_groups

class WiiPartyWorld(World):
    """
    INSERT DESCRIPTION HERE
    """
    game = "Wii Party"
    web = WiiPartyWebWorld()

    options_dataclass = WiiPartyOptions
    options: WiiPartyOptions


    location_name_to_id = LOCATION_NAME_TO_ID
    item_name_to_id = ITEM_NAME_TO_ID

    item_name_groups = auto_item_groups
    location_name_groups = auto_location_groups

    settings: ClassVar[wp_settings.WPSettings]
    settings_key = wp_settings.WPSettings.settings_key


    origin_region_name = "Main Menu"

    ut_can_gen_without_yaml = True
    ut_generation_options = (
        "game_region",
        "party_games",
        "randomise_bgi_spots",
        "four_player_minigames",
        "one_vs_three_minigames",
        "one_vs_one_minigames",
        "pair_minigames",
        "skill_minigames",
        "luck_minigames",
        "skluck_minigames",
        "reaction_minigames",
        "precision_minigames",
        "puzzle_minigames",
        "trap_chance",
    )

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

        # state = self.multiworld.get_all_state(False)
        #
        # state.update_reachable_regions(self.player)
        #
        # visualize_regions(
        #     self.get_region("Main Menu"),
        #     "wii_party_regions_status.puml",
        #     show_entrance_names=True,
        #     regions_to_highlight=set(state.reachable_regions[self.player])
        # )

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.WPItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def generate_early(self) -> None:
        re_gen_passthrough = getattr(self.multiworld, "re_gen_passthrough", {})
        if re_gen_passthrough and self.game in re_gen_passthrough:
            slot_data = re_gen_passthrough[self.game]
            for option_name, value in slot_data.get("options", {}).items():
                option = getattr(self.options, option_name, None)
                if option is not None:
                    setattr(self.options, option_name, option.from_any(value))

    @staticmethod
    def interpret_slot_data(slot_data: dict[str, Any]) -> dict[str, Any]:
        """Request a Universal Tracker regeneration using the seed's slot data."""
        return slot_data


    # Stuff to send to the client/tracker because it needs to know that
    def fill_slot_data(self) -> Mapping[str, Any]:
        slot_data = {
        "version": WORLD_VERSION,
        "game_region": self.options.game_region.value,
        "party_games": self.options.party_games.value,

        "options": self.options.as_dict(*self.ut_generation_options),
        }

        return slot_data