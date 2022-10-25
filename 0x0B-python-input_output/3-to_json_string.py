#!/usr/bin/python3
"""
    This module supplies a function that
    serializes an object
"""
import json


def to_json_string(my_obj):
    """
        This function serializez an object

        Parameters:
        my_obj(any): object to serialize

        Return:
        JSON object
    """
    return json.loads(my_obj)
