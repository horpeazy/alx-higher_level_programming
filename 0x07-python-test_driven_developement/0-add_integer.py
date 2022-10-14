#!/usr/bin/python3
"""
    This modules suplies a function add_integer that adds two integers and
    returns the result
"""

def add_integer(a, b=98):
    """
        The fucntions takes two integers a and b and returns the result of
        their addition.

        Parameters:
        a (int):  Integer to add
        b (int):  Integer to add (optional)

        Returns:
        int: Result of the addition of the two inputs
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b
