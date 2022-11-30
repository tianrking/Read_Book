"""
File: testbag.py
Author: Ken Lambert
A tester program for bag implementations.
"""

from arraybag import ArrayBag
from linkedbag import LinkedBag

def test(bagType):
    """Expects a bag type as an argument and runs some tests
    on objects of that type."""
    print("Testing", bagType)
    lyst = list(range(1, 11))
    print("The list of items added is:", lyst)
    b = bagType(lyst)
    print("Expect the bag's string:", b)
    print("Add 5 more items to test increasing the array size:")
    for i in range(11, 16):
        b.add(i)
    print("Expect the bag's string:", b)

def testClone(bagType):
    """Tests the resizing of an array-based bag,
    when space is wasted."""
    print("Testing", bagType)
    bag1 = bagType([2,3,4])
    bag2 = bag1.clone()
    print("Creating bag1 with 2, 3, and 4.")
    print("Cloning bag1 to bag2.")
    print("Expect {2, 3, 4} and {2, 3, 4}.")
    print(bag1, bag2)
    print("Expect True for ==:", bag1 == bag2)
    print("Expect False for is:", bag1 is bag2)

testClone(ArrayBag)
testClone(LinkedBag)
