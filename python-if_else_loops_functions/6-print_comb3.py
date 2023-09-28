#!/usr/bin/python3
d = 0
i = 1
while d < 9:
    if d == 8 and i == 9:
        print("{}{}".format(d, i))
        break
    elif i > d and i < 9:
        print("{}{}, ".format(d, i), end="")
        i = i + 1
    elif i == 9:
        print("{}{}, ".format(d, i), end="")
        i = 0
        d = d + 1
    else:
        i = i + 1
