#!/usr/bin/python3

"""
    This modules supplies a function that checks if an
    object is an instance of another
"""


def is_same_class(obj, a_class):
    """
        Checks if an object is an instance of a class

        Args:
        obj(any): object to check
        a_class(any): class to check with

        Return:
        boolean: True or False
    """
    return type(obj) == a_class
