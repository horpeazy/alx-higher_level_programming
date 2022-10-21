#!/usr/bin/python3

"""
    This module supplies a function say_my_name
    that prints the name to the stdout
"""

def say_my_name(first_name, last_name=""):
    """
        prints the first and last name from the arguments

        Parameters:
        first_name(str): first name
        last_name(str): last name

        Return:
        None
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))