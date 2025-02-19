'''
    The Fantasy Quest character system needs a list of "heroes" to be able to run the game properly. Someone wrote some pretty nasty code, and the code in question creates a heroes list where every 3rd index defines a new hero. First their name, then their age, then whether or not they're an "elf".

    Fix the structure of the heroes list by changing it into a list of tuples, where each tuple represents one hero and contains their data in the same order.
'''

def get_heroes():
    # pass
    heroes = [
        ("Glorfindel", 2093, True),
        ("Gandalf", 1054, False),
        ("Gimli", 389, False),
        ("Aragorn", 87, False)
    ]

    return heroes