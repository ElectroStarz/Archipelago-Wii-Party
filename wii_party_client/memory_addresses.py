class GameAddresses:
    """Addresses to do with anything in-game"""

    current_rel         = 0x803388A3 # Byte
    mini_in_results     = 0x935DDF4E # Halfword
    pg_in_results       = 0x935DFC0A # Halfword
    fp_minigame_submode = 0x80231B48 # Word | Only works on the free-play selection
    game_mode           = 0x80231B40 # Word
    minigame_id         = 0x80235D8C # Word

    game_diff           = 0x80231D75 # Byte

    paused              = 0x80246D18 # Word | Has Pointers


class MenuAddresses:
    """Addresses to do with the menu"""

    button_unlock = 0x80337EA0 # Word

class PlayerAddresses:
    """Addresses to do with the player"""

    minigame_placement = 0x802319AB # Byte | If 4 player minigame type, 0 = 1st, else 1 = Win

class CPUAddresses:
    """Addresses to do with the active CPUs"""

    current_skill = 0x80231D78 # Byte | For all CPUs | 0 = Beginner

class UnlockAddresses:
    """Addresses to do with in-game unlocks"""

    button_unlock  = 0x80337EA0 # Word | Uses custom code by Dorian, see handle_button_unlocks in WPContext.py
    cpu_skill      = 0x802421EE # Byte | 1 = Expert, 2 = Master
    balance_boat_1 = 0x80242214 # Byte | 1 =  Double Up Intermediate, 2 = DU Expert, 3 = Time Attack
    balance_boat_2 = 0x80242215 # Byte | Time Attack Unlocks : 1 = Intermediate, 2 = Expert
    rule_reversal  = 0x80242220 # Byte | 0 = Locked, 1 = Unlocked | This will be 1 as the button unlock will handle this
    solo_mode      = 0x80242225 # Byte | 1 = Intermediate, 2 = Expert

class BGIAddresses:
    """Addresses to do with Board Game Island"""

    generic_data = 0x80246810 # In CAL with Pointers

class Pointers:
    """Pointers for any address"""
    paused = [0x08, 0x10, 0x1D]

    class BGI:
        """Pointers for Board Game Island"""
        to_generic_data = [0x10, 0x18, 0x00, 0x14, 0x98] # Anything inside this will have GD in the comment

        current_turn = [0x1CC] # GD
        player_in_turn_1 = [0x1D0] # GD
        player_in_turn_2 = [0x1D4] # GD
        player_in_turn_3 = [0x1D8] # GD
        player_in_turn_4 = [0x1DC] # GD

        p1_to_goal = [0x1F4] #GD
        p2_to_goal = [0x1F8] #GD
        p3_to_goal = [0x1FC] #GD
        p4_to_goal = [0x200] #GD