#!/usr/bin/python3
"""
This is the "3-say_my_name.py" module.
The 3-say_my_name.py module supplies one function, say_my_name().  For example,
>>> say_my_name("Walter", "White")
My name is Walter White
"""


def text_indentation(text):
    """ prints My name is <first name> <last name>
    first_name and last_name must be strings
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    esp_ch = ""
    for a_char in text:
        if esp_ch == "." or esp_ch == "?" or esp_ch == ":":
            if a_char == " ":
                continue
            else:
                esp_ch = ""
                print(a_char, end="")
                continue
        if a_char == "." or a_char == "?" or a_char == ":":
            print(a_char)
            print("")
            esp_ch = a_char
        else:
            print(a_char, end="")
