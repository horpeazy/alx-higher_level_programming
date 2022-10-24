#!/usr/bin/python3

"""
    This module supplies a class MyInt
"""

class MyInt(int):
    """Custome int class"""

    def __eq__(self, __x: object) -> bool:
        """rebel version of __eq__"""
        return not super().__eq__(__x)

    def __ne__(self, __x: object) -> bool:
        """rebel version of __ne__"""
        return not super().__ne__(__x)
