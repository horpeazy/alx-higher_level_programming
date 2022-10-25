#!/usr/bin/python3
"""
    This function supplies a function that performs
    I/O
"""


def append_write(filename="", text=""):
    """Appends text to a file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
