def sum_of_odd_numbers(end):
    total = 0
    for i in range(0, end):
        if i%2 == 1: #meaning if i divide the current number to 2 and it gives me remainder of 1
            total += i # i will add it to the total

    return total
