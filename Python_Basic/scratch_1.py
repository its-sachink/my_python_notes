# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def num_of_uniq_chars(string):
    string_list = []
    for char in string:
        if char not in string_list:
            string_list.insert(0, char)
    return string_list

def solution(S):
    # write your code in Python 3.6
    pass

    return max
