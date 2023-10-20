#!/usr/bin/python3
"""Module that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """Function that reads a text file (UTF8) and prints it to stdout
    """
    with open(filename) as file:
        print(file.read(), end="")
