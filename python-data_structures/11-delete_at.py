#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    long = len(my_list) - 1
    if long < idx or idx < 0:
        return my_list
    else:
        del my_list[idx]
        return my_list
