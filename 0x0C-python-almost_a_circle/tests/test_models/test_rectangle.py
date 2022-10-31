# #!/usr/bin/python3
# """ This module contains test for Rectangle class """
# import unittest
# from models.rectangle import Rectangle
# from models.base import Base


# class TestRectangleClass(unittest.TestCase):
#     """ test case for rectangle class """

#     def setUp(self) -> None:
#         Base._Base__nb_objects = 0

#     def test_dimensions(self):
#         """ test that it assings the dimensions """
#         rectangle = Rectangle(10, 3)
#         self.assertEqual(rectangle.width, 10)
#         self.assertEqual(rectangle.height, 3)

#     def test_coordinates(self):
#         """ test that it assings the coordinates """
#         rectangle = Rectangle(2, 3, 1, 1)
#         self.assertEqual(rectangle.x, 1)
#         self.assertEqual(rectangle.y, 1)

#     def test_id(self):
#         """ test it imitates the behaviour of base class """
#         rectangle3 = Rectangle(5, 78, 2, 3, 6)
#         self.assertEqual(rectangle3.id, 6)

#     def test_type_error(self):
#         """ test that it raises type error """
#         with self.assertRaises(TypeError):
#             Rectangle("string", 0)
#             Rectangle(5, "string")
#             Rectangle(5, 6, "string")
#             Rectangle(5, 6, 4, "string")

#     def test_value_error(self):
#         """ test that it raises value error """
#         with self.assertRaises(ValueError):
#             Rectangle(0, 6)
#             Rectangle(4, 0)
#             Rectangle(4, 8, -1)
#             Rectangle(5, 7, 2, -5)

#     def test_area(self):
#         """ test the area of the rectangle """
#         rectangle1 = Rectangle(10, 2)
#         rectangle2 = Rectangle(5, 7)
#         self.assertEqual(rectangle1.area(), 20)
#         self.assertEqual(rectangle2.area(), 35)

#     def test_incomplete_argument(self):
#         """ test that it raises argument error """
#         with self.assertRaises(TypeError):
#             Rectangle(4)
#             Rectangle()

#     def test_str(self):
#         """ test the str magic method """
#         rectangle1 = Rectangle(4, 6, 2, 1, 12)
#         self.assertEqual(str(rectangle1), "[Rectangle] (12) 2/1 - 4/6")

#     def test_args_update(self):
#         """ test update method """
#         rectangle = Rectangle(10, 10, 10, 10)
#         rectangle.update(89)
#         self.assertEqual(str(rectangle), "[Rectangle] (89) 10/10 - 10/10")
#         rectangle.update(89, 2)
#         self.assertEqual(str(rectangle), "[Rectangle] (89) 10/10 - 2/10")
#         rectangle.update(89, 2, 3)
#         self.assertEqual(str(rectangle), "[Rectangle] (89) 10/10 - 2/3")
#         rectangle.update(89, 2, 3, 4)
#         self.assertEqual(str(rectangle), "[Rectangle] (89) 4/10 - 2/3")
#         rectangle.update(89, 2, 3, 4, 5)
#         self.assertEqual(str(rectangle), "[Rectangle] (89) 4/5 - 2/3")

#     def test_kwargs_update(self):
#         """ test update mwthod with kwargs """
#         rectangle = Rectangle(10, 10, 10, 10, 90)
#         rectangle.update(height=1)
#         self.assertEqual(str(rectangle), "[Rectangle] (90) 10/10 - 10/1")
#         rectangle.update(width=1, x=2)
#         self.assertEqual(str(rectangle), "[Rectangle] (90) 2/10 - 1/1")
#         rectangle.update(y=1, width=2, x=3, id=91)
#         self.assertEqual(str(rectangle), "[Rectangle] (91) 3/1 - 2/1")
#         rectangle.update(x=1, height=2, y=3, width=4)
#         self.assertEqual(str(rectangle), "[Rectangle] (91) 1/3 - 4/2")

#     def test_skip_kwargs(self):
#         """ test that it skips kwargs if args is present """

#         rectangle = Rectangle(10, 10, 10, 10)
#         rectangle.update(30, id=1)
#         self.assertEqual(str(rectangle), "[Rectangle] (30) 10/10 - 10/10")
#         rectangle.update(31, 6, height=14, x=2)
#         self.assertEqual(str(rectangle), "[Rectangle] (31) 10/10 - 6/10")
#         rectangle.update(23, id=91)
#         self.assertEqual(str(rectangle), "[Rectangle] (23) 10/10 - 6/10")
#         rectangle.update(76, 4, 5, x=1, width=2, y=3)
#         self.assertEqual(str(rectangle), "[Rectangle] (76) 10/10 - 4/5")

#     def test_to_dictionary(self):
#         """ test if the to_dictionary method works """

