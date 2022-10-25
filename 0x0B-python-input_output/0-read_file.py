#!/usr/bin/python3
"""
    This module supplies a function that performs I/O
"""

def read_file(filename="", encode="utf8"):
    """Reads a file and prints it to stdout"""
    with open(filename) as f:
        file_content = f.read()
        print(file_content)
