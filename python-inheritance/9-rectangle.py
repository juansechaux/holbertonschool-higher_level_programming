#!/usr/bin/python3
"""Module based on 7-base_geometry.py
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle
    """
    def __init__(self, width, height):
        """Instantiation with width and height
        width and height must be private. No getter or setter
        width and height must be positive integers,
        validated by integer_validator
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Magic method str,
        print the actual width and height of the rectangle.
        """
        return f'[Rectangle] {self.__width}/{self.__height}'

    def area(self):
        """Instantiation area of the rectangle with the
        width and height.
        """
        return self.__width * self.__height