#         rectangle = Rectangle(10, 2, 1, 9, 50)
#         rectangle2 = Rectangle(1, 1, 4, 6, 20)
#         rectangle_dict = rectangle.to_dictionary()
#         rectangle2.update(**rectangle_dict)
#         self.assertEqual(rectangle_dict,
#                          {'x': 1, 'y': 9, 'id': 50, 'height': 2, 'width': 10})
#         self.assertIsInstance(rectangle_dict, dict)
#         self.assertFalse(rectangle == rectangle2)

#     def test_load_from_file_rectangle(self):
#         """ test the method load_from_file """

#         r1 = Rectangle(10, 7, 2, 8)
#         r2 = Rectangle(2, 4)
#         list_rectangles_input = [r1, r2]
#         Rectangle.save_to_file(list_rectangles_input)
#         list_rectangles_output = Rectangle.load_from_file()
#         self.assertIsInstance(list_rectangles_output, list)
#         self.assertEqual(str(list_rectangles_output[0]),
#                          "[Rectangle] (1) 2/8 - 10/7")
#         self.assertEqual(str(list_rectangles_output[1]),
#                          "[Rectangle] (2) 0/0 - 2/4")

#     def test_load_from_file_csv_rectangle(self):
#         """ test the method load_from_file """

#         r1 = Rectangle(10, 7, 2, 8)
#         r2 = Rectangle(2, 4)
#         list_rectangles_input = [r1, r2]
#         Rectangle.save_to_file_csv(list_rectangles_input)
#         list_rectangles_output = Rectangle.load_from_file_csv()
#         self.assertIsInstance(list_rectangles_output, list)
#         self.assertEqual(str(list_rectangles_output[0]),
#                          "[Rectangle] (1) 2/8 - 10/7")
#         self.assertEqual(str(list_rectangles_output[1]),
#                          "[Rectangle] (2) 0/0 - 2/4")
#!/usr/bin/python3
""" Module for test Rectangle class """
import unittest
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleMethods(unittest.TestCase):
    """ Suite to test Rectangle class """

    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0

    def test_new_rectangle(self):
        """ Test new rectangle """
        new = Rectangle(1, 1)
        self.assertEqual(new.width, 1)
        self.assertEqual(new.height, 1)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)
        self.assertEqual(new.id, 1)

    def test_new_rectangle_2(self):
        """ Test new rectangle with all attrs """
        new = Rectangle(2, 3, 5, 5, 4)
        self.assertEqual(new.width, 2)
        self.assertEqual(new.height, 3)
        self.assertEqual(new.x, 5)
        self.assertEqual(new.y, 5)
        self.assertEqual(new.id, 4)

    def test_new_rectangles(self):
        """ Test new rectangles """
        new = Rectangle(1, 1)
        new2 = Rectangle(1, 1)
        self.assertEqual(False, new is new2)
        self.assertEqual(False, new.id == new2.id)

    def test_is_Base_instance(self):
        """ Test Rectangle is a Base instance """
        new = Rectangle(1, 1)
        self.assertEqual(True, isinstance(new, Base))

    def test_incorrect_amount_attrs(self):
        """ Test error raise with 1 arg passed """
        with self.assertRaises(TypeError):
            new = Rectangle(1)

    def test_incorrect_amount_attrs_1(self):
        """ Test error raised with no args passed """
        with self.assertRaises(TypeError):
            new = Rectangle()

    def test_access_private_attrs(self):
        """ Trying to access to a private attribute """
        new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            new.__width

    def test_access_private_attrs_2(self):
        """ Trying to access to a private attribute """
        new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            new.__height

    def test_access_private_attrs_3(self):
        """ Trying to access to a private attribute """
        new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            new.__x

    def test_access_private_attrs_4(self):
        """ Trying to access to a private attribute """
        new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            new.__y

    def test_valide_attrs(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            new = Rectangle("2", 2, 2, 2, 2)

    def test_valide_attrs_2(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            new = Rectangle(2, "2", 2, 2, 2)

    def test_valide_attrs_3(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            new = Rectangle(2, 2, "2", 2, 2)

    def test_valide_attrs_4(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            new = Rectangle(2, 2, 2, "2", 2)

    def test_value_attrs(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            new = Rectangle(0, 1)

    def test_value_attrs_1(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            new = Rectangle(1, 0)

    def test_value_attrs_2(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            new = Rectangle(1, 1, -1)

    def test_value_attrs_3(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            new = Rectangle(1, 1, 1, -1)

    def test_area(self):
        """ Checking the return value of area method """
        new = Rectangle(4, 5)
        self.assertEqual(new.area(), 20)

    def test_area_2(self):
        """ Checking the return value of area method """
        new = Rectangle(2, 2)
        self.assertEqual(new.area(), 4)
        new.width = 5
        self.assertEqual(new.area(), 10)
        new.height = 5
        self.assertEqual(new.area(), 25)

    def test_area_3(self):
        """ Checking the return value of area method """
        new = Rectangle(3, 8)
        self.assertEqual(new.area(), 24)
        new2 = Rectangle(10, 10)
        self.assertEqual(new2.area(), 100)

    def test_display(self):
        """ Test string printed """
        r1 = Rectangle(2, 5)
        res = "##\n##\n##\n##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_display_2(self):
        """ Test string printed """
        r1 = Rectangle(2, 2)
        res = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

        r1.width = 5
        res = "#####\n#####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_str(self):
        """ Test __str__ return value """
        r1 = Rectangle(2, 5, 2, 4)
        res = "[Rectangle] (1) 2/4 - 2/5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_2(self):
        """ Test __str__ return value """
        r1 = Rectangle(3, 2, 8, 8, 10)
        res = "[Rectangle] (10) 8/8 - 3/2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        r1.id = 1
        r1.width = 7
        r1.height = 15
        res = "[Rectangle] (1) 8/8 - 7/15\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_3(self):
        """ Test __str__ return value """
        r1 = Rectangle(5, 10)
        res = "[Rectangle] (1) 0/0 - 5/10\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        r2 = Rectangle(25, 86, 4, 7)
        res = "[Rectangle] (2) 4/7 - 25/86\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r2)
            self.assertEqual(str_out.getvalue(), res)

        r3 = Rectangle(1, 1, 1, 1)
        res = "[Rectangle] (3) 1/1 - 1/1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r3)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_4(self):
        """ Test __str__ return value """
        r1 = Rectangle(3, 3)
        res = "[Rectangle] (1) 0/0 - 3/3"
        self.assertEqual(r1.__str__(), res)

    def test_display_3(self):
        """ Test string printed """
        r1 = Rectangle(5, 4, 1, 1)
        res = "\n #####\n #####\n #####\n #####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_display_4(self):
        """ Test string printed """
        r1 = Rectangle(3, 2)
        res = "###\n###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

        r1.x = 4
        res = "    ###\n    ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

        r1.y = 2
        res = "\n\n    ###\n    ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_to_dictionary(self):
        """ Test dictionary returned """
        r1 = Rectangle(1, 2, 3, 4, 1)
        res = "[Rectangle] (1) 3/4 - 1/2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, 1)

        res = "<class 'dict'>\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(r1.to_dictionary()))
            self.assertEqual(str_out.getvalue(), res)

    def test_to_dictionary_2(self):
        """ Test dictionary returned """
        r1 = Rectangle(2, 2, 2, 2)
        res = "[Rectangle] (1) 2/2 - 2/2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        r2 = Rectangle(5, 7)
        res = "[Rectangle] (2) 0/0 - 5/7\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r2)
            self.assertEqual(str_out.getvalue(), res)

        r1_dictionary = r1.to_dictionary()
        r2.update(**r1_dictionary)

        self.assertEqual(r1.width, r2.width)
        self.assertEqual(r1.height, r2.height)
        self.assertEqual(r1.x, r2.x)
        self.assertEqual(r1.y, r2.y)
        self.assertEqual(r1.id, r2.id)

        res = "<class 'dict'>\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(r1_dictionary))
            self.assertEqual(str_out.getvalue(), res)

    def test_dict_to_json(self):
        """ Test Dictionary to JSON string """
        r1 = Rectangle(2, 2)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        res = "[{}]\n".format(dictionary.__str__())

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(json_dictionary)
            self.assertEqual(str_out.getvalue(), res.replace("'", "\""))

    def test_check_value(self):
        """ Test args passed """
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 2)

    def test_check_value_2(self):
        """ Test args passed """
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, -2)

    def test_create(self):
        """ Test create method """
        dictionary = {'id': 89}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)

    def test_create_2(self):
        """ Test create method """
        dictionary = {'id': 89, 'width': 1}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)

    def test_create_3(self):
        """ Test create method """
        dictionary = {'id': 89, 'width': 1, 'height': 2}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

    def test_create_4(self):
        """ Test create method """
        dictionary = {'id': 89, 'width': 1, 'height': 2, 'x': 3}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)

    def test_create_5(self):
        """ Test create method """
        dictionary = {'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    def test_load_from_file(self):
        """ Test load JSON file """
        load_file = Rectangle.load_from_file()
        self.assertEqual(load_file, [])

    def test_load_from_file_2(self):
        """ Test load JSON file """
        r1 = Rectangle(5, 5)
        r2 = Rectangle(8, 2, 5, 5)

        linput = [r1, r2]
        Rectangle.save_to_file(linput)
        loutput = Rectangle.load_from_file()

        for i in range(len(linput)):
            self.assertEqual(linput[i].__str__(), loutput[i].__str__())
