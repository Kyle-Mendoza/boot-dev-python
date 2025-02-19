'''
    We need to filter the profanity out of our game’s live chat feature! Complete the filter_messages function. It takes a list of chat messages as input and returns 2 new lists:

    A list of the same messages but with all instances of the word dang removed.
    A list containing the number of dang words that were removed from the message at that particular index.
    Here are some examples:

    messages = ["dang it bobby!", "look at it go"]
    filter_messages(messages) # returns ["it bobby!", "look at it go"], [1, 0]

    messages2 = ["That's the bloody dang Reaper of Mars...", "Pax au Telemanus!", "I was never taught how to use a dang razor!"]
    filter_messages(messages2) # returns ["That's the bloody Reaper of Mars...", "Pax au Telemanus!", "I was never taught how to use a razor!"], [1, 0, 1]
    Copy icon
    Here are the steps for you to follow:

    Create the 2 empty lists that you’ll return at the end:
    One for the filtered messages. / 
    And one for counts of words removed. /
    For each message in the input list: 
    Split the message into a list of words using the .split() string method (see below for help). /
    Create a new empty list for all the non-bad words for this message. /
    Create a counter variable and set it to 0. We’ll increment this when we remove words from this message. /
    For each word in the message:
    If the word is dang, increment the counter /
    If it is not dang, add the word to the non-bad word list you created /
    Join the list of non-bad words into a single string using the .join() method (see below for help)
    Append the new clean message to the final list of filtered messages
    Append the count of bad words removed to its list
    Return the filtered messages first, then the counters
'''

def filter_messages(messages):
    filtered_messages = []
    total_removed_words_count = []

    for message in messages:
        words = message.split(" ")
        removed_words_count = 0
        non_bad_words = []

        for word in words:
            if word == "dang":
                del word
                removed_words_count += 1
            else: 
                non_bad_words.append(word)

        new_filtered_message = " ".join(non_bad_words)
        total_removed_words_count.append(removed_words_count)
        filtered_messages.append(new_filtered_message)
    
    return filtered_messages, total_removed_words_count
