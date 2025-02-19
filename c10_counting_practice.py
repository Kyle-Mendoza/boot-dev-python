'''
    We need to be able to report to our players how many enemies are in their immediate vicinity - but they want the count of each enemy by its kind. Fix the count_enemies function. If you run the code, it will result in a KeyError. It takes a list of enemy_names as input. It should return a dictionary where the keys are all the enemy names from the list, and the values are the counts of how many times each enemy appeared in the list.
'''

def count_enemies(enemy_names):
    enemies_dict = {}

    for enemy_name in enemy_names:
        if enemy_name in enemies_dict:
            enemies_dict[enemy_name] = enemies_dict[enemy_name] + 1 # update when it already existed
        else:
            enemies_dict[enemy_name] = 1 # else create new with value of 1
        

    return enemies_dict
