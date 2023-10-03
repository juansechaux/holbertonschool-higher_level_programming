#!/usr/bin/python3
def max_integer(my_list=[]):
    long = len(my_list)
    if long == 0:
        return "None"
    else:
        my_list.sort()
        return my_list[long - 1]
