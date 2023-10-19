#!/usr/bin/python3
"""Module based on 5-base_geometry.py
"""


class BaseGeometry:
    """class BaseGeometry
    """
    def area(self):
        """Is a Public instance method that raises
        an Exception with the message 'area() is not implemented'
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Is a Public instance method that validates value.
        if value is not an integer raise a TypeError.
        if value is not an integer raise a ValueError.
        """
        if type(value) is int:
            if value <= 0:
                raise ValueError(f"{name} must be greater than 0")
        else:
            raise TypeError(f"{name} must be an integer")


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
