#!/usr/bin/python3
"""Defines a function that returns the JSON
 representation of an object (string)."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(json.dumps(my_obj))
