#!/usr/bin/python3
"""Module that appends a string at the end of a text file (UTF8)
"""
import json


def to_json_string(my_obj):
    """Function that appends a string at the end of a text file (UTF8)
    (UTF8) and returns the number of characters written
    """
    return json.dumps(my_obj)
