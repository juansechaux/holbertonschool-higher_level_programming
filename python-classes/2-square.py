#!/usr/bin/python3
"""class Square that defines a square by: (based on 0-square.py)"""


class Square:
    """This class has private instance attribute: size"""
    def __init__(self, size=0):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                print("size must be >= 0", end="")
                raise ValueError
        else:
            print("size must be an integer", end="")
            raise TypeError

