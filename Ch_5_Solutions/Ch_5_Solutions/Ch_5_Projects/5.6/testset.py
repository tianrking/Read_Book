"""
File: testset.py
Author: Ken Lambert
A tester program for set implementations.
"""

from arrayset import ArraySet

def test(setType):
    """Expects a bag type as an argument and runs some tests
    on objects of that type."""
    print("Testing", setType)
    lyst = list(range(1, 11))
    print("The list of items added is:", lyst)
    s = setType(lyst)
    print("Expect the set's string:", s)
    print("Add same items to test for uniqueness:")
    for i in range(1, 11):
        s.add(i)
    print("Expect the set's string:", s)

test(ArraySet)

