"""
File: testdict.py

Project 11.7

Tests a hash-based dictionary.
"""

from hashdict import HashDict

def main(capacity = 10):
    """You can specify a capacity with a HashDict."""
    d = HashDict()
    for key in range(1, capacity + 1):
        d[key] = "Value" + str(key)
    print("\nLength: ", len(d))
    print("\nThe dictionary:", d)
    print("\nThe keys:", list(d.keys()))
    print("\nThe values:", list(d.values()))
    print("\nThe entries:", list(map(str, d.entries())))  
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

