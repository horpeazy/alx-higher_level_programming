#!/usr/bin/python3
"""
    This module supplies a function that performs I/O
"""


def read_file(filename=""):
    """Reads a file and prints it to stdout"""
    with open(filename, encoding="utf-8") as f:
        for line in f.readlines():
            print(line)
