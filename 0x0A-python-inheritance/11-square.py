#!/usr/bin/python3

"""
    This module supplies a class Square
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """A Square class"""
    def __init__(self, size) -> None:
        """Initialize an instance"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """prints the area"""
        return self.__size ** 2

    def __str__(self) -> str:
        """string magic method"""
        return f"[Square] {self.__size}/{self.__size}"
