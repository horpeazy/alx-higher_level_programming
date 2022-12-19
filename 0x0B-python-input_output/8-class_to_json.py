#!/usr/bin/python3
"""
    This module supplies a function that returns the
    dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for
    JSON serialization of an object
"""


def class_to_json(obj):
    """
        This function returns a dict representaion of
        an object
    """
    return obj.__dict__
