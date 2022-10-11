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
    def position(self, position):
        if len(position) != 2 or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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
        for _ in range(self.size):
            if self.position[1] == 0:
                for _ in range(self.position[0]):
                    print(" ", end="")
            for _ in range(self.size):
                print("#", end="")
            print()
        return
