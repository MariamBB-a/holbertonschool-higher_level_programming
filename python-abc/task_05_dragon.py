#!/usr/bin/python3
"""Mixins example: SwimMixin, FlyMixin, and Dragon"""


class SwimMixin:
    """Provides swimming capability"""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Provides flying capability"""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon that can both swim and fly"""

    def roar(self):
        print("The dragon roars!")
