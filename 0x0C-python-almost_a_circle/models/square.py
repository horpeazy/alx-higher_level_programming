#!/usr/bin/python3
"""
This module supplies a class Square
that inherits from Rectangle
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """
        Square Class

        Private instance attributes:
            size(int): size of the rectangle
            x(int): padding in x-direction
            y(int): padding in y-direction
    """

    def __init__(self, size, x=0, y=0, id=None) -> None:
        """ initialize a new instance of the class """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ getter for y """
        return self.width

    @size.setter
    def size(self, size):
        """ setter for size """
        if type(size) != int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ update the attributes """
        if args:
            for index, arg in enumerate(args):
                if index == 0:
                    self.id = arg
                elif index == 1:
                    self.size = arg
                elif index == 2:
                    self.x = arg
                elif index == 3:
                    self.y = arg
                else:
                    pass
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ return dictionary representation of class """
        my_dict = {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

        return my_dict

    def __str__(self) -> str:
        """ string representation of the square class """

        return "[{}] ({}) {}/{} - {}".\
                format(self.__class__.__name__, self.id, self.x, self.y, self.width)