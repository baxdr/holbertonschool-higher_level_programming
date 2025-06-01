#!/usr/bin/python3
"""
This module demonstrates the use of duck typing in Python.
"""
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract base class for shapes
    """
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
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius


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


def Shape_info(shape):
    """
    Function to print area and perimeter of a shape
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
