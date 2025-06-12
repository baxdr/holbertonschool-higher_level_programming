#!/usr/bin/python3
"""
Module to check if an object is exactly an instance of a specified class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class that defines a square, inheriting from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes the square with a given size.
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size ** 2
