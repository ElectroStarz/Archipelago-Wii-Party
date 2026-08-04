class GameAddresses:
    current_map = 0x803388A3
    in_results = 0x807296B0 # Word

class MenuAddresses:
    button_unlock = 0x80337EA0 # Word

class PlayerAddresses:
    placement = 0x802319AB # Byte | If 4 player minigame type, 0 = 1st, else 1 = 1st

class CPUAddresses:
    skill = 0x80231D78 # Byte | For all CPUs | 0 = Beginner