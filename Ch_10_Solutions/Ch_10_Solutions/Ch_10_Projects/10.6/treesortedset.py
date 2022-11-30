"""
File: treesortedset.py

Project 10.6

A binary search tree-based implementation of a sorted set.
"""

from linkedbst import LinkedBST
from abstractbag import AbstractBag

class TreeSortedSet(AbstractBag):
    """A binary search tree-based implementation of a sorted set."""

    # Uses a LinkedBST to contain the set's items.
    # The tree is rebalanced after items are added during istantiation.
    # The iterator uses an inorder traversal to ensure visiting items
    # in ascending order.

    # eq is overridden for set-specific equality.

    # Searches, insertions, and removals are logarithmic on average,
    # and linear in the worst case.

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.items = LinkedBST()
        AbstractBag.__init__(self, sourceCollection)
        if not self.items.isBalanced():
            self.items.rebalance()

    # Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
        return self.items.inorder()

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if self is other: return True
        if type(self) != type(other) or \
           len(self) != len(other):
            return False
        for item in self:
            if not item in other:
                return False
        return True

 
    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.size = 0
        self.items.clear()

    def add(self, item):
        """Adds item to self."""
        if not item in self:
            self.items.add(item)
            self.size += 1

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        # Check precondition and raise if necessary
        if not item in self:
            raise KeyError(str(item) + " not in set")
        self.items.remove(item)
        self.size -= 1
        
