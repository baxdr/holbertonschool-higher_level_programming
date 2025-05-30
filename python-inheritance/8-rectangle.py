#!/usr/bin/python3
"""
Module to check if an object is exactly an instance of a specified class
"""


class Rectangle(BaseGeometry):
    """
    A class that defines a rectangle, inheriting from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes the rectangle with width and height.
        Raises TypeError if width or height is not an integer,
        and ValueError if width or height is <= 0.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
