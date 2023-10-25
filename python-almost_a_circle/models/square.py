#!/usr/bin/python3
""" Module that have the class Square"""

from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Magic method str,
        print the actual size of the square.
        """
        s = "[Square]"
        size = f"{self.x}/{self.y}"
        return f"{s} ({self.id}) {size} - {self.width}"
