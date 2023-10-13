#!/usr/bin/python3
"""
This is the "add" module.
The add module supplies one function, add_integer().  For example,
>>> add_integer(1, 2)
3
"""


def matrix_divided(matrix, div):
    """Returns an integer: the addition of a and b
    a and b must b integers or floats
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
