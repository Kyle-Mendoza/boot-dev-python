def get_max_health(modifier, level):
    return modifier * level


my_modifier = 5
my_level = 10

## don't touch above this line
# from this 
# max_health = get_max_health(modifier, level) -> this is wrong 
max_health = get_max_health(my_modifier, my_level)

# don't touch below this line

print(f"max_health is: {max_health}")
