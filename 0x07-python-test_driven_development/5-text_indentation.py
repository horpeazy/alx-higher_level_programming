#!/usr/bin/python3

"""
    This module returns a function text_indentation
    that replaces certain characters with two new lines
"""
def text_indentation(text):
    """
        prints the text suplied as a parameter with the
        characters ",?:" replaced by two new lines

        Parameter:
        text(str): text to print out

        Return:
        None
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    
    for delim in ".?:":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])
    
    print("{}".format(text), end="")
