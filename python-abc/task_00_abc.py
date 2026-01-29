#!/usr/bin/python3
"""Abstract Animal Class and Subclasses using ABC"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for all animals"""

    @abstractmethod
    def sound(self):
        """Abstract method for making a sound"""
        pass


class Dog(Animal):
    """Dog class, subclass of Animal"""

    def sound(self):
        """Return the sound made by a dog"""
        return "Bark"


class Cat(Animal):
    """Cat class, subclass of Animal"""

    def sound(self):
        """Return the sound made by a cat"""
        return "Meow"
