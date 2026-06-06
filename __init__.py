from collections.abc import Mapping
from typing import Any
from BaseClasses import Tutorial
import pkgutil
import json
from worlds.AutoWorld import WebWorld, World
from .options import wii_party_option_groups, WiiPartyOptions
from . import components, items, locations, regions, rules
from .items import auto_item_groups, ITEM_NAME_TO_ID
from .locations import auto_location_groups, LOCATION_NAME_TO_ID


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


    origin_region_name = "Main Menu"

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

        # state = self.multiworld.get_all_state(False)
        #
        # state.update_reachable_regions(self.player)
        #
        # visualize_regions(
        #     self.get_region("Main Menu"),
        #     "mario_sports_mix_regions_status.puml",
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

   # Stuff to send to the client/tracker because it needs to know that
    def fill_slot_data(self) -> Mapping[str, Any]:
        slot_data = {
        "version": WORLD_VERSION,
        }

        return slot_data
