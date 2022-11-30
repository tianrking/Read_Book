"""
File: testdict.py

Project 11.9

Tests a tree-based sorted dictionary.
"""

from treesorteddict import TreeSortedDict

def main(capacity = 10):
    """You can specify a capacity with a TreeSortedDict."""
    d = TreeSortedDict()
    for key in range(1, capacity + 1):
        d[key] = "Value" + str(key)
    print("\nLength: ", len(d))
    print("\nThe dictionary:", d)
    print("\nThe keys:", list(d.keys()))
    print("\nThe values:", list(d.values()))
    print("\nThe items:", list(map(str, d.entries())))  
    print("\nKey Value (using []):", end = " ")
    for key in d:
        print(key, d[key], end = " ")
    print("\nReplace Value1 with ValueZ:", end = " ")
    d[1] = "ValueZ"
    print(d)
    print("\nDelete all keys:")
    for key in range(1, capacity + 1):
        print(d.pop(key))
    print("\nLength: ", len(d))
    
if __name__ == "__main__":
    main(5)

