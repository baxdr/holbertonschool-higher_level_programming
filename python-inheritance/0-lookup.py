#!/usr/bin/python3
"""
Module to return the list of available attributes and methods of an object
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object
    """
    return dir(obj)
