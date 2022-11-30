"""
File: hashset.py
Project 11.6

Adjusts the array's capacity and rehahses if the load factor > .8 after creating
the HashSet.
"""

from node import Node
from arrays import Array
from abstractcollection import AbstractCollection
from abstractset import AbstractSet

class HashSet(AbstractCollection, AbstractSet):
    """Represents a hash-based set."""

    DEFAULT_CAPACITY = 9

    def __init__(self, sourceCollection = None,
                 capacity = None):
        # Now tracks occupied cells for rehashing if necessary.
        if capacity is None:
            self.capacity = HashSet.DEFAULT_CAPACITY
        else:
            self.capacity = capacity
        self.array = Array(self.capacity)
        self.foundNode = self.priorNode = None
        self.index = -1
        self.occupiedCells = 0
        AbstractCollection.__init__(self, sourceCollection)
        while self.loadFactor() > 0.8:
            self.rehash()

    # Accessor methods
    def __contains__(self, item):
        """Returns True if item is in self or False otherwise."""
        self.index = abs(hash(item)) % len(self.array)
        self.priorNode = None
        self.foundNode = self.array[self.index]
        while self.foundNode != None:
            if self.foundNode.data == item: 
                return True
            else:
                self.priorNode = self.foundNode
                self.foundNode = self.foundNode.next
        return False

    def __str__(self):
        """Returns the string representation of self."""
        return "{" + ", ".join(map(str, self)) + "}"

    def __iter__(self):
        """Supports iteration over a view of self."""
        for node in self.array:
            while node != None:
                yield node.data
                node = node.next

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.size = 0
        self.foundNode = self.priorNode = None
        self.index = -1
        self.occupiedCells = 0
        self.array = Array(HashSet.DEFAULT_CAPACITY)

    def add(self, item):
        """Adds item to self."""
        if not item in self:
            if not self.array[self.index]:
                self.occupiedCells += 1
            self.array[self.index] = Node(item,
                                            self.array[self.index])
            self.size += 1

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        if not item in self:
            raise KeyError(str(item) + " not in set")
        elif self.priorNode == None:
            self.array[self.index] = self.foundNode.next
            self.occupiedCells -= 1
        else:
            self.priorNode.next = self.foundNode.next
        self.size -= 1

    # Utility methods
    def loadFactor(self):
        return self.occupiedCells / len(self.array)

    def rehash(self):
        items = list(self)
        self.array = Array(len(self.array) * 2)
        self.size = 0
        self.occupiedCells = 0
        for item in items:
            self.add(item)

