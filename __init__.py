from BaseClasses import Tutorial
from Options import OptionError
from worlds.AutoWorld import WebWorld, World
from .options import wii_party_option_groups, WiiPartyOptions


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

    def create_item(self, name: str) -> items.MSMItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

   # Stuff to send to the client/tracker because it needs to know that
    def fill_slot_data(self) -> Mapping[str, Any]:
        slot_data = {
        "version": WORLD_VERSION,
        "goal_condition": self.options.goal_condition.value,
        "behemoth_hp": self.options.behemoth_hp.value,
        "behemoth_king_hp": self.options.behemoth_king_hp.value,


        "sports_mix_unlock": self.options.sports_mix_unlock.value,
        "exhibition_difficulty": self.options.exhibition_difficulty.value,
        "hard_tournament_difficulty": self.options.hard_tournament_difficulty.value,
        "character_sanity": self.options.character_sanity.value,
        "send_both_character_sanity": self.options.send_both_character_sanity.value,


        "deathlink": self.options.deathlink.value,
        "deathlink_action": self.options.deathlink_action.value,
        "deathlink_consequence": self.options.deathlink_consequence.value,
        "deathlink_opponent_get_points": self.options.deathlink_opponent_get_points.value,
        "deathlink_opponent_scores_points": self.options.deathlink_opponent_scores_points.value,
        "deathlink_boss_health_recovered": self.options.deathlink_boss_health_recovered.value,
        "deathlink_dodgeball_health_lost": self.options.deathlink_dodgeball_health_lost.value,
        }

        return slot_data
