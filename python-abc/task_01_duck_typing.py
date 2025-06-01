#!/usr/bin/python3
"""
This module demonstrates the use of duck typing in Python.
"""
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """
    Abstract base class for shapes
    """

    def __init__(self):
        """
        Initialize the shape.
        """
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
    Concrete class for Circle that implements the Shape interface
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        pi = math.pi
        return pi * (self.radius ** 2)

    def perimeter(self):
        pi = math.pi
        return 2 * pi * self.radius


class Rectangle(Shape):
    """
    Concrete class for Rectangle that implements the Shape interface
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Function to print area and perimeter of a shape
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
