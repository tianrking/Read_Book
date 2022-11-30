"""
File: arrays.py
Project 4.6

Drops __iter__ and modifies __str__.  The user of an array
should only be able to see the items currently available in it.
The user can use an index-based loop over its logical size
to visit the items currently available in the array.

An Array is a restricted list whose clients can use
only [], len, iter, and str.

To instantiate, use

<variable> = array(<capacity>, <optional fill value>)

The fill value is None by default.
"""

class Array(object):
    """Represents an array."""

    def __init__(self, capacity, fillValue = None):
        """Capacity is the static size of the array.
        fillValue is placed at each position."""
        self.items = list()
        self.logicalSize = 0
        # Track the capacity and fill value for adjustments later
        self.capacity = capacity
        self.fillValue = fillValue
        for count in range(capacity):
            self.items.append(fillValue)

    def __len__(self):
        """-> The capacity of the array."""
        return len(self.items)

    def __str__(self):
        """-> The string representation of the array."""
        result = ""
        for index in range(self.size()):
            result += str(self.items[index]) + " "
        return result

    def __getitem__(self, index):
        """Subscript operator for access at index.
        Precondition: 0 <= index < size()"""
        if index < 0 or index >= self.size():
            raise IndexError("Array index out of bounds")
        return self.items[index]

    def __setitem__(self, index, newItem):
        """Subscript operator for replacement at index.
        Precondition: 0 <= index < size()"""
        if index < 0 or index >= self.size():
            raise IndexError("Array index out of bounds")
        self.items[index] = newItem

    def size(self):
        """-> The number of items in the array."""
        return self.logicalSize

    def grow(self):
        """Increases the physical size of the array if necessary."""
        # Double the physical size if no more room for items
        # and add the fillValue to the new cells in the underlying list
        for count in range(len(self)):
            self.items.append(self.fillValue)

    def shrink(self):
        """Decreases the physical size of the array if necessary."""
        # Shrink the size by half but not below the default capacity
        # and remove those garbage cells from the underlying list
        newSize = max(self.capacity, len(self) // 2)
        for count in range(len(self) - newSize):   
            self.items.pop()

    def insert(self, index, newItem):
        """Inserts item at index in the array."""
        if self.size() == len(self):
            self.grow()
        if index >= self.size():
            self.items[self.size()] = newItem
        else:
            index = max(index, 0)
            # Shift items down by one position
            for i in range(self.size(), index, -1):      
                self.items[i] = self.items[i - 1]

            # Add new item and increment logical size                       
            self.items[index] = newItem 
        self.logicalSize += 1

    def pop(self, index):
        """Removes and returns item at index in the array.
        Precondition: 0 <= index < size()"""
        if index < 0 or index >= self.size():
            raise IndexError("Array index out of bounds")
        itemToReturn = self.items[index]
        # Shift items up by one position
        for i in range(index, self.size() - 1):       
            self.items[i] = self.items[i + 1]
        # Reset empty slot to fill value
        self.items[self.size() - 1] = self.fillValue
        self.logicalSize -= 1
        if self.size() <= len(self) // 4 and len(self) > self.capacity:
            self.shrink()
        return itemToReturn

    def __eq__(self, other):
        """Returns True if the two arrays are equal or
        False otherwise."""
        if self is other: return True
        if type(self) != type(other): return False
        if self.size() != other.size(): return False
        for index in range(self.size()):
            if self[index] != other[index]:
                return False
        return True


def main():
    """Test code for modified Array class."""
    a = Array(10)
    for item in range(4):
        a.insert(0, item)
    print(a)
    
if __name__ == "__main__":
    main()
