'''
    Our players want a way to see their strongest attack from their last combat. Let's add another function to analyze data from our combat log.

    Complete the find_max function that looks at each number in the nums list and returns the maximum value. If no maximum is found, it just returns negative infinity. I've added it for you as the starting value of max_so_far.

    For example:

    max_val = find_max([100, 10, 22])
    print(max_val)
    # 100
'''
def find_max(nums):
    max_so_far = float("-inf")
    
    for number in nums:
        if number > max_so_far:
            max_so_far = number
        
    return max_so_far