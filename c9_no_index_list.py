'''
    We need to check if a player has a specific item in their inventory. In the contains_leather_scraps function, use the no-index syntax to iterate over each item in items. If you find an item called Leather Scraps, set the found variable to True.
'''

def contains_leather_scraps(items):
    found = False 

    # dont touch above this line 
    for item in items: 
        has_leather_scraps = item == "Leather Scraps"
        if has_leather_scraps:
            found = True 

    # dont touch below this line
    return found