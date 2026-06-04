from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld, World
from .options import wii_party_option_groups


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