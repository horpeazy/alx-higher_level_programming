#!/usr/bin/python3

"""
    This module supplies a class BaseGeometry
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle class"""
    def __init__(self, width, height) -> None:
        super().__init__()
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        return self.__width * self.__height

    def __str__(self) -> str:
        return (f"[Rectangle] {self.__width}/{self.__height}")
