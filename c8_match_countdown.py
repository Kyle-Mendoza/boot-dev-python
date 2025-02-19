'''
    In the countdown_to_start function, write a loop that counts down from 10 to 1. At each iteration, print the number with an ellipsis:

    i...

    However, when i is 1, it should print 1...Fight! instead.

    Do not use the ellipsis (…) character. Use three periods (...) instead.
'''

def countdown_to_start():
    step_condition = -1 # -1 meaning it will countdown, if 1 and it will count count up

    for i in range(10, 0, step_condition):
        if i == 1:
            print(f"{i}...Fight")
            break # after reaching this it will break the loop
        print(i)
        

# Don't edit below this line 

def test():
    print("Counting down to match start: ")
    countdown_to_start()
    print("==============================")

def main():
    test()

main()