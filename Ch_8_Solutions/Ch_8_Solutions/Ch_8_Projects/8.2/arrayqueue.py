"""
File: arrayqueue.py
Project 8.2
"""

from arrays import Array
from abstractcollection import AbstractCollection

class ArrayQueue(AbstractCollection):
    """An array-based queue implementation."""

    # Class variable
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.front = self.rear = -1
        self.items = Array(ArrayQueue.DEFAULT_CAPACITY)
        AbstractCollection.__init__(self, sourceCollection)

    # Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = self.front
        while cursor != self.rear:
            yield self.items[cursor]
            if cursor == len(self.items) - 1:
                cursor = 0
            else:
                cursor += 1
        if cursor == self.rear and cursor != -1:
            yield self.items[cursor]

    def peek(self):
        """Returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if queue is empty."""
        if self.isEmpty():
            raise KeyError("Queue is empty")
        return self.items[self.front]

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.size = 0
        self.front = self.rear = -1
        self.items = Array(ArrayQueue.DEFAULT_CAPACITY)

    def add(self, item):
        """Inserts item at rear of the queue."""
        # Resize array if full
        if len(self) == len(self.items):
            tempArray = Array(len(self.items) * 2)
            i = 0
            for nextItem in self:
                tempArray[i] = nextItem
                i += 1
            self.items = tempArray
            if not self.isEmpty():
                self.front = 0
                self.rear = len(self) - 1
        if self.isEmpty():
            self.front = self.rear = 0
        elif self.rear == len(self.items) - 1:
            self.rear = 0
        else:
            self.rear += 1
        self.items[self.rear] = item
        self.size += 1

    def pop(self):
        """Removes and returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if queue is empty.
        Postcondition: the front item is removed from the queue."""
        if self.isEmpty():
            raise KeyError("Queue is empty")
        data = self.items[self.front]
        self.size -= 1
        if self.isEmpty(): self.front = self.rear = -1                  
        elif self.front == len(self.items) - 1:
            self.front = 0
        else:
            self.front += 1
        if len(self) <= .25 * len(self.items) and \
           ArrayQueue.DEFAULT_CAPACITY <= len(self.items) // 2:
            tempArray = Array(len(self.items) // 2)
            i = 0
            for item in self:
                tempArray[i] = item
                i += 1
            self.items = tempArray
            if not self.isEmpty():
                self.front = 0
                self.rear = len(self) - 1
        return data
        
         
