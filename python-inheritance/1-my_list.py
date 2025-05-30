#!/usr/bin/python3
"""Defines class MyList that inherits from list"""


class MyList(list):
    """Custom list with a print_sorted method"""

    def print_sorted(self):
        """
        Print the list in ascending order without modifying the original list
        """
        print(sorted(self))
