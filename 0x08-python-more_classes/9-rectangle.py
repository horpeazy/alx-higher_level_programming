#!/usr/bin/python3

"""This modules supplies a basic rectangle class"""


class Rectangle:
    """This ia basic representation of the rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """This is function is called when a class is created"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the bigger rectangle"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """ returns a new instance of Rectangles with size equal to size"""

        return Rectangle(size, size)

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
                str_ += str(self.print_symbol)
            str_ += "\n"

        return str_[:-1]

    def __repr__(self):
        """returns a formal representation of the rectangle"""

        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Executes when an instance is deleted"""

        if Rectangle.number_of_instances > 0:
            Rectangle.number_of_instances -= 1

        print("Bye rectangle...")
