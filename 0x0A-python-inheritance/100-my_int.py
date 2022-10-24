#!/usr/bin/python3

"""
    This module supplies a class MyInt
"""

class MyInt(int):

    def __eq__(self, __x: object) -> bool:
        return self != __x

    def __ne__(self, __x: object) -> bool:
        return not self.__eq__(__x)
