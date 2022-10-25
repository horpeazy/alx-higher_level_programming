#!/usr/bin/python3
"""
    This module supplies a function that makes
    an object from a json file
"""
import json


def load_from_json_file(filename):
    """
        This functions makes an object from input
        read from the file in the parameter

        Parameter:
        filename(str)- name of the file to read from

        Return:
        json object create
    """
    with open(filename) as f:
        file_content = f.read()
        return json.loads(file_content)
