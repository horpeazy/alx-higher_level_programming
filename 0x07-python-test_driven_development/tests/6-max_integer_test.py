#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test case for max integer fucntion"""

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

    def test_none(self):
        self.assertRaises(TypeError, max_integer, None)

    def test_identical(self):
        self.assertEqual(max_integer([6,6,6,6,6]), 6)

    def test_float(self):
        l = [2, 4.5, 3]
        result = max_integer(l)
        self.assertEqual(result, 4.5)

if __name__ == "__main__":
    unittest.main()
