#!/usr/bin/python3
""" Module that have the class Base
"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """public method, that returns a list of
        a dictionary representation.
        """
        new_dict = "[]"
        if list_dictionaries is None or list_dictionaries is ():
            return new_dict
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """function that writes an Object to a text file,
        using a JSON representation.
        """
        list_of_dict = []
        class_name = cls.__name__ + ".json"
        if list_of_dict is not None:
            for obj in list_objs:
                list_of_dict.append(obj.to_dictionary())
        with open(class_name, mode="w+", encoding="utf-8") as file:
            file.write(cls.to_json_string(list_of_dict))
