#!/usr/bin/python3
""" This module contains test for Rectangle class """
import unittest

from pyautogui import size
from models.square import Square


class TestRectangleClass(unittest.TestCase):
    """ test case for rectangle class """

    def test_dimensions(self):
        """ test that it assings the dimensions """
        square = Square(10)
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)

    def test_coordinates(self):
        """ test that it assings the coordinates """
        square = Square(2, 1, 1)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 1)

    def test_id(self):
        """ test it imitates the behaviour of base class """
        square = Square(78, 2, 3, 6)
        self.assertEqual(square.id, 6)

    def test_type_error(self):
        """ test that it raises type error """
        with self.assertRaises(TypeError):
            Square("string")
            Square(5, "string")
            Square(5, 6,"string")

    def test_value_error(self):
        """ test that it raises value error """
        with self.assertRaises(ValueError):
            Square(0)
            Square(4, -1)
            Square(5, 2, -5)

    def test_area(self):
        """ test the area of the rectangle """
        square1 = Square(10)
        square2 = Square(5)
        self.assertEqual(square1.area(), 100)
        self.assertEqual(square2.area(), 25)

    def test_incomplete_argument(self):
        """ test that it raises argument error """
        with self.assertRaises(TypeError):
            Square()

    def test_str(self):
        """ test the str magic method """
        square = Square(4, 2, 1, 12)
        self.assertEqual(str(square), "[Square] (12) 2/1 - 4")

    def test_size(self):
        """ test the size property """
        square = Square(5)
        self.assertEqual(square.size, 5)
        square.size = 10
        self.assertEqual(square.size, 10)

    def test_size_exception(self):
        """ test that it raises exception for invalid size type """
        with self.assertRaises(TypeError):
            Square("8")

    def test_args_update(self):
        """ test update method """
        square = Square(10, 10, 10, 10)
        square.update(89)
        self.assertEqual(str(square), "[Square] (89) 10/10 - 10")
        square.update(89, 2)
        self.assertEqual(str(square), "[Square] (89) 10/10 - 2")
        square.update(89, 2, 3)
        self.assertEqual(str(square), "[Square] (89) 3/10 - 2")
        square.update(89, 2, 3, 4)
        self.assertEqual(str(square), "[Square] (89) 3/4 - 2")

    def test_kwargs_update(self):
        """ test update mwthod with kwargs """
        square = Square(10, 10, 10, 90)
        square.update(size=1)
        self.assertEqual(str(square), "[Square] (90) 10/10 - 1")
        square.update(size=14, x=2)
        self.assertEqual(str(square), "[Square] (90) 2/10 - 14")
        square.update(y=1, x=3, id=91)
        self.assertEqual(str(square), "[Square] (91) 3/1 - 14")
        square.update(x=1, size=2, y=3)
        self.assertEqual(str(square), "[Square] (91) 1/3 - 2")

    def test_skip_kwargs(self):
        """ test that it skips kwargs if args is present """

        square = Square(10, 10, 10, 90)
        square.update(30, size=1)
        self.assertEqual(str(square), "[Square] (30) 10/10 - 10")
        square.update(31, 6, size=14, x=2)
        self.assertEqual(str(square), "[Square] (31) 10/10 - 6")
        square.update(23, id=91)
        self.assertEqual(str(square), "[Square] (23) 10/10 - 6")
        square.update(76, 4, 5 ,x=1, size=2, y=3)
        self.assertEqual(str(square), "[Square] (76) 5/10 - 4")

    def test_to_dictionary(self):
        """ test if the to_dictionary method works """

        square = Square(10, 1, 9, 23)
        square2 = Square(9)
        square_dict = square.to_dictionary()
        square.update(**square_dict)
        self.assertEqual(square_dict, 
            {'id': 23, 'x': 1, 'size': 10, 'y': 9})
        self.assertIsInstance(square_dict, dict)
        self.assertFalse(square == square2)
