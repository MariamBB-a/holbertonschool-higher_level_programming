#!/usr/bin/env python3
import pickle


class CustomObject:
    """
    Class representing a custom object that can be serialized using pickle.
    """

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object's attributes.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current object to a file.
        """
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except (FileNotFoundError, IOError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file and return it.
        """
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)
            return obj
        except (FileNotFoundError, IOError, pickle.PickleError):
            return None
