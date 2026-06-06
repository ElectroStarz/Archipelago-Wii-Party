from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import Region

if TYPE_CHECKING:
    from . import WiiPartyWorld


def create_and_connect_regions(world: "WiiPartyWorld") -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: "WiiPartyWorld") -> None:
    main_menu = Region("Main Menu", world.player, world.multiworld)
    bgi = Region("Board Game Island", world.player, world.multiworld)
    globe_trot = Region("Globe Trot", world.player, world.multiworld)
    mii_of_a_kind = Region("Mii Of A Kind", world.player, world.multiworld)
    spin_off = Region("Spin-Off", world.player, world.multiworld)
    bingo = Region("Bingo", world.player, world.multiworld)
    four_minigames = Region("4 Player Minigames", world.player, world.multiworld)
    one_vs_three_minigames = Region("1 vs 3 Minigames", world.player, world.multiworld)
    one_vs_one_minigames = Region("1 vs 1 Minigames", world.player, world.multiworld)
    pair_minigames = Region("Pair Minigames", world.player, world.multiworld)

    regions = [main_menu, bgi, globe_trot, mii_of_a_kind, spin_off, bingo, four_minigames, one_vs_three_minigames,
               one_vs_one_minigames, pair_minigames]

    world.multiworld.regions += regions

def connect_regions(world: "WiiPartyWorld") -> None:
    main_menu = world.get_region("Main Menu")
    bgi = world.get_region("Board Game Island")
    globe_trot = world.get_region("Globe Trot")
    mii_of_a_kind = world.get_region("Mii Of A Kind")
    spin_off = world.get_region("Spin-Off")
    bingo = world.get_region("Bingo")
    four_minigames = world.get_region("4 Player Minigames")
    one_vs_three_minigames = world.get_region("1 vs 3 Minigames")
    one_vs_one_minigames = world.get_region("1 vs 1 Minigames")
    pair_minigames = world.get_region("Pair Minigames")

    # Connect Main Menu to everything
    main_menu.connect(bgi, "Main Menu -> Board Game Island")
    main_menu.connect(globe_trot, "Main Menu -> Globe Trot")
    main_menu.connect(mii_of_a_kind, "Main Menu -> Mii Of A Kind")
    main_menu.connect(spin_off, "Main Menu -> Spin-Off")
    main_menu.connect(bingo, "Main Menu -> Bingo")
    main_menu.connect(four_minigames, "Main Menu -> 4 Player Minigames")
    main_menu.connect(one_vs_three_minigames, "Main Menu -> 1 vs 3 Minigames")
    main_menu.connect(one_vs_one_minigames, "Main Menu -> 1 vs 1 Minigames")
    main_menu.connect(pair_minigames, "Main Menu -> Pair Minigames")

    