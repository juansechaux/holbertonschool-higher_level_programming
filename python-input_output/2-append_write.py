#!/usr/bin/python3
"""Module that appends a string at the end of a text file (UTF8)
"""


def append_write(filename="", text=""):
    """Function that appends a string at the end of a text file (UTF8)
    (UTF8) and returns the number of characters written
    """
    with open(filename, mode="a", encoding="UTF8") as file:
        return file.write(text)
