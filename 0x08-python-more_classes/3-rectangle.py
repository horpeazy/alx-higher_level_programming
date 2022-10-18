#!/usr/bin/python3

"""This modules supplies a basic rectangle class"""


class Rectangle:
    """This ia basic representation of the rectangle class"""

    def __init__(self, width=0, height=0):
        """This is function is called when a class is created"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """gets the width of the rectangle"""
        return self.__width

    @property
    def height(self):
        """gets the height of the rectangle"""
        return self.__height

    @width.setter
    def width(self, width):
        """sets the width of the rectangle"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """sets the height of the rectangle"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """ returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        """returns a string representation of the rectangle"""
        str_ = ""
        if self.height == 0 or self.width == 0:
            return str_
        for _ in range(self.height):
            for _ in range(self.width):
                str_ += "#"
            str_ += "\n"

        return str_[:-1]
