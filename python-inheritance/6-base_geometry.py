#!/usr/bin/python3
"""
Module to check if an object is exactly an instance of a specified class
"""


class BaseGeometry:
    """
    A class that defines a base geometry.
    """

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")
