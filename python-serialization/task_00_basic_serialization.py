#!/usr/bin/python3
"""Basic serialization and deserialization module."""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to JSON and save it to a file.

    - data: Python dict to serialize.
    - filename: target JSON file path; existing file will be overwritten.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load JSON from a file and return the corresponding Python dictionary.

    - filename: path to the JSON file to read.
    - Returns: Python dict with deserialized data.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
