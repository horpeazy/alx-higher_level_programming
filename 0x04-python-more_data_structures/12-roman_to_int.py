#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    result = 0
    for i in range(len(roman_string)):
        if roman_string[i] == "I":
            result += 1
        elif roman_string[i] == "V":
            if i != 0 and roman_string[i-1] == "I":
                result += 3
                continue
            result += 5
        elif roman_string[i] == "X":
            if i != 0 and roman_string[i-1] == "I":
                result += 8
                continue
            result += 10
        elif roman_string[i] == "L":
            if i != 0 and roman_string[i-1] == "X":
                result += 30
                continue
            result += 50
        elif roman_string[i] == "C":
            if i != 0 and roman_string[i-1] == "X":
                result += 80
                continue
            result += 100
        elif roman_string[i] == "D":
            if i != 0 and roman_string[i-1] == "C":
                result += 300
                continue
            result += 500
        elif roman_string[i] == "M":
            if i != 0 and roman_string[i-1] == "C":
                result += 800
                continue
            result += 1000

    return result
