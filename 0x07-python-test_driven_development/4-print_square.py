#!/usr/bin/python3

"""
    This module supplies a function  print_square
    that prints a square using #
"""


def print_square(size):
    """
        prints a square with the character #

        Parameter:
        size(int): the size of the square

        Return:
        None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(int(size)):
        for j in range(int(size)):
            print("#", end="")
        print()
