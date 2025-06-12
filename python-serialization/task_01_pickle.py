#!/usr/bin/env python3
"""
task_01_pickle.py: Defines the CustomObject class with
Pickle-based serialization and deserialization methods.
Attributes:
    - name (str)
    - age (int)
    - is_student (bool)

Methods:
    - serialize(self, filename) -> bool | None
        Serialize the instance to a pickle file.
        Returns True on success, None on failure.
    - deserialize(cls, filename) -> CustomObject | None
        Class method to load and return an instance
        rom a pickle file. Returns instance on success, None on failure.
"""
import pickle


class CustomObject:
    """
    Represents a custom object with pickling support.

    Args:
        name (str): The name of the object.
        age (int): The age attribute.
        is_student (bool): Student status flag.
    """

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Print the object's attributes in the format:
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
            filename (str): Path to the output pickle file.

        Returns:
            bool: True on success, None on failure.
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
            filename (str): Path to the input pickle file.

        Returns:
            CustomObject: The loaded instance on success.
            None: If loading fails or the file is invalid.
        """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
            if isinstance(obj, cls):
                return obj
            return None
        except (OSError, pickle.PickleError):
            return None
