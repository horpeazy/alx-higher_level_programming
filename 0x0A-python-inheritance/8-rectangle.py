#!/usr/bin/python3

"""
    This module supplies a class BaseGeometry
"""


class BaseGeometry:
    """An bare bones base geometry class"""

    def area(self):
        """raise an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A rectangle class"""
    def __init__(self, width, height) -> None:
        super().__init__()
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
        self.__width = width
        self.__height = height
