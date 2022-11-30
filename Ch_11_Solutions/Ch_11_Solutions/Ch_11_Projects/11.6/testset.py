"""
File: testset.py

Project 11.6

A tester program for HashSet.
Prints the length of the set and its load factor before each addtion.
"""

from hashset import HashSet

def test():
    """Expects a set type as an argument and runs some tests
    on objects of that type."""
    s = HashSet()
    for i in range(10):
        print("Number of items before add:", len(s))
        print("Load factor before add:", s.loadFactor())
        s.add(i)
    print(s)

test()
