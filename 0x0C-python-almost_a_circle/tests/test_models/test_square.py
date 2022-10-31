# #!/usr/bin/python3
# """ This module contains test for Rectangle class """
# import unittest
# from models.base import Base
# from models.square import Square


# class TestRectangleClass(unittest.TestCase):
#     """ test case for rectangle class """

#     def setUp(self) -> None:
#         Base._Base__nb_objects = 0

#     def test_dimensions(self):
#         """ test that it assings the dimensions """
#         square = Square(10)
#         self.assertEqual(square.width, 10)
#         self.assertEqual(square.height, 10)

#     def test_coordinates(self):
#         """ test that it assings the coordinates """
#         square = Square(2, 1, 1)
#         self.assertEqual(square.x, 1)
#         self.assertEqual(square.y, 1)

#     def test_id(self):
#         """ test it imitates the behaviour of base class """
#         square = Square(78, 2, 3, 6)
#         self.assertEqual(square.id, 6)

#     def test_type_error(self):
#         """ test that it raises type error """
#         with self.assertRaises(TypeError):
#             Square("string")
#             Square(5, "string")
#             Square(5, 6, "string")

#     def test_value_error(self):
#         """ test that it raises value error """
#         with self.assertRaises(ValueError):
#             Square(0)
#             Square(4, -1)
#             Square(5, 2, -5)

#     def test_area(self):
#         """ test the area of the rectangle """
#         square1 = Square(10)
#         square2 = Square(5)
#         self.assertEqual(square1.area(), 100)
#         self.assertEqual(square2.area(), 25)

#     def test_incomplete_argument(self):
#         """ test that it raises argument error """
#         with self.assertRaises(TypeError):
#             Square()

#     def test_str(self):
#         """ test the str magic method """
#         square = Square(4, 2, 1, 12)
#         self.assertEqual(str(square), "[Square] (12) 2/1 - 4")

#     def test_size(self):
#         """ test the size property """
#         square = Square(5)
#         self.assertEqual(square.size, 5)
#         square.size = 10
#         self.assertEqual(square.size, 10)

#     def test_size_exception(self):
#         """ test that it raises exception for invalid size type """
#         with self.assertRaises(TypeError):
#             Square("8")

#     def test_args_update(self):
#         """ test update method """
#         square = Square(10, 10, 10, 10)
#         square.update(89)
#         self.assertEqual(str(square), "[Square] (89) 10/10 - 10")
#         square.update(89, 2)
#         self.assertEqual(str(square), "[Square] (89) 10/10 - 2")
#         square.update(89, 2, 3)
#         self.assertEqual(str(square), "[Square] (89) 3/10 - 2")
#         square.update(89, 2, 3, 4)
#         self.assertEqual(str(square), "[Square] (89) 3/4 - 2")

#     def test_kwargs_update(self):
#         """ test update mwthod with kwargs """
#         square = Square(10, 10, 10, 90)
#         square.update(size=1)
#         self.assertEqual(str(square), "[Square] (90) 10/10 - 1")
#         square.update(size=14, x=2)
#         self.assertEqual(str(square), "[Square] (90) 2/10 - 14")
#         square.update(y=1, x=3, id=91)
#         self.assertEqual(str(square), "[Square] (91) 3/1 - 14")
#         square.update(x=1, size=2, y=3)
#         self.assertEqual(str(square), "[Square] (91) 1/3 - 2")

#     def test_skip_kwargs(self):
#         """ test that it skips kwargs if args is present """

#         square = Square(10, 10, 10, 90)
#         square.update(30, size=1)
#         self.assertEqual(str(square), "[Square] (30) 10/10 - 10")
#         square.update(31, 6, size=14, x=2)
#         self.assertEqual(str(square), "[Square] (31) 10/10 - 6")
#         square.update(23, id=91)
#         self.assertEqual(str(square), "[Square] (23) 10/10 - 6")
#         square.update(76, 4, 5, x=1, size=2, y=3)
#         self.assertEqual(str(square), "[Square] (76) 5/10 - 4")

#     def test_to_dictionary(self):
#         """ test if the to_dictionary method works """

#         square = Square(10, 1, 9, 23)
#         square2 = Square(9)
#         square_dict = square.to_dictionary()
#         square.update(**square_dict)
#         self.assertEqual(square_dict,
#                          {'id': 23, 'x': 1, 'size': 10, 'y': 9})
#         self.assertIsInstance(square_dict, dict)
#         self.assertFalse(square == square2)

#     def test_load_from_file_csv_square(self):
#         """ test the method load_from_file """

#         s1 = Square(5)
#         s2 = Square(7, 9, 1)
#         list_squares_input = [s1, s2]
#         Square.save_to_file_csv(list_squares_input)
#         list_squares_output = Square.load_from_file_csv()
#         self.assertIsInstance(list_squares_output, list)
#         self.assertEqual(str(list_squares_output[0]),
#                          "[Square] (1) 0/0 - 5")
#         self.assertEqual(str(list_squares_output[1]),
#                          "[Square] (2) 9/1 - 7")

