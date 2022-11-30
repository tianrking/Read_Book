"""
File: arrayset.py
Project 6.5
Author: Ken Lambert
"""

from arraybag import ArrayBag

class ArraySet(ArrayBag):
    """An array-based set implementation."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        ArrayBag.__init__(self, sourceCollection)

    # Mutator methods
    def add(self, item):
        """Adds item to self."""
        if not item in self:
            ArrayBag.add(self, item)
