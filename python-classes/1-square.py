#!/usr/bin/python3
"""
This module defines a Square class with a private size attribute.
"""


class Square:
    """
    Represents a square with a private size attribute.

    Attributes:
        __size (int): The size of the square (private).
    """
    def __init__(self, size):
        """
        Initializes a new Square instance with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
