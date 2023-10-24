#!/usr/bin/python3
""" Module that have the class Base
"""


class Base:
    """Class Base, private class attribute __nb_objects = 0
        if id is not None, assign the public instance
        attribute id with this argument value
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
