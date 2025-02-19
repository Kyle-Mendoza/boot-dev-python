'''
    Complete the double_string function. It takes a string as input and returns a “doubled” version, including spaces!

    Example output

    sentence = "LF3M BRD full clear"
    print(double_string(sentence)) # "LLFF33MM  BBRRDD  ffuullll  cclleeaarr"
'''
def double_string(string):
    char_array_storage = []
    double_string = ""

    for char in string:
        char_array_storage.extend([char, char]) # NOTE: .append(value) is for single value while .extend([value1, value2]) for multiples 

    double_string = "".join(char_array_storage)
    return double_string