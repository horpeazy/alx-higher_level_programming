#!/usr/bin/python3

def weight_average(my_list=[]):
    total = 0
    avg = 0

    for tul in my_list:
        total += tul[0] * tul[1]
        avg += tul[1]

    return total/avg


