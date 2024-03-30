#!/usr/bin/python3
"""
Module for MyList class that inherits from list.
"""


class MyList(list):
    """
    A class that inherits from list and provides additional methods.
    """

    def print_sorted(self):
        """
        Prints the list in sorted order (ascending).
        """
        sorted_list = sorted(self)
        print(sorted_list)
