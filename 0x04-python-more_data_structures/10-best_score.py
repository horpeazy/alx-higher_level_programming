#!/usr/bin/python3

def best_score(a_dictionary):
    value_ = 0
    key_ = ""

    if not a_dictionary:
        return None

    for key, value in a_dictionary.items():
        if value >= value_:
            value_ = value
            key_ = key

    return key_
