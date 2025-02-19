'''
    Complete the meditate function using a while loop. It takes mana, max_mana, energy and energy_drinks integers.

    While meditating, a character converts 1 energy into 1 mana for each iteration of the loop, up to the max_mana.
    If they have any energy_drinks when they run out of energy, they will drink 1 energy potion to gain 50 energy and continue meditating.
    A character will stop meditating if either:
    Their mana reaches the max_mana, or
    They run out of both energy and energy_drinks.
    Return the mana and remaining energy and energy_drinks when the character stops meditating.
'''

def meditate(mana, max_mana, energy, energy_drinks):
    total_mana = mana
    total_energy_drinks = energy_drinks
    exhausted = -1

    while energy != exhausted: # this must be set to -1
        no_drinks = total_energy_drinks == 0 # boolean conditions
        have_drinks = total_energy_drinks > 0
        mana_full = total_mana == max_mana
        no_energy = energy == 0

        if mana_full:
            break 
        elif no_energy:
            if have_drinks:
                energy += 50
                total_energy_drinks -= 1
                continue
            elif no_drinks: 
                break
        
        total_mana += 1
        energy -= 1

    return total_mana, energy, total_energy_drinks
