#!/usr/bin/python3
"""Pickling Custom Classes: CustomObject serialization/deserialization."""
import pickle


class CustomObject:
    """
    A custom object with attributes name, age, is_student,
    supporting pickle serialization and deserialization.
    """

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize this instance to a file using pickle.
        If an error occurs, return None.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except (OSError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an instance of CustomObject from a pickle file.
        Returns the instance, or None on failure.
        """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
            return obj
        except (OSError, pickle.PickleError):
            return None
