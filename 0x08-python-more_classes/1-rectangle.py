#!/usr/bin/python3

"""This modules supplies a basic rectangle class"""

class Rectangle:
    def __init__(self, width=0, height=0):
        """This is basic rectangle class"""
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
