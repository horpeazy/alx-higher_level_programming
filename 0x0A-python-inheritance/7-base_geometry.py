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
        if not isinstance(value):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
