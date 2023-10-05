#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    key_exist = key in a_dictionary
    if key_exist == False:
        return a_dictionary
    else:
        del a_dictionary[key]
        return a_dictionary
