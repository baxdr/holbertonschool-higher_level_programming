#!/usr/bin/python3
"""
Module to check if an object is exactly an instance of a specified class
"""


def is_kind_of_class(obj, a_classs):
    """
    Returns True if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class,
    otherwise returns False
    """
    return isinstance(obj, a_classs)
