#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        empy = 0
        for i in matrix:
            long = len(i)
            cont = 1
            for c in i:
                if long == cont:
                    print("{:d}".format(c))
                    empy += 1
                else:
                    print("{:d} ".format(c), end=(""))
                    empy += 1
                cont += 1
        if empy == 0:
            print("{}".format(""))
