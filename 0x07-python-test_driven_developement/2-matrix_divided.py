#!/usr/bin/python3
"""
    This modules suplies a function matrix_divided that loops through a
    matrix, divides it by div and returns the result
"""

def matrix_divided(matrix, div):
    """
        The functions takes a matrix and an integer as input and returns a
        new matrix that is a result of dividing the elements of the input
        matrix by the integer. It raises errors when the matrix contains 
        worng value types or is of an inappropiate length, it also raises
        an error when the div supplied is not an integer or is equal to zero

        Parameters:
        matrix (list):  a list of lists
        div (int): inetger to divide matrix by 

        Returns:
        list: a new matrix
    """
    len_ = len(matrix)

    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        for num in row:
            if type(num) != int and type(num) != float:
                raise TypeError("matrix must be a matrix (list of lists)" +
                                " of integers/floats")

    for row in matrix:
        if len(row) != len_:
            raise TypeError("Each row of the matrix must have the same size")

    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]

    return new_matrix
