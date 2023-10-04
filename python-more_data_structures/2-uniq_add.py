#!/usr/bin/python3
def uniq_add(my_list=[]):
    cop_list = my_list.copy()
    sum_items = 0
    for item in my_list:
        if cop_list.count(item) > 1:
            cop_list.pop(cop_list.index(item))
        else:
            sum_items += item
    return sum_items
