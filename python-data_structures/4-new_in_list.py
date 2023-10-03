#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        new_list = list.copy(my_list)
        if len(my_list) <= idx or idx < 0:
            return new_list
        else:
            new_list[idx] = element
            return new_list
