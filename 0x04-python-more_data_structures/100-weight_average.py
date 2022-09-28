#!/usr/bin/python3

from functools import reduce

def weight_average(my_list=[]):
    result = 0

    mul_ = [x * y for (x, y) in my_list]
    avg_l = [x[1] for x in my_list]

    total = reduce(lambda x, y: x + y, mul_)
    avg = reduce(lambda x, y: x + y, avg_l)

    return total/avg


