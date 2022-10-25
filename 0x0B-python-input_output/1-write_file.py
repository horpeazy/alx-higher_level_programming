#!/usr/bin/python3
"""
    This module supllies a function that writes
    to a file
"""


def write_file(filename="", text=""):
    """writes to a text file"""
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
