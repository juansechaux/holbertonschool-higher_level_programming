#!/usr/bin/python3
"""class Square that defines a square by: (based on 0-square.py)"""


class Square:
    """This class has private instance attribute: size"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int and type(value[1]) is not int:
            print("position must be a tuple of 2 positive integers", end="")
            raise TypeError
        if value[0] >= 0 and value[1] >= 0:
            self.__position = (value[0], value[1])
        else:
            print("position must be a tuple of 2 positive integers", end="")
            raise TypeError

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for jump in range(0, self.__position[1]):
                print("")
            for colum in range(0, self.__size):
                for space in range(0, self.__position[0]):
                    print(" ", end="")
                for rows in range(0, self.__size):
                    print("#", end="")
                print("")
