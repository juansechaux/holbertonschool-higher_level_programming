#!/usr/bin/python3
"""class Square that defines a square by: (based on 0-square.py)"""


class Square:
    """This class has private instance attribute: size"""
    def __init__(self, size=0, position=(0, 0)):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                print("size must be >= 0", end="")
                raise ValueError
        else:
            print("size must be an integer", end="")
            raise TypeError
        if len(position) <= 2:
            if isinstance(position[0], int) and isinstance(position[1], int):
                if position[0] >= 0 and position[1] >= 0:
                    self.__position = (position[0], position[1])
                else:
                    print("position must be a tuple of 2 positive integers")
                    raise TypeError
            else:
                print("position must be a tuple of 2 positive integers")
                raise TypeError
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if len(value) < 2:
            if isinstance(value[0], int) and isinstance(value[1], int):
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = (value[0], value[1])
                else:
                    print("position must be a tuple of 2 positive integers")
                    raise TypeError
            else:
                print("position must be a tuple of 2 positive integers")
                raise TypeError
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for colum in range(0, self.__size):
                for space in range(0, self.__position[0]):
                    print(" ", end="")
                for rows in range(0, self.__size):
                    print("#", end="")
                print("")
