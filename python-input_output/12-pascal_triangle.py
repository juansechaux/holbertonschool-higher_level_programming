#!/usr/bin/python3
""" function def pascal_triangle(n):
    that returns a list of lists of integers
    representing the Pascals triangle of n
"""


def pascal_triangle(n):
    c_list = []
    if n <= 0:
        return c_list
    for colum in range(n):
        row_list = []
        if colum == 0:
            row_list.append(1)
        elif colum == 1:
            row_list.append(1)
            row_list.append(1)
        else:
            for row in range(colum + 1):
                if row == 0 or row == colum:
                    row_list.append(1)
                else:
                    item = c_list[colum - 1][row - 1] + c_list[colum - 1][row]
                    row_list.append(item)
        c_list.append(row_list)
    return c_list
