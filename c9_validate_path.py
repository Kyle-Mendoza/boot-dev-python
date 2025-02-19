'''
    Complete the validate_path function. It should compare the expected sequence of waypoints with the actual sequence taken by a character and calculate how accurately the character followed the intended path.

    Inputs
    expected_path: A list of waypoints that define the correct path for the quest.
    character_path: A list where the first index is the name of the character, and the rest of the list consists of the waypoints they actually visited.
    character_path contains the same number of waypoints as expected_path.

    Output
    The function should return 2 values:

    character_name: a string
    percentage: a float
    Example
    expected_path = ["A", "B", "C", "D"]
    character_path = ["Hero123", "A", "C", "B", "D"]
    name, percent = validate_path(expected_path, character_path)
    print(name, percent)
    # prints: Hero123, 50.0
'''

def validate_path(expected_path, character_path):
    character_name = ""
    count_of_correct_path = 0

    character_name = character_path.pop(0)


    for i in range(0, len(expected_path)): 
        if expected_path[i] == character_path[i]:
            count_of_correct_path += 1
            
    percentage = (count_of_correct_path / len(expected_path)) * 100.0
    return character_name, percentage
