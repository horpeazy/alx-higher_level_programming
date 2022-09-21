#!/usr/bin/python3

def uppercase(str):
    length = len(str)
    for i in range(0, length):
        if(i == length-1):
            _end = "\n"
        else:
            _end = ''
        if(ord(str[i]) >= 97 and ord(str[i]) <= 122):
            print(chr(ord(str[i]) - 32), end=_end)
        else:
            print(str[i], end=_end)
