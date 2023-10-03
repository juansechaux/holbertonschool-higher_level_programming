#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    long = len(my_list) - 1
    while long >= 0:
        print("{:d}".format(my_list[long]))
        long = long - 1
