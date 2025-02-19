'''
    Fix the for loop in the count_down function. It takes start and end inputs, but start is always greater than end. It's supposed to print numbers counting down from start to end, exclusive, but there's a mistake in the range function call.

    range(start_inclusive, end_exclusive, step_optional)
'''
def count_down(start, end):
    if start > end:
        for i in range(start, end, -1):
            print(i)
    else: 
        print("Error can't count down if the end is greater than the start.")

def test(start, end):
    print(f"Using inputs start: {start} and end: {end}")
    print(f"Printing numbers from {start} to {end + 1}")
    count_down(start, end)
    print("=======================================")

def main():
    test(10, 0)
    test(20, 10)
    test(15, 11)
    test(10, 50) # this will not countdown

main()