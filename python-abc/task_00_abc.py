#!/usr/bin/python3
""" 
This module demonstrates the use of Abstract Base Classes (ABC) in Python.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class for animals
    """
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """
    Concrete class for Dog that implements the Animal interface
    """

    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    Concrete class for Cat that implements the Animal interface
    """

    def sound(self):
        return "Meow"