#     def test_load_from_file_square(self):
#         """ test the method load_from_file """

#         s1 = Square(5)
#         s2 = Square(7, 9, 1)
#         list_squares_input = [s1, s2]
#         Square.save_to_file(list_squares_input)
#         list_squares_output = Square.load_from_file()
#         self.assertIsInstance(list_squares_output, list)
#         self.assertEqual(str(list_squares_output[0]),
#                          "[Square] (1) 0/0 - 5")
#         self.assertEqual(str(list_squares_output[1]),
#                          "[Square] (2) 9/1 - 7")
#!/usr/bin/python3
""" Module for test Square class """
import unittest
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquareMethods(unittest.TestCase):
    """ Suite to test Square class """

    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0

    def test_new_square(self):
        """ Test new square """
        new = Square(3)
        self.assertEqual(new.size, 3)
        self.assertEqual(new.width, 3)
        self.assertEqual(new.height, 3)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)
        self.assertEqual(new.id, 1)

    def test_new_square_2(self):
        """ Test new square with all attrs """
        new = Square(2, 5, 5, 4)
        self.assertEqual(new.size, 2)
        self.assertEqual(new.width, 2)
        self.assertEqual(new.height, 2)
        self.assertEqual(new.x, 5)
        self.assertEqual(new.y, 5)
        self.assertEqual(new.id, 4)

    def test_new_squares(self):
        """ Test new squares """
        new = Square(1, 1)
        new2 = Square(1, 1)
        self.assertEqual(False, new is new2)
        self.assertEqual(False, new.id == new2.id)

    def test_is_Base_instance(self):
        """ Test Square is a Base instance """
        new = Square(1)
        self.assertEqual(True, isinstance(new, Base))

    def test_is_Rectangle_instance(self):
        """ Test Square is a Rectangle instance """
        new = Square(1)
        self.assertEqual(True, isinstance(new, Rectangle))

    def test_incorrect_amount_attrs(self):
        """ Test error raise with no args passed """
        with self.assertRaises(TypeError):
            new = Square()

    def test_incorrect_amount_attrs_1(self):
        """ Test error raised with no args passed """
        with self.assertRaises(TypeError):
            new = Square(1, 1, 1, 1, 1)

    def test_access_private_attrs(self):
        """ Trying to access to a private attribute """
        new = Square(1)
        with self.assertRaises(AttributeError):
            new.__width

    def test_access_private_attrs_2(self):
        """ Trying to access to a private attribute """
        new = Square(1)
        with self.assertRaises(AttributeError):
            new.__height

    def test_access_private_attrs_3(self):
        """ Trying to access to a private attribute """
        new = Square(1)
        with self.assertRaises(AttributeError):
            new.__x

    def test_access_private_attrs_4(self):
        """ Trying to access to a private attribute """
        new = Square(1)
        with self.assertRaises(AttributeError):
            new.__y

    def test_valide_attrs(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            new = Square("2", 2, 2, 2)

    def test_valide_attrs_2(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            new = Square(2, "2", 2, 2)

    def test_valide_attrs_3(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            new = Square(2, 2, "2", 2)

    def test_value_attrs(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            new = Square(0)

    def test_value_attrs_2(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            new = Square(1, -1)

    def test_value_attrs_3(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            new = Square(1, 1, -1)

    def test_area(self):
        """ Checking the return value of area method """
        new = Square(4)
        self.assertEqual(new.area(), 16)

    def test_load_from_file(self):
        """ Test load JSON file """
        load_file = Square.load_from_file()
        self.assertEqual(load_file, load_file)

    def test_area_2(self):
        """ Checking the return value of area method """
        new = Square(2)
        self.assertEqual(new.area(), 4)
        new.size = 5
        self.assertEqual(new.area(), 25)

    def test_display(self):
        """ Test string printed """
        r1 = Square(2)
        res = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_display_2(self):
        """ Test string printed """
        r1 = Square(4)
        res = "####\n####\n####\n####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

        r1.size = 5
        res = "#####\n#####\n#####\n#####\n#####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_str(self):
        """ Test __str__ return value """
        r1 = Square(4, 2, 2)
        res = "[Square] (1) 2/2 - 4\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_2(self):
        """ Test __str__ return value """
        r1 = Square(3, 2, 5, 3)
        res = "[Square] (3) 2/5 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        r1.id = 1
        r1.size = 11
        res = "[Square] (1) 2/5 - 11\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_3(self):
        """ Test __str__ return value """
        s1 = Square(5)
        res = "[Square] (1) 0/0 - 5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

        s2 = Square(3, 7, 1)
        res = "[Square] (2) 7/1 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s2)
            self.assertEqual(str_out.getvalue(), res)

        s3 = Square(1, 1, 1)
        res = "[Square] (3) 1/1 - 1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s3)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_4(self):
        """ Test __str__ return value """
        s1 = Square(3)
        res = "[Square] (1) 0/0 - 3"
        self.assertEqual(s1.__str__(), res)

    def test_display_3(self):
        """ Test string printed """
        s1 = Square(5, 2, 1)
        res = "\n  #####\n  #####\n  #####\n  #####\n  #####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            s1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_display_4(self):
        """ Test string printed """
        s1 = Square(3)
        res = "###\n###\n###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            s1.display()
            self.assertEqual(str_out.getvalue(), res)

        s1.x = 1
        res = " ###\n ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            s1.display()
            self.assertEqual(str_out.getvalue(), res)

        s1.y = 2
        res = "\n\n ###\n ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            s1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_update(self):
        """ Test update method """
        s1 = Square(3)
        res = "[Square] (1) 0/0 - 3\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

        s1.update(5)
        res = "[Square] (5) 0/0 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

    def test_update_2(self):
        """ Test update method """
        s1 = Square(3)
        res = "[Square] (1) 0/0 - 3\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

        s1.update(5)
        res = "[Square] (5) 0/0 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

    def test_update_3(self):
        """ Test update method """
        s1 = Square(1)
        res = "[Square] (1) 0/0 - 1\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

        s1.update(2, 2, 2, 2)
        res = "[Square] (2) 2/2 - 2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

        s1.update(y=3)
        res = "[Square] (2) 2/3 - 2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

        s1.update(id=1, size=10)
        res = "[Square] (1) 2/3 - 10\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

    def test_update_4(self):
        """ Test update method """
        s1 = Square(10)
        res = "[Square] (1) 0/0 - 10\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

        dic = {'size': 3, 'y': 5}
        s1.update(**dic)
        res = "[Square] (1) 0/5 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

    def test_update_5(self):
        """ Test update method """
        s1 = Square(7)
        res = "[Square] (1) 0/0 - 7\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

        dic = {'id': 10, 'x': '5', 'y': 5}

        with self.assertRaises(TypeError):
            s1.update(**dic)

    def test_to_dictionary(self):
        """ Test dictionary returned """
        s1 = Square(1, 2, 3)
        res = "[Square] (1) 2/3 - 1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.width, 1)
        self.assertEqual(s1.height, 1)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)
        self.assertEqual(s1.id, 1)

        res = "<class 'dict'>\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(s1.to_dictionary()))
            self.assertEqual(str_out.getvalue(), res)

    def test_to_dictionary_2(self):
        """ Test dictionary returned """
        s1 = Square(2, 2, 2)
        res = "[Square] (1) 2/2 - 2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

        s2 = Square(5)
        res = "[Square] (2) 0/0 - 5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s2)
            self.assertEqual(str_out.getvalue(), res)

        s1_dictionary = s1.to_dictionary()
        s2.update(**s1_dictionary)

        self.assertEqual(s1.width, s2.width)
        self.assertEqual(s1.height, s2.height)
        self.assertEqual(s1.x, s2.x)
        self.assertEqual(s1.y, s2.y)
        self.assertEqual(s1.id, s2.id)

        res = "<class 'dict'>\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(s1_dictionary))
            self.assertEqual(str_out.getvalue(), res)

    def test_dict_to_json(self):
        """ Test Dictionary to JSON string """
        s1 = Square(2)
        dictionary = s1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        res = "[{}]\n".format(dictionary.__str__())

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(json_dictionary)
            self.assertEqual(str_out.getvalue(), res.replace("'", "\""))

    def test_json_file(self):
        """ Test Dictionary to JSON string """
        s1 = Square(2)
        dictionary = s1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        res = "[{}]\n".format(dictionary.__str__())
        res = res.replace("'", "\"")

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(json_dictionary)
            self.assertEqual(str_out.getvalue(), res)

        Square.save_to_file([s1])
        res = "[{}]".format(dictionary.__str__())
        res = res.replace("'", "\"")

        with open("Square.json", "r") as file:
            res2 = file.read()

        self.assertEqual(res, res2)

    def test_value_square(self):
        """ Test value pased to Square """
        with self.assertRaises(ValueError):
            s1 = Square(-1)

    def test_create(self):
        """ Test create method """
        dictionary = {'id': 89}
        s1 = Square.create(**dictionary)
        self.assertEqual(s1.id, 89)

    def test_create_2(self):
        """ Test create method """
        dictionary = {'id': 89, 'size': 1}
        s1 = Square.create(**dictionary)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)

    def test_create_3(self):
        """ Test create method """
        dictionary = {'id': 89, 'size': 1, 'x': 2}
        s1 = Square.create(**dictionary)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)

    def test_create_4(self):
        """ Test create method """
        dictionary = {'id': 89, 'size': 1, 'x': 2, 'y': 3}
        s1 = Square.create(**dictionary)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)

    def test_load_from_file_2(self):
        """ Test load JSON file """
        s1 = Square(5)
        s2 = Square(8, 2, 5)

        linput = [s1, s2]
        Square.save_to_file(linput)
        loutput = Square.load_from_file()

        for i in range(len(linput)):
            self.assertEqual(linput[i].__str__(), loutput[i].__str__())
