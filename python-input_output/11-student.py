#!/usr/bin/python3
"""Defines Student class with serialization and deserialization methods."""


class Student:
    """Student that can be serialized to
      JSON-compatible dict and reloaded from one."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of the Student instance.

        If attrs is a list of strings, only
          include those attributes present in both
        the instance and the list. Otherwise, return all public attributes.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance based on json dict.

        json keys are attribute names and values are the new attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
