"""
File: arraylistiterator.py
Author: Ken Lambert
"""

class ArrayListIterator(object):
    """Represents the list iterator for an array list."""

    def __init__(self, backingStore):
        self.backingStore = backingStore
        self.modCount = backingStore.getModCount()
        self.first()

    def first(self):
        """Returns the cursor to the beginning of the backing store."""
        self.cursor = 0
        self.lastItemPos = -1

    def hasNext(self):
        """Returns True if the iterator has a next item or False otherwise."""
        return self.cursor < len(self.backingStore)

    def next(self):
        """Preconditions: hasNext returns True
        The list has not been modified except by this iterator's mutators.
        Returns the current item and advances the cursor to the next item.
        Postcondition: lastItemPos is now defined.
        Raises: ValueError if no next item.
        AttributeError if illegal mutation of backing store."""
        if not self.hasNext():
            raise ValueError("No next item in list iterator")
        if self.modCount != self.backingStore.getModCount():
            raise AttributeError("Illegal modification of backing store")
        self.lastItemPos = self.cursor
        self.cursor += 1
        return self.backingStore[self.lastItemPos]

    def last(self):
        """Moves the cursor to the end of the backing store."""
        self.cursor = len(self.backingStore)
        self.lastItemPos = -1

    def hasPrevious(self):
        """Returns True if the iterator has a previous item or False otherwise."""
        return self.cursor > 0

    def previous(self):
        """Preconditions: hasPrevious returns True
        The list has not been modified except by this iterator's mutators.
        Returns the current item and moves the cursor to the previous item.
        Postcondition: lastItemPos is now defined.
        Raises: ValueError if no next item.
        AttributeError if illegal mutation of backing store."""
        if not self.hasPrevious():
            raise ValueError("No previous item in list iterator")
        if self.modCount != self.backingStore.getModCount():
            raise AttributeError("Illegal modification of backing store")
        self.cursor -= 1
        self.lastItemPos = self.cursor
        return self.backingStore[self.lastItemPos]

    def replace(self, item):
        """Preconditions: the current position is defined.
        The list has not been modified except by this iterator's mutators.
        Replaces the items at the current position with item.
        Raises: AttibuteError if position is not defined.
        AttributeError if illegal mutation of backing store."""
        if self.lastItemPos == -1:
            raise AttributeError("The current position is undefined.")
        if self.modCount != self.backingStore.getModCount():
            raise AttributeError("List has been modified illegally.")
        self.backingStore[self.lastItemPos] = item
        self.lastItemPos = -1

    def insert(self, item):         
        """Preconditions:
        The list has not been modified except by this iterator's mutators.
        Adds item to the end if the current position is undefined, or
        inserts it at that position.
        Raises: AttributeError if illegal mutation of backing store."""
        if self.modCount != self.backingStore.getModCount():
            raise AttributeError("List has been modified illegally.")
        if self.lastItemPos == -1:
            self.backingStore.add(item)
        else:
            self.backingStore.insert(self.lastItemPos, item)
            self.lastItemPos = -1
        self.modCount += 1

    def remove(self):         
        """Preconditions: the current position is defined.
        The list has not been modified except by this iterator's mutators.
        Pops the item at the current position.
        Raises: AttibuteError if position is not defined.
        AttributeError if illegal mutation of backing store."""
        if self.lastItemPos == -1:
            raise AttributeError("The current position is undefined.")
        if self.modCount != self.backingStore.getModCount():
            raise AttributeError("List has been modified illegally.")
        item = self.backingStore.pop(self.lastItemPos)
        # If the item removed was obtained via next, move cursor back
        if self.lastItemPos < self.cursor:
            self.cursor -= 1
        self.modCount += 1
        self.lastItemPos = -1
