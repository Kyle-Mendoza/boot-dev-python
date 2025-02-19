'''
    Assignment
    Complete the print_status function.

    If player_health is 0, print the text dead to the console.
    Afterwards, whether or not the player is dead, print the text status check complete to the console.
    Tip
'''

def print_status(player_health):
    if player_health == 0:
        print(f"Player health reached {player_health}. Player is now DEAD")
    print("Status check complete.")

def test(health):
    print(f"Player health: {health}")
    print("Status checking...")
    print_status(health)
    print("===========================")

def main():
    test(0)
    test(5)
    test(3) 


main()