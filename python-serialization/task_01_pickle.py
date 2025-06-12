#!/usr/bin/env python3
"""
task_01_pickle.py: Defines the CustomObject class with
pickle-based serialization and deserialization methods.

Attributes:
    name (str): The name of the object.
    age (int): The age attribute.
    is_student (bool): Student status flag.

Methods:
    serialize(self, filename):
        Serialize the instance to a pickle file.
        Returns True on success, None on failure.

    @classmethod deserialize(cls, filename):
        Load and return an instance from a pickle file.
        Returns the instance on success, None on failure.
"""
import pickle


class CustomObject:
    """
    A custom object that supports pickling.
    """

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Print the object's attributes:
        Name: <name>
        Age: <age>
        Is Student: <is_student>
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize this instance to the given file using pickle.

        Args:
            filename (str): Path to output pickle file.

        Returns:
            bool or None: True on success, None on failure.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
            return True
        except (OSError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize a CustomObject instance from the given pickle file.

        Args:
            filename (str): Path to input pickle file.

        Returns:
            CustomObject or None: Loaded instance on success, None on failure.
        """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
            return obj if isinstance(obj, cls) else None
        except (OSError, pickle.PickleError):
            return None
