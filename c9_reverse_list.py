'''
    Assignment
    Some of our players would like to view their inventories in reverse order.

    Let's write a function that takes a list as an input and returns a new list except all the items are in reverse order.

    For example:

    [1, 2, 3] -> [3, 2, 1]
    ['a', 'b', 'c', 'd'] -> ['d', 'c', 'b', 'a']
'''
def reverse_array(items):
    # pass
    reverse_items = []
    array_length = len(items) - 1
    decrement = - 1
    
    for i in range(array_length, -1, decrement):
        reverse_items.append(items[i])

    return reverse_items