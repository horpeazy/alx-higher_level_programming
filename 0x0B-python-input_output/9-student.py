#!/usr/bin/python3
"""
    This module supplies a class
"""


class Student:
    """A class representation of a student"""

    def __init__(self, first_name, last_name, age) -> None:
        """Initialize an instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dict representation of the class"""
        return self.__dict__
