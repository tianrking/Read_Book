"""
File: testdict.py

Project 11.10

Tests a tree-based sorted dictionary.
"""

from treesorteddict import TreeSortedDict
from hashdict import HashDict

def main(dictType, capacity = 10):
    """You can specify a capacity with a TreeSortedDict."""
    d = dictType()
    for key in range(1, capacity + 1):
        d[key] = "Value" + str(key)
    print("\nThe dictionary:", d)
    print("\nThe keys:", list(d.keys()))
    print("\nThe values:", list(d.values()))
    print("\nThe items:", list(map(str, d.entries())))
    print("\nUnzip:", d.unzip())
    
if __name__ == "__main__":
    main(HashDict, 5)

