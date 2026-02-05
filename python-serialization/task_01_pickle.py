#!/usr/bin/env python3
""" sterializing costumers list"""

class CustomObject:
    """Class representing a costumer"""
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
    """display customer info"""
        print(f"name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def sterialize(self, filename):
    """sterialize current obj and save in file"""
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    def destrialize(cls, filename):
    """destrialize obj from file"""
        with open(filename, 'rd') as f:
            return pickle.load(f)
