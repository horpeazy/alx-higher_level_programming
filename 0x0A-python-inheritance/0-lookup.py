#!/usr/bin/python3

"""
    This module supllies a function lookup that
    returns a list of the attributes and methods
    present in an object passed to iy
"""


def lookup(obj):
    """
        Finds and return all the list and attributes
        in obj

        Args:
        obj(object): object to lookup

        Return:
        list - a list of the attributes and methods
    """
    if not obj:
        raise TypeError("argument must be a valid object")
    res = dir(obj)
    return list(res)
