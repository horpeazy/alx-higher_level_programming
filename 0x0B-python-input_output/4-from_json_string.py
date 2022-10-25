#!/usr/bin/python3
"""
    This module supplies a function that
    deserializes a json object
"""
import json


def from_json_string(my_str):
    """
        This function deserializes an object

        Parameters:
        my_str(json string) - json string to deserialize

        Return:
        Python object
    """
    return json.loads(my_str)
