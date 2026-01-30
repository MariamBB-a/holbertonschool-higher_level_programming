#!/usr/bin/python3
"""VerboseList class that prints 
notifications on list modifications"""


class VerboseList(list):
    """A list subclass that prints messages when modified"""

    def append(self, item):
        """Append item and print a notification"""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend list with iterable and print a notification"""
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        """Remove item and print a notification"""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pop item at index and print a notification"""
        item = self[index]  # Get the item to pop
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
