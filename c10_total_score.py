'''

'''

def merge(dict1, dict2):
    new_dict = {}
    for key1 in dict1: 

        for key2 in dict2: 
            if key1 not in new_dict and key2 not in new_dict: 
                new_dict[key1]  = dict1[key1]
                new_dict[key2] = dict2[key2]
            else:
                if key1 in new_dict and key2 not in new_dict:
                    new_dict[key2] = dict2[key2]
                elif key1 not in new_dict and key2 in new_dict:
                    new_dict[key1] = dict1[key1]
                

    return new_dict

def total_score(score_dict):
    total = 0
    for score_key in score_dict: 
        total += score_dict[score_key]

    return total