#!/usr/bin/python3

"""
    This module supplies a class BaseGeometry
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """A Square class"""
    def __init__(self, size) -> None:
        super.__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        return self.__size ** 2
