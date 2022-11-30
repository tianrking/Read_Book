"""
File: testset.py
Project 6.5
Author: Ken Lambert

A tester program for set implementations.
"""

from arrayset import ArraySet
from linkedset import LinkedSet

def test(setType):
    """Expects a set type as an argument and runs some tests
    on objects of that type."""
    lyst = [2013, 61, 1973]
    print("The list of items added is:", lyst)
    s1 = setType(lyst)
    print("Expect 3:", len(s1))
    print("Expect the set's string:", s1)
    print("Expect True:", 2013 in s1)
    print("Expect False:", 2012 in s1)
    print("Expect the items on separate lines:")
    for item in s1:
        print(item)
    s1.clear()
    print("Expect {}:", s1)
    s1.add(25)
    s1.remove(25)
    print("Expect {}:", s1)
    s1 = setType(lyst)
    s2 = setType(s1)
    print("Expect True:", s1 == s2)
    print("Expect False:", s1 is s2)
    print("Expect one of each item:", s1 + s2)
    for item in lyst:
        s1.remove(item)
    print("Expect {}:", s1)

test(ArraySet)
test(LinkedSet)
