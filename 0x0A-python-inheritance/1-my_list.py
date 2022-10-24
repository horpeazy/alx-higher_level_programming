#!/usr/bin/python3

"""
    This module supplies a class MyList that inherits for the
    list class
"""


class MyList(list):
    """
        A custom class that inherits from the python class
    """
    def __init_subclass__(cls) -> None:
        """Initialize the class with parent attr and methods"""
        return super().__init_subclass__()

    def print_sorted(self):
        """prints the elements in reversed sorted order"""
        print(sorted(self))
