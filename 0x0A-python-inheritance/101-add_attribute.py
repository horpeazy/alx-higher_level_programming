#!/usr/bin/python3

"""This modules supplies a function add_attribute"""


def add_attribute(obj, var, val):
    """
        Adds an attribute to an object if it is possible
        otherwise raise an exception
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, var, val)
    else:
        raise TypeError("can't add new attribute")
