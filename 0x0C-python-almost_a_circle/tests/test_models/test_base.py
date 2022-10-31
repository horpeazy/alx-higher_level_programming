#!/usr/bin/python3
""" This module contains test for the base Class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBaseClass(unittest.TestCase):
    """ Test case for base class """

    def setUp(self) -> None:
        Base._Base__nb_objects = 0

    def test_unique_id(self):
        """
            test that it skips incrementing num of instances
            and assigns appropritae value
        """
        base = Base(20)

        self.assertEqual(base.id, 20)

    def test_multiple_instance(self):
        """
            test for the behaviour of the class when
            multiple instances are created
        """
        base1 = Base()
        base2 = Base()
        base3 = Base(89)
        base4 = Base()

        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 89)
        self.assertEqual(base4.id, 3)

    def test_to_json_string(self):
        """ test the to_json_string method """

        r1 = Rectangle(10, 7, 2, 8, 45)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(dictionary,
                         {'x': 2, 'width': 10, 'id': 45, 'height': 7, 'y': 8})
        self.assertIsInstance(dictionary, dict)
        self.assertIsInstance(json_dictionary, str)

    def test_from_json_string(self):
        """ test the from_json_string method """

        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertIsInstance(list_input, list)
        self.assertEqual(list_input,
                         [{'height': 4, 'width': 10, 'id': 89},
                          {'height': 7, 'width': 1, 'id': 7}])
        self.assertIsInstance(json_list_input, str)
        self.assertIsInstance(list_output, list)
        self.assertEqual(list_output,
                         [{'height': 4, 'width': 10, 'id': 89},
                          {'height': 7, 'width': 1, 'id': 7}])

    def test_create(self):
        """ test create method """

        rectangle = Rectangle(3, 5, 1, 6, 9)
        rrectangle_dict = rectangle.to_dictionary()
        rectangle2 = Rectangle.create(**rrectangle_dict)
        self.assertEqual(str(rectangle), "[Rectangle] (9) 1/6 - 3/5")
        self.assertEqual(str(rectangle2), "[Rectangle] (9) 1/6 - 3/5")
        self.assertFalse(rectangle is rectangle2)
        self.assertFalse(rectangle == rectangle2)
