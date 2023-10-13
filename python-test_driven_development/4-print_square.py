#!/usr/bin/python3
"""
This is the "3-say_my_name.py" module.
The 3-say_my_name.py module supplies one function, say_my_name().  For example,
>>> say_my_name("Walter", "White")
My name is Walter White
"""


def print_square(size):
    """ prints My name is <first name> <last name>
    first_name and last_name must be strings
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for column in range(size):
        for row in range(size):
            print("#", end="")
        print("")
