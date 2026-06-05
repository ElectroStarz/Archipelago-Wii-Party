from dataclasses import dataclass
from Options import Choice, OptionSet, PerGameCommonOptions, Range, Toggle, DefaultOnToggle, Visibility, OptionGroup

class PartyGames(OptionSet):
    """Which party games do you want included?
(Board Game Island, Globe Trot, Mii Of A Kind (Swap Meet), Spin-Off, Bingo)"""
    display_name = "Party Games"
    valid_keys = {"Board Game Island", "Globe Trot", "Mii Of A Kind", "Spin-Off", "Bingo"}
    default = {"Board Game Island", "Globe Trot", "Mii Of A Kind", "Spin-Off", "Bingo"}

class RandomiseBGISpots(DefaultOnToggle):
    """Randomise the spots on Board Game Island (Credit of Dorian)"""
    display_name = "Randomise BGI spots"

class FourPlayerMinigames(DefaultOnToggle):
    """Enable 4 Player Minigames"""
    display_name = "4 Player Minigames"

class OnevsThreeMinigames(Toggle):
    """Enable 1 vs 3 Minigames"""
    display_name = "1 vs 3 Minigames"
    default = False

class OnevsOneMinigames(Toggle):
    """Enable 1 vs 1 Minigames"""
    display_name = "1 vs 1 Minigames"
    default = False

class PairMinigames(Toggle):
    """Enable Pair Minigames"""
    display_name = "Pair Minigames"
    default = False

class SkillMinigames(DefaultOnToggle):
    """Enable skill based minigames for each player type you've enabled"""
    display_name = "Skill Minigames"

class LuckMinigames(DefaultOnToggle):
    """Enable luck based minigames for each player type you've enabled"""
    display_name = "Luck Minigames"

class SkluckMinigames(DefaultOnToggle):
    """Enables minigames that aren't just skill, but also luck based for each player type you've enabled"""
    display_name = "Skill/Luck Minigames"

class PrecisionMinigames(DefaultOnToggle):
    """Enable precision based minigames for each player type you've enabled"""
    display_name = "Precision Minigames"

class PuzzleMinigames(DefaultOnToggle):
    """Enables puzzle minigames for each player type you've enabled"""
    display_name = "Puzzle Minigames"

class TrapChance(Range):
    """The chance a filler is swapped with a trap"""
    display_name = "Trap Chance"
    range_start = 0
    range_end = 100
    default = 20


wii_party_option_groups = [
    OptionGroup("Party Game Options", [
        PartyGames,
        RandomiseBGISpots,
    ]),
    OptionGroup("Minigame Options", [
        FourPlayerMinigames,
        OnevsThreeMinigames,
        OnevsOneMinigames,
        PairMinigames,
        SkillMinigames,
        LuckMinigames,
        SkluckMinigames,
        PrecisionMinigames,
        PuzzleMinigames,
    ]),
    OptionGroup("Miscellaneous Options", [
        TrapChance,
    ])
]


@dataclass
class WiiPartyOptions(PerGameCommonOptions):
    party_games: PartyGames
    randomise_bgi_spots: RandomiseBGISpots
    four_player_minigames: FourPlayerMinigames
    one_vs_three_minigames: OnevsThreeMinigames
    one_vs_one_minigames: OnevsOneMinigames
    pair_minigames: PairMinigames
    skill_minigames: SkillMinigames
    luck_minigames: LuckMinigames
    skluck_minigames: SkluckMinigames
    precision_minigames: PrecisionMinigames
    puzzle_minigames: PuzzleMinigames
    trap_chance: TrapChance