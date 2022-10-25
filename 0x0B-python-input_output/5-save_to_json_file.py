#!/usr/bin/python3
"""
    This module supplies a function that writes an object
    to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """writes a json object to a file"""
    with open(filename, 'w') as f:
        text = json.dumps(my_obj)
        f.write(text)
