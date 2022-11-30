"""
File: treesortedset.py
Project 11.8

A tree-based sorted set implementation.
"""

from linkedbst import LinkedBST
from abstractset import AbstractSet

class TreeSortedSet(AbstractSet):
    """An tree-based sorted set implementation."""

    def __init__(self, sourceCollection = None):
        self.items = LinkedBST()
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    # Accessor methods
    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        return self.items.isEmpty()
    
    def __len__(self):
        """-Returns the number of items in self."""
        return len(self.items)

    def __str__(self):
        """Returns the string representation of self."""
        return " {" + ", ".join(map(str, self)) + "}"

    def __iter__(self):
        """Supports iteration over a view of self."""
        return self.items.inorder()

    def __add__(self, other):
        """Returns a new set containing the contents
        of self and other."""
        result = type(self)(self)
        for item in self:
            result.add(item)
        return result

    def __contains__(self, item):
        """Returns True if item is in the set or
        False otherwise."""
        return item in self.items

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.items.clear()

    def add(self, item):
       """Adds item to the set if it is not in the set."""
       if not item in self:
           self.items.add(item)

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        postcondition: item is removed from self."""
        self.items.remove(item)
