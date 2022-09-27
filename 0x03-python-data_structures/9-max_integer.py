#!/usr/bin/python3

def max_integer(my_list=[]):
    max_ = 0
    if len(my_list) == 0:
        return None
    for number in my_list:
        if number > max_:
            max_ = number
    return max_
