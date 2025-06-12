#!/usr/bin/python3
"""
Module that defines MyList class which extends the built-in list class.
Allows printing the list in sorted (ascending) order without modifying it.
"""


class MyList(list):
    """
    A class that inherits from list and adds a print_sorted method.
    """

    def print_sorted(self):
        """
        Prints the list sorted in ascending order without modifying the.
        """
        print(sorted(self))
