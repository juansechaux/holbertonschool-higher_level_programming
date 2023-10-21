#!/usr/bin/python3
"""Student to JSON"""


class Student:
    """lass Student that defines a student by:
    Public instance attributes: first_name, last_name, age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            result = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    result[key] = value

            return result

    def reload_from_json(self, json):
        """that replaces all attributes"""
        for name, value in json.items():
            setattr(self, name, value)
