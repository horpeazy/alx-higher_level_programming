#!/usr/bin/python3
"""
    This modules defines a python class Square
    that contains no attribute
"""


class Square:
    """
        This a class that represents a square

        Arguments:
            It takes no arguments
    """
    def __init__(self, size=0) -> None:
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
