'''

what the most common enemy in a given area of the game map is.

Complete the get_most_common_enemy function by iterating over all enemies in the dictionary and returning only the name of the enemy with the highest count.

If there are no enemies, return None. If there are multiple enemies with the same highest count, return the first one found.

enemies_dict is a dictionary of name -> count. Example:

{
    "jackal": 1,
    "kobold": 2,
    "soldier": 3,
    "gremlin": 5
}
Copy icon
Tip: Negative Infinity
When you're trying to find a "max" value, it helps to keep track of the "max so far" in a variable and to start that variable at the lowest possible number, negative infinity.

max_so_far = float("-inf")
Copy icon
You'll also want to keep track of the enemy name associated with the maximum count. I would set the default for that variable to None.

'''

def get_most_common_enemy(enemies_dict):
    max_so_far = float("-inf")
    most_common_enemy = ""

    for enemy in enemies_dict:
        count = enemies_dict[enemy] 

        if count > max_so_far:
            max_so_far = count
            most_common_enemy = enemy
        
    return most_common_enemy if most_common_enemy != "" else None
