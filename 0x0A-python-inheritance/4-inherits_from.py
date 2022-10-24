#!/usr/bin/python3

"""
    This modules supplies a function that checks if an
    object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class
"""


def inherits_from(obj, a_class):
    """
        Checks if an object is an instance of, or
        if the object is an instance of a class that
        inherited from, the specified class

        Args:
        obj(any): object to check
        a_class(any): class to check with

        Return:
        boolean: True or False
    """
    return isinstance(obj, a_class) and not type(obj) == a_class
