#!/usr/bin/python3
"""Module that create class MyList that inherits from list
"""


class MyList(list):
    """Class that create class MyList that inherits from list
    """

    def print_sorted(self):
        """Function that prints the list, but sorted (ascending sort)
        """
        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)
