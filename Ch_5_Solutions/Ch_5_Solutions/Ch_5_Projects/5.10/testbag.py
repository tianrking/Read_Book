"""
File: testbag.py
Author: Ken Lambert
A tester program for bag implementations.
"""

from arraybag import ArrayBag
from linkedbag import LinkedBag
from arraysortedbag import ArraySortedBag
from random import shuffle

def test(bagType):
    """Expects a bag type as an argument and runs some tests
    on objects of that type."""
    print("Testing", bagType)
    lyst = list(range(1, 11))
    shuffle(lyst)
    print("The list of items added is:", lyst)
    b = bagType(lyst)
    print("Expect the bag's string, in ascending order:", b)
    print("Add 5 more items to test increasing the array size:")
    for i in range(11, 16):
        b.add(i)
    print("Expect the bag's string:", b)

test(ArraySortedBag)
#test(LinkedBag)
