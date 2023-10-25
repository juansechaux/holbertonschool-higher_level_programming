#!/usr/bin/python3
""" Module that have the class Square"""

from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Magic method str,
        print the actual size of the square.
        """
        s = "[Square]"
        size = f"{self.x}/{self.y}"
        return f"{s} ({self.id}) {size} - {self.width}"

    def update(self, *args, **kwargs):
        """update the args of the class Square,
        1st argument should be the id attribute
        2nd argument should be the size attribute
        3th argument should be the x attribute
        4th argument should be the y attribute
        """
        names = ["id", "size", "x", "y"]
        if args is not () and args is not None:
            for value, name in zip(args, names):
                setattr(self, name, value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
