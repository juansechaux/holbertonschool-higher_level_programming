#!/usr/bin/python3
def element_at(my_list, idx):
    long = len(my_list)
    if long < idx or idx < 0:
        return (None)
    else:
        return (my_list[idx])
