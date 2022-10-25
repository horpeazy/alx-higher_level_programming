#!/usr/bin/python3
"""
    This module supplies a function that performs I/O
"""


def read_file(filename=""):
    """Reads a file and prints it to stdout"""
    with open(filename, 'r', encode="utf8") as f:
        file_content = f.read()
        print(file_content)
