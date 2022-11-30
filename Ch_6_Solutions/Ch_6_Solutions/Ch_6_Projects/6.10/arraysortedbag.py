"""
File: arraysortedbag.py
Project 6.9
Author: Ken Lambert

Eliminates redundant search during remove.
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
                self.targetIndex = midPoint
                return True
            elif self.items[midPoint] > item:
                right = midPoint - 1
            else:
                left = midPoint + 1
        return False

    # Mutator methods
    def add(self, item):
        """Adds item to self."""
        # Check array memory here and increase it if necessary
        if len(self) == len(self.items):
            temp = Array(2 * len(self))
            for i in range(len(self)):
                temp[i] = self.items[i]
            self._items = temp
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
