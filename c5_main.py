'''
    Complete the total_xp function. It accepts two integers as input:

    level
    xp_to_add
    There are 100 xp per level. total_xp should convert the current level to xp, then add this current xp to the xp_to_add argument and return the player's total xp. For example:

    If a player is level 1 and gains 100 xp, they have 200 total xp.
    If a player is level 2 and gains 250 xp, they have 450 total xp.
    If a player is level 170 and gains 590 xp, they have 17590 total xp.
    The pass keyword is a way to tell Python to do nothing. You'll need to replace it with your own code.
'''

def total_xp(level, xp_to_add):
    # pass
    xp_per_level = 100
    current_level_exp = level * xp_per_level
    total_xp = current_level_exp + xp_to_add
    return total_xp
    