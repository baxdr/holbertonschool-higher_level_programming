#!/usr/bin/python3
"""Defines a function that returns the JSON
 representation of an object (string)."""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    (list, dictionary, string, integer
    and boolean) for JSON serialization of an object.
    """
    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__
    return res
