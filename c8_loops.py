'''
    Assignment
    Complete the missing sections of the for-loop in the print_numbers function so that it prints the numbers 0-99 to the console.
'''

def print_numbers():
    for i in range(0, 100): 
        print(i)

# don't edit below this lin

def test():
    print("Printing numbers from 0 to 99: ")
    print_numbers()
    print("================================")

def main():
    test()

main()