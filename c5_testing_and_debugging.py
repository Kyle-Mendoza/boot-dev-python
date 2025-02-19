'''
    At Boot.dev, the Run button is for debugging. The Submit button mimics the idea of publishing your code for production use.

    You should be debugging your code using the Run button. You should be adding print() statements to your code to make sure it's doing what you think it's doing at different points in the code.

    Write a line to calculate a value
    print() the value you calculated
    Run the code
    Did it print what you expected? If not, fix it
    Repeat
    You will never lose XP or be penalized on Boot.dev for using the run button. However, there are consequences for submitting broken code, just like there are career consequences for pushing broken code to your users!

    Complete the take_magic_damage function. It should return the new health after calculating how much magic-type damage the player takes. Here is a description of the arguments:

    health: The player's starting health
    resist: The player's magic resistance. This reduces the damage they take by a static amount
    amp: The attacker's magic amplification. This increases the damage they deal by a multiplier
    spell_power: The base damage of the spell
    First, calculate the total maximum damage to be inflicted by multiplying the spell_power by the amp. Then, subtract the resist from the total damage to get the actual damage dealt. Apply that damage to the player's health and return the new health.

'''

def take_magic_damage(health, resist, amp, spell_power):
    # pass
    total_maximum_damage = spell_power * amp 
    actual_damage = total_maximum_damage - resist 
    new_health = health - actual_damage
    return new_health