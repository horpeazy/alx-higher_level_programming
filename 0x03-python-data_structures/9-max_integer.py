#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_ = my_list[0]
    for number in my_list:
        if number > max_:
            max_ = number
    return max_
