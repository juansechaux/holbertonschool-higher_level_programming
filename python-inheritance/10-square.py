#!/usr/bin/python3
"""Module based on 9-rectangle.py
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square
    """
    def __init__(self, size):
        """Instantiation with size
        size must be private. No getter or setter
        size must be positive integers,
        validated by integer_validator
        """
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """Magic method str,
        print the actual size of the rectangle.
        """
        return f'[Rectangle] {self.__size}/{self.__size}'

    def area(self):
        """Instantiation area of the rectangle size * size.
        """
        return self.__size * self.__size
