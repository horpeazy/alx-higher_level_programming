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
    def __init__(self, size=0, position=(0, 0)) -> None:
        self.size = size
        self.position = position

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position to a value."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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

    def my_print(self):
        if self.size == 0:
            print()
            return
        for _ in range(0, self.position[1]):
            print()
        for _ in range(self.size):
            for _ in range(self.position[0]):
                print(" ", end="")
            for _ in range(self.size):
                print("#", end="")
            print()
        return
