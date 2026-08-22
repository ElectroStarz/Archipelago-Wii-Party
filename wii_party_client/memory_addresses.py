class GameAddresses:
    current_rel = 0x803388A3 # Byte
    mini_in_results = 0x935DDF4E # Halfword
    pg_in_results = 0x935DFC0A # Halfword
    fp_minigame_submode = 0x80231B48 # Word | Only works on the free-play selection
    game_mode = 0x80231B40 # Word
    minigame_id = 0x80235D8C # Word

class MenuAddresses:
    button_unlock = 0x80337EA0 # Word

class PlayerAddresses:
    minigame_placement = 0x802319AB # Byte | If 4 player minigame type, 0 = 1st, else 1 = Win

class CPUAddresses:
    skill = 0x80231D78 # Byte | For all CPUs | 0 = Beginner