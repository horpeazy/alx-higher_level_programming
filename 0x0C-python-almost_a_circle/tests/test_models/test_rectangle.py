#!/usr/bin/python3
""" This module contains test for Rectangle class """
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleClass(unittest.TestCase):
    """ test case for rectangle class """

    def setUp(self) -> None:
        Base._Base__nb_objects = 0

    def test_dimensions(self):
        """ test that it assings the dimensions """
        rectangle = Rectangle(10, 3)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 3)

    def test_coordinates(self):
        """ test that it assings the coordinates """
        rectangle = Rectangle(2, 3, 1, 1)
        self.assertEqual(rectangle.x, 1)
        self.assertEqual(rectangle.y, 1)

    def test_id(self):
        """ test it imitates the behaviour of base class """
        rectangle3 = Rectangle(5, 78, 2, 3, 6)
        self.assertEqual(rectangle3.id, 6)

    def test_type_error(self):
        """ test that it raises type error """
        with self.assertRaises(TypeError):
            Rectangle("string", 0)
            Rectangle(5, "string")
            Rectangle(5, 6, "string")
            Rectangle(5, 6, 4, "string")

    def test_value_error(self):
        """ test that it raises value error """
        with self.assertRaises(ValueError):
            Rectangle(0, 6)
            Rectangle(4, 0)
            Rectangle(4, 8, -1)
            Rectangle(5, 7, 2, -5)

    def test_area(self):
        """ test the area of the rectangle """
        rectangle1 = Rectangle(10, 2)
        rectangle2 = Rectangle(5, 7)
        self.assertEqual(rectangle1.area(), 20)
        self.assertEqual(rectangle2.area(), 35)

    def test_incomplete_argument(self):
        """ test that it raises argument error """
        with self.assertRaises(TypeError):
            Rectangle(4)
            Rectangle()

    def test_str(self):
        """ test the str magic method """
        rectangle1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(rectangle1), "[Rectangle] (12) 2/1 - 4/6")

    def test_args_update(self):
        """ test update method """
        rectangle = Rectangle(10, 10, 10, 10)
        rectangle.update(89)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 10/10 - 10/10")
        rectangle.update(89, 2)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 10/10 - 2/10")
        rectangle.update(89, 2, 3)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 10/10 - 2/3")
        rectangle.update(89, 2, 3, 4)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 4/10 - 2/3")
        rectangle.update(89, 2, 3, 4, 5)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 4/5 - 2/3")

    def test_kwargs_update(self):
        """ test update mwthod with kwargs """
        rectangle = Rectangle(10, 10, 10, 10, 90)
        rectangle.update(height=1)
        self.assertEqual(str(rectangle), "[Rectangle] (90) 10/10 - 10/1")
        rectangle.update(width=1, x=2)
        self.assertEqual(str(rectangle), "[Rectangle] (90) 2/10 - 1/1")
        rectangle.update(y=1, width=2, x=3, id=91)
        self.assertEqual(str(rectangle), "[Rectangle] (91) 3/1 - 2/1")
        rectangle.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(rectangle), "[Rectangle] (91) 1/3 - 4/2")

    def test_skip_kwargs(self):
        """ test that it skips kwargs if args is present """

        rectangle = Rectangle(10, 10, 10, 10)
        rectangle.update(30, id=1)
        self.assertEqual(str(rectangle), "[Rectangle] (30) 10/10 - 10/10")
        rectangle.update(31, 6, height=14, x=2)
        self.assertEqual(str(rectangle), "[Rectangle] (31) 10/10 - 6/10")
        rectangle.update(23, id=91)
        self.assertEqual(str(rectangle), "[Rectangle] (23) 10/10 - 6/10")
        rectangle.update(76, 4, 5, x=1, width=2, y=3)
        self.assertEqual(str(rectangle), "[Rectangle] (76) 10/10 - 4/5")

    def test_to_dictionary(self):
        """ test if the to_dictionary method works """

        rectangle = Rectangle(10, 2, 1, 9, 50)
        rectangle2 = Rectangle(1, 1, 4, 6, 20)
        rectangle_dict = rectangle.to_dictionary()
        rectangle2.update(**rectangle_dict)
        self.assertEqual(rectangle_dict,
                         {'x': 1, 'y': 9, 'id': 50, 'height': 2, 'width': 10})
        self.assertIsInstance(rectangle_dict, dict)
        self.assertFalse(rectangle == rectangle2)

    def test_load_from_file_rectangle(self):
        """ test the method load_from_file """

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertIsInstance(list_rectangles_output, list)
        self.assertEqual(str(list_rectangles_output[0]),
                         "[Rectangle] (1) 2/8 - 10/7")
        self.assertEqual(str(list_rectangles_output[1]),
                         "[Rectangle] (2) 0/0 - 2/4")

    def test_load_from_file_csv_rectangle(self):
        """ test the method load_from_file """

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertIsInstance(list_rectangles_output, list)
        self.assertEqual(str(list_rectangles_output[0]),
                         "[Rectangle] (1) 2/8 - 10/7")
        self.assertEqual(str(list_rectangles_output[1]),
                         "[Rectangle] (2) 0/0 - 2/4")
