def get_item_counts(item):
    potion_count = 0 
    bread_count = 0 
    shortsword_count = 0

    for i in range(0, len(item)):
        if item[i].lower() == "potion":
            potion_count += 1 
        elif item[i].lower() == "bread":
            bread_count += 1
        elif item[i].lower() == "shortsword":
            shortsword_count += 1
        else:
            pass

    return potion_count, bread_count, shortsword_count