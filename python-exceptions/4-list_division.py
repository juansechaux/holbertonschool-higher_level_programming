#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    count = 0
    val = 0
    new_list = []
    for i in range(0, list_length):
        try:
            val = my_list_1[i] / my_list_2[i]
            new_list.append(val)
            count += 1
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
            continue
        except TypeError:
            print("wrong type")
            new_list.append(0)
            continue
        except IndexError:
            print("out of range")
            new_list.append(0)
            continue
    return (new_list)
