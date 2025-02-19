''' 
    Sets are like Lists, but they are unordered and they guarantee uniqueness. Only ONE of each value can be in a set.

    Complete the remove_duplicates function. It should take a list of spells that a player has learned and return a new List where there is at most one of each title. You can accomplish this in at least two ways:

    Iteration:

    Create a set to track spells that have been seen
    Create a list to store the unique spells
    Iterate over the list
    If the spell is not in the set, add it to the set and the list
    Return the list
    Set conversion:

    Convert the list to a set
    Convert the set back to a list and return it.
    It makes no sense to learn a spell twice! Once it's learned, it's learned forever.


'''
def remove_duplicates(spells):
    new_list = []
    spell_set = set(spells)   

    # for spell in spells: # FIRST VERSION ANSWER
    #     if spell not in spell_set:
    #         spell_set.add(spell)
    #         new_list.append(spell)

    for spell in spell_set:
        new_list.append(spell)

    return new_list