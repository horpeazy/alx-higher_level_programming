# #!/usr/bin/python3
# """ This module contains test for the base Class"""
# import unittest
# from models.base import Base
# from models.rectangle import Rectangle


# class TestBaseClass(unittest.TestCase):
#     """ Test case for base class """

#     def setUp(self) -> None:
#         Base._Base__nb_objects = 0

#     def test_unique_id(self):
#         """
#             test that it skips incrementing num of instances
#             and assigns appropritae value
#         """
#         base = Base(20)

#         self.assertEqual(base.id, 20)

#     def test_multiple_instance(self):
#         """
#             test for the behaviour of the class when
#             multiple instances are created
#         """
#         base1 = Base()
#         base2 = Base()
#         base3 = Base(89)
#         base4 = Base()

#         self.assertEqual(base1.id, 1)
#         self.assertEqual(base2.id, 2)
#         self.assertEqual(base3.id, 89)
#         self.assertEqual(base4.id, 3)

#     def test_to_json_string(self):
#         """ test the to_json_string method """

#         r1 = Rectangle(10, 7, 2, 8, 45)
#         dictionary = r1.to_dictionary()
#         json_dictionary = Base.to_json_string([dictionary])
#         self.assertEqual(dictionary,
#                          {'x': 2, 'width': 10, 'id': 45, 'height': 7, 'y': 8})
#         self.assertIsInstance(dictionary, dict)
#         self.assertIsInstance(json_dictionary, str)

#     def test_from_json_string(self):
#         """ test the from_json_string method """

#         list_input = [
#             {'id': 89, 'width': 10, 'height': 4},
#             {'id': 7, 'width': 1, 'height': 7}
#         ]
#         json_list_input = Rectangle.to_json_string(list_input)
#         list_output = Rectangle.from_json_string(json_list_input)
#         self.assertIsInstance(list_input, list)
#         self.assertEqual(list_input,
#                          [{'height': 4, 'width': 10, 'id': 89},
#                           {'height': 7, 'width': 1, 'id': 7}])
#         self.assertIsInstance(json_list_input, str)
#         self.assertIsInstance(list_output, list)
#         self.assertEqual(list_output,
#                          [{'height': 4, 'width': 10, 'id': 89},
#                           {'height': 7, 'width': 1, 'id': 7}])

#     def test_create(self):
#         """ test create method """

#         rectangle = Rectangle(3, 5, 1, 6, 9)
#         rrectangle_dict = rectangle.to_dictionary()
#         rectangle2 = Rectangle.create(**rrectangle_dict)
#         self.assertEqual(str(rectangle), "[Rectangle] (9) 1/6 - 3/5")
#         self.assertEqual(str(rectangle2), "[Rectangle] (9) 1/6 - 3/5")
#         self.assertFalse(rectangle is rectangle2)
#         self.assertFalse(rectangle == rectangle2)
#!/usr/bin/python3
""" Module for test Base class """
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
import os


class TestBaseMethods(unittest.TestCase):
    """ Suite to test Base class """

    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0

    def test_id(self):
        """ Test assigned id """
        new = Base(1)
        self.assertEqual(new.id, 1)

    def test_id_default(self):
        """ Test default id """
        new = Base()
        self.assertEqual(new.id, 1)

    def test_id_nb_objects(self):
        """ Test nb object attribute """
        new = Base()
        new2 = Base()
        new3 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new2.id, 2)
        self.assertEqual(new3.id, 3)

    def test_id_mix(self):
        """ Test nb object attributes and assigned id """
        new = Base()
        new2 = Base(1024)
        new3 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new2.id, 1024)
        self.assertEqual(new3.id, 2)

    def test_string_id(self):
        """ Test string id """
        new = Base('1')
        self.assertEqual(new.id, '1')

    def test_more_args_id(self):
        """ Test passing more args to init method """
        with self.assertRaises(TypeError):
            new = Base(1, 1)

    def test_access_private_attrs(self):
        """ Test accessing to private attributes """
        new = Base()
        with self.assertRaises(AttributeError):
            new.__nb_objects

    def test_save_to_file_1(self):
        """ Test JSON file """
        Square.save_to_file(None)
        res = "[]\n"
        with open("Square.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)

        try:
            os.remove("Square.json")
        except:
            pass

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_2(self):
        """ Test JSON file """
        Rectangle.save_to_file(None)
        res = "[]\n"
        with open("Rectangle.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)
        try:
            os.remove("Rectangle.json")
        except:
            pass

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")
