#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    long1 = len(tuple_a)
    long2 = len(tuple_b)

    if long1 == 0:
        tuple_a = (0, 0)
    if long2 == 0:
        tuple_b = (0, 0)
    if long1 < 2:
        if tuple_a[0] > 0:
            tuple_a = (tuple_a[0], 0)
        else:
            tuple_a = (0, tuple_a[1])
    if long2 < 2:
        if tuple_b[0] > 0:
            tuple_b = (tuple_b[0], 0)
        else:
            tuple_b = (0, tuple_b[1])
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
