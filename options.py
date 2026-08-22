from dataclasses import dataclass
from Options import Choice, OptionSet, PerGameCommonOptions, Range, Toggle, DefaultOnToggle, Visibility, OptionGroup, T


class GameRegion(Choice):
    """What region is your game from?
    This will change names of items/locations to match the region"""
    option_PAL = 1
    option_NTSCU = 2
    default = 1

    @classmethod
    def get_option_name(cls, value: T) -> str:
        match value:
            case 1: return "PAL (Europe / Australia)"
            case 2: return "NTSC-U (US / Canada)"
            case _: return "ERROR"

class PartyGames(OptionSet):
    """Which party games do you want included?
(Board Game Island, Globe Trot, Mii of a Kind (Swap Meet), Spin-Off, Bingo)"""
    display_name = "Party Games"
    valid_keys = {"Board Game Island", "Globe Trot", "Mii of a Kind", "Spin-Off", "Bingo"}
    default = {"Board Game Island", "Globe Trot", "Mii of a Kind", "Spin-Off", "Bingo"}

class RandomiseBGISpots(Toggle):
    """Randomise the spots on Board Game Island (Credit of Dorian)"""
    display_name = "Randomise BGI spots"
    default = False

class FourPlayerMinigames(Toggle):
    """Enables 4 Player Minigames"""
    display_name = "4 Player Minigames"
    default = False

class OnevsThreeMinigames(Toggle):
    """Enables 1 vs 3 Minigames"""
    display_name = "1 vs 3 Minigames"
    default = False

class OnevsOneMinigames(Toggle):
    """Enables 1 vs 1 Minigames"""
    display_name = "1 vs 1 Minigames"
    default = False

class PairMinigames(Toggle):
    """Enables Pair Minigames"""
    display_name = "Pair Minigames"
    default = False

class SkillMinigames(Toggle):
    """Enables skill based minigames for each player type you've enabled"""
    display_name = "Skill Minigames"
    default = False

class LuckMinigames(Toggle):
    """Enables luck based minigames for each player type you've enabled"""
    display_name = "Luck Minigames"
    default = False

class SkluckMinigames(Toggle):
    """Enables minigames that aren't just skill, but also luck based for each player type you've enabled"""
    display_name = "Skill/Luck Minigames"
    default = False

class ReactionMinigames(Toggle):
    """Enables reaction based minigames for each player type you've enabled"""
    display_name = "Reaction Minigames"
    default = False

class PrecisionMinigames(Toggle):
    """Enables precision based minigames for each player type you've enabled"""
    display_name = "Precision Minigames"
    default = False

class PuzzleMinigames(Toggle):
    """Enables puzzle minigames for each player type you've enabled"""
    display_name = "Puzzle Minigames"
    default = False

class TrapChance(Range):
    """The chance a filler is swapped with a trap"""
    display_name = "Trap Chance"
    range_start = 0
    range_end = 99
    default = 20


wii_party_option_groups = [
    OptionGroup("Game Options", [
        GameRegion,
    ]),
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
        ReactionMinigames,
        PrecisionMinigames,
        PuzzleMinigames,
    ]),
    OptionGroup("Miscellaneous Options", [
        TrapChance,
    ])
]


@dataclass
class WiiPartyOptions(PerGameCommonOptions):
    game_region: GameRegion
    party_games: PartyGames
    randomise_bgi_spots: RandomiseBGISpots
    four_player_minigames: FourPlayerMinigames
    one_vs_three_minigames: OnevsThreeMinigames
    one_vs_one_minigames: OnevsOneMinigames
    pair_minigames: PairMinigames
    skill_minigames: SkillMinigames
    luck_minigames: LuckMinigames
    skluck_minigames: SkluckMinigames
    reaction_minigames: ReactionMinigames
    precision_minigames: PrecisionMinigames
    puzzle_minigames: PuzzleMinigames
    trap_chance: TrapChance