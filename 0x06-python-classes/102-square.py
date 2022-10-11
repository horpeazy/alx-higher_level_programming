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
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        return self.__size ** 2

    def __eq__(self, other):
        if not isinstance(other, Square):
            raise Exception("{} is not an instance of {}".format(other, self))

        return self.size == other.size

    def __lt__(self, other):
        if not isinstance(other, Square):
            raise Exception("{} is not an instance of {}".format(other, self))

        return self.size < other.size

    def __gt__(self, other):
        if not isinstance(other, Square):
            raise Exception("{} is not an instance of {}".format(other, self))

        return self.size > other.size

    def __le__(self, other):
        if not isinstance(other, Square):
            raise Exception("{} is not an instance of {}".format(other, self))

        return self.size <= other.size

    def __ge__(self, other):
        if not isinstance(other, Square):
            raise Exception("{} is not an instance of {}".format(other, self))

        return self.size >= other.size
