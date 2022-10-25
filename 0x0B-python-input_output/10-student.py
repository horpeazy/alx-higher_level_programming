#!/usr/bin/python3
"""
    This module contains a class Student
"""


class Student:
    """A class representation of a student"""

    def __init__(self, first_name, last_name, age) -> None:
        """Initialize an instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dict representation of the class"""
        my_dict = self.__dict__
        if not attrs:
            return my_dict
        
        if type(attrs) == list:
            for att in attrs:
                my_dict.pop(att)
            return my_dict
