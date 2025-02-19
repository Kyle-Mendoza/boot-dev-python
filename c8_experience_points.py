'''
    Complete the calculate_experience_points function.

    The calculate_experience_points function takes a single parameter named level. Determine the total XP they have gained to reach the specified level from level 1 and return it.

'''

def calculate_experience_points(level):
    xp_to_next_level = 5 
    total_xp = 0 
    for i in range(0, level):
        total_xp += i * xp_to_next_level
    
    return total_xp