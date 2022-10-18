#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_regular(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_not_int(self):
        self.assertRaises(TypeError, max_integer, [3, None, 8, 3])
        self.assertRaises(TypeError, max_integer, [1, 3, "hope", 8])

    def test_not_list(self):
        self.assertRaises(TypeError, max_integer, 8)

    def test_string(self):
        self.assertEqual(max_integer(["alx", "holberton"]), "holberton")

if __name__ == "__main__":
    unittest.main()