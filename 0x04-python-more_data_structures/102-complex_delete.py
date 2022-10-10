#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    keys = []
    for key_, value_ in a_dictionary.items():
        if value_ == value:
            keys.append(key_)

    for key in keys:
        del a_dictionary[key]
    return a_dictionary
