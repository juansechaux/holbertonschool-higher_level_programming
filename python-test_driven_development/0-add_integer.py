#!/usr/bin/python3
"""
This is the "add" module.
The add module supplies one function, add_integer().  For example,
>>> add_integer(1, 2)
3
"""


def add_integer(a, b=98):
    """Returns an integer: the addition of a and b
    a and b must b integers or floats
    """

    if type(a) is int or type(a) is float:
        if type(b) is int or type(b) is float:
            return int(int(a) + int(b))
        else:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("a must be an integer")
