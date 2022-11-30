"""
File: hashtable.py
Project 11.3

Adds the get and remove methods to HashTable.
"""

from arrays import Array

class HashTable(object):
    "Represents a hash table."""

    EMPTY = None
    DELETED = True

    def __init__(self, capacity = 29,
                 hashFunction = hash,
                 linear = True):
        self.table = Array(capacity, HashTable.EMPTY)
        self.size = 0
        self.hash = hashFunction
        self.homeIndex = -1
        self.actualIndex = -1
        self.linear = linear
        self.probeCount = 0

    def insert(self, item):
        """Inserts item into the table
        Preconditions: There is at least one empty cell or
        one previously occupied cell.
        There is not a duplicate item."""
        self.probeCount = 0
        # Get the home index
        self.homeIndex = abs(self.hash(item)) % len(self.table)
        distance = 1
        index = self.homeIndex

        # Stop searching when an empty cell is encountered
        while not self.table[index] in (HashTable.EMPTY,
                                         HashTable.DELETED):

            # Increment the index and wrap around to first 
            # position if necessary
            if self.linear:
                increment = index + 1
            else:
                # Quadratic probing
                increment = self.homeIndex + distance ** 2
                distance += 1
            index = increment % len(self.table)
            self.probeCount += 1

        # An empty cell is found, so store the item
        self.table[index] = item
        self.size += 1
        self.actualIndex = index

    def __len__(self):
        return self.size

    def __str__(self):
        return str(self.table)

    def getLoadFactor(self):
        return float(len(self)) / len(self.table)

    def getHomeIndex(self):
        return self.homeIndex

    def getActualIndex(self):
        return self.actualIndex

    def getProbeCount(self):
        return self.probeCount

    def get(self, item):
        """Returns the index if the item is present
        or -1 otherwise."""
        self.probeCount = 0
        # Get the home index
        self.homeIndex = abs(self.hash(item)) % len(self.table)
        distance = 1
        index = self.homeIndex

        # Stop searching when an empty cell is encountered
        while  (self.table[index] != HashTable.EMPTY or \
                self.table[index] == HashTable.DELETED) and \
                self.table[index] != item:

            # Increment the index and wrap around to first 
            # position if necessary
            if self.linear:
                increment = index + 1
            else:
                # Quadratic probing
                increment = self.homeIndex + distance ** 2
                distance += 1
            index = increment % len(self.table)
            self.probeCount += 1

        if self.table[index] == item:
            self.actualIndex = index
            return index
        else:
            self.actualIndex = -1
            return -1

    def remove(self, item):
        """Removes the item if it exists and returns its index or
        returns -1 otherwise."""
        # Get the home index
        self.homeIndex = abs(self.hash(item)) % len(self.table)
        distance = 1
        index = self.homeIndex

        # Stop searching when an empty cell or the target item
        # is encountered
        while  (self.table[index] != HashTable.EMPTY or \
                self.table[index] == HashTable.DELETED) and \
                self.table[index] != item:

            # Increment the index and wrap around to first 
            # position if necessary
            if self.linear:
                increment = index + 1
            else:
                # Quadratic probing
                increment = self.homeIndex + distance ** 2
                distance += 1
            index = increment % len(self.table)
            self.probeCount += 1

        if self.table[index] == item:
            self.table[index] = HashTable.DELETED
            self.actualIndex = index
            self.size -= 1
            return index
        else:
            self.actualIndex = -1
            return -1
        
def main():
    """Uses an example data set from Chapter 19."""
    table = HashTable(8, lambda x : x)
    for item in range(10, 71, 10):
        table.insert(item)
    print("Table:", table)
    print("Items and positions during runs of the method get:")
    for item in range(10, 71, 10):
        print(item, table.get(item))
    print("Items, positions, and the table during runs of the method remove:")
    for item in range(10, 71, 10):
        print(item, table.remove(item))
        print(table)
    

if __name__ == "__main__": main()

        



