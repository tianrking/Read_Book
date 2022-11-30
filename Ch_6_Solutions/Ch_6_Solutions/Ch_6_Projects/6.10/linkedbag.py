"""
File: linkedbag.py
Project 6.10
Author: Ken Lambert

Eliminates redundant search during remove.
"""

from node import Node
from abstractbag import AbstractBag

class LinkedBag(AbstractBag):
    """A link-based bag implementation."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.items = None
        self.probe = self.trailer = None
        AbstractBag.__init__(self, sourceCollection)

    # Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = self.items
        while not cursor is None:
            yield cursor.data
            cursor = cursor.next

    def __contains__(self, item):
        """Returns True if item is in self or False otherwise."""
        self.probe = self.items
        self.trailer = None
        for targetItem in self:
            if item == targetItem: return True
            self.trailer = self.probe
            self.probe = self.probe.next
        return False

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.size = 0
        self.probe = self.trailer = None
        self.items = None

    def add(self, item):
        """Adds item to self."""
        self.items = Node(item, self.items)
        self.size += 1
        
    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        postcondition: item is removed from self."""
        # Check precondition and raise if necessary
        if not item in self:
            raise KeyError(str(item) + " not in bag")
        # Search for the node containing the target item was done in
        # method __contains__
        # self._probe will point to the target node, and self._trailer
        # will point to the one before it, if it exists
        # Unhook the node to be deleted, either the first one or one
        # thereafter
        if self.probe == self.items:
            self.items = self.items.next
        else:
            self.trailer.next = self.probe.next
        # Decrement logical size
        self.size -= 1
        
        
