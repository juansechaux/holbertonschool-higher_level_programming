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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for colum in range(0, self.__size):
                for rows in range(0, self.__size + 1):
                    if rows == self.__size:
                        print("#")
                    else:
                        print("#", end="")
