'''
    Complete the purchase_item function. If the character doesn't have enough gold raise an exception with the text not enough gold. Don't handle the exception.

    Otherwise, return the amount of money the customer has leftover after completing the purchase.
'''
def purchase_item(items, gold_available):

    if gold_available >= items: 
        return gold_available - items
    else:
        raise Exception("not enough gold")
