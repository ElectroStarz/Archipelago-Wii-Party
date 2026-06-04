from dataclasses import dataclass
from Options import Choice, OptionSet, PerGameCommonOptions, Range, Toggle, DefaultOnToggle, Visibility, OptionGroup

class PartyGames(OptionSet):
    """Which party games do you want included?
(Board Game Island, Globe Trot, Swap Meet (Mii of a Kind), Spin-Off, Bingo)"""
    display_name = "Party Games"
    valid_keys = {"Board Game Island", "Globe Trot", "Swap Meet", "Spin-Off", "Bingo"}
    default = {"Board Game Island", "Globe Trot", "Swap Meet", "Spin-Off", "Bingo"}

class SkillMinigames(DefaultOnToggle):
    """Enable skill based minigames"""
    display_name = "Skill Minigames"

class LuckMinigames(DefaultOnToggle):
    """Enable luck based minigames"""
    display_name = "Luck Minigames"

class SkluckMinigames(DefaultOnToggle):
    """Enables minigames that aren't just skill, but also luck based."""
    display_name = "Skill/Luck Minigames"


wii_party_option_groups = [
    OptionGroup("Party Game Options", [
        PartyGames,
    ]),
    OptionGroup("Minigame Options", [
        SkillMinigames,
        LuckMinigames,
        SkluckMinigames,
    ]),
]


@dataclass
class WiiPartyOptions(PerGameCommonOptions):
    party_games: PartyGames
    skill_minigames: SkillMinigames
    luck_minigames: LuckMinigames
    skluck_minigames: SkluckMinigames