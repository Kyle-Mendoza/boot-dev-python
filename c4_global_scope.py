'''
    Let's change how we are calculating our player's stats! The only thing we should need to define globally is the character level and then let our functions do the rest!

    Declare the variable player_level at the top of the global scope and set it to 4.
'''

player_level = 4 # correct answer
# ?

# Don't touch below this line


def calculate_health(modifier):
    global player_level # this is possible when using a global variable
    return player_level * modifier


def calculate_primary_stats(armor_bonus, modifier):
    return armor_bonus + modifier + player_level # but this is possible too
 

print(f"Character has {calculate_health(10)} max health.")

print(f"Character has {calculate_primary_stats(3, 8)} primary stats.")
