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
