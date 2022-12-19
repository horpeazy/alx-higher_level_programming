#!/usr/bin/python3
"""
    This module supplies a function pascal triangle
"""


def pascal_triangle(n):
    """This function builds a pascal triangle"""
    if n == 0:
        return []
    if n == 1:
        return [[1]]

    prev_res = pascal_triangle(n-1)
    prev_arr = prev_res[-1]
    new_arr = [1]

    for i in range(1, len(prev_arr)):
        new_arr.append(prev_arr[i] + prev_arr[i - 1])
    new_arr.append(1)
    prev_res.append(new_arr)

    return prev_res
