#!/usr/bin/python3
"""
This is the "3-say_my_name.py" module.
The 3-say_my_name.py module supplies one function, say_my_name().  For example,
>>> say_my_name("Walter", "White")
My name is Walter White
"""


def say_my_name(first_name, last_name=""):
    """ prints My name is <first name> <last name>
    first_name and last_name must be strings
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
