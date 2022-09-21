#!/usr/bin/python3

def remove_char_at(str, n):
    _str = ""
    for i in range(len(str)):
        if i == n or -1 == n:
            continue
        _str = _str + str[i]

    return _str

