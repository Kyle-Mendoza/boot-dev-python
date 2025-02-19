'''
    Finish the check_ingredient_match function by looping over the recipe list. The function should calculate and return a percentage of ingredients the character has, as well as a list of missing from the recipe.

    For example, if these were the lists:

    recipe = ["Dragon Scale", "Unicorn Hair", "Phoenix Feather", "Troll Tusk"]
    ingredients = ["Dragon Scale", "Goblin Ear", "Phoenix Feather", "Troll Tusk"]

    percentage, missing_ingredients = check_ingredient_match(recipe, ingredients)
    print(percentage, missing_ingredients)
    # Prints: 75.00 ["Unicorn Hair"]
    Copy icon
    The percentage must be a float, not an integer!
'''
def check_ingredient_match(recipe, ingredients):
    percentage = 0 
    missing_ingredients = []
    correct_ingredient_count = 0

    for food in recipe: 
        if food in ingredients:
            correct_ingredient_count += 1
        else:
            missing_ingredients.append(food)

    percentage = (correct_ingredient_count / len(recipe)) * 100
    return percentage, missing_ingredients