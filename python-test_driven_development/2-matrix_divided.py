#!/usr/bin/python3
"""
This is the "matrix_divided" module.
The matrix_divided module supplies one function, matrix_divided().  For example,
>>> matrix_divided(matrix, 2)
new matrix
"""


def matrix_divided(matrix, div):
    """Returns a new matrix
    matrix must be a list of lists of integers or floats
    """
    error = "matrix must be a matrix (list of lists) of integers/floats"
    long = len(matrix[0])
    for list in matrix:
        if len(list) != long:
            raise TypeError("Each row of the matrix must have the same size")
        for i in range(0, len(list)):
            if type(list[i]) is int or type(list[i]) is float:
                continue
            else:
                raise TypeError(error)

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for list in matrix:
        new_row = []
        for i in range(0, len(list)):
            new_item = round(float(list[i] / div), 2)
            new_row.append(new_item)
        new_matrix.append(new_row)
    return new_matrix
