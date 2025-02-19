'''
    Assignement

    In Fantasy Quest, players can go to a town's local pub. Drinking virtual beer refills their stamina!

    Complete the function that determines if a bartender should serve drinks to a customer. Only return True if all of these conditions apply. If any of these conditions are False, return False:

    The customer's age is 21 or older
    The bartender is working
    The time is at least 5 but no later than 10
'''

def should_serve_customer(customer_age, on_break, time):
    # pass
    if (customer_age >= 21 and not on_break and time >= 5 and time <= 10):
        return True 
    return False