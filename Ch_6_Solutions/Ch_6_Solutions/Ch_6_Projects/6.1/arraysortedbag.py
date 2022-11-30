"""
File: arraysortedbag.py
Project 6.1
Author: Ken Lambert

Adds __eq__ to ArraySortedBag, with O(n) running time.
"""

from arraybag import ArrayBag

class ArraySortedBag(ArrayBag):
    """An array-based sorted bag implementation."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        ArrayBag.__init__(self, sourceCollection)

    # Accessor methods
    def __contains__(self, item):
        left = 0
        right = len(self) - 1
        while left <= right:
            midPoint = (left + right) // 2
            if self.items[midPoint] == item:
                return True
            elif self.items[midPoint] > item:
                right = midPoint - 1
            else:
                left = midPoint + 1
        return False

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if self is other: return True
        if type(self) != type(other) or \
           len(self) != len(other):
            return False
        otherIter = iter(other)
        for item in self:
            if item != next(otherIter):
                return False
        return True

    # Mutator methods
    def add(self, item):
        """Adds item to self."""
        # Check array memory here and increase it if necessary
        if len(self) == len(self.items):
            temp = Array(2 * len(self))
            for i in range(len(self)):
                temp[i] = self.items[i]
            self.items = temp
        # Empty or last item, call ArrayBag.add
        if self.isEmpty() or item >= self.items[len(self) - 1]:
            ArrayBag.add(self, item)
        else:
            # Search for first item >= new item
            targetIndex = 0
            while item > self.items[targetIndex]:
                targetIndex += 1
            # Open a hole for new item
            for i in range(len(self), targetIndex, -1):
                self.items[i] = self.items[i - 1]
            # Insert item and update size
            self.items[targetIndex] = item
            self.size += 1
