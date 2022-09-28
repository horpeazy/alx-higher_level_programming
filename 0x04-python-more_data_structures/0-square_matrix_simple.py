#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    return [list(map(lambda x: x**2, list_)) for list_ in matrix]
