'''
    In the calculate_flurry_crit function, write a loop that calculates and returns the total_damage of the flurry as a critical hit.

    The function takes 2 inputs num_attacks, base_damage.

    Range over the num_attacks for the flurry
    Calculate the total damage for each attack within the flurry. Remember, each attack is a critical hit and does double the base_damage!
    The final swing of the flurry should do 4x the base_damage
    Return the total damage

'''

def calculate_flurry_crit(num_attacks, base_damage):
    total_damage = 0 
    last_attack = num_attacks - 1

    for attack in range(0, num_attacks):
        if attack == last_attack:
            total_damage += (base_damage * 4)
        else:
            total_damage += (base_damage * 2)

    return total_damage