#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix:
        for array in matrix:
            for i in range(len(array)):
                if i == len(array) - 1:
                    print("{:d}".format(array[i]), end="")
                else:
                    print("{:d}".format(array[i]), end=" ")
            print()
