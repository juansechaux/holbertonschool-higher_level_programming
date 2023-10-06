#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(0, x):
            print("{}".format(my_list[i]), end="")
    except IndexError:
        return (my_list[i - 1])
    else:
        return (my_list[i])
    finally:
        print("")
