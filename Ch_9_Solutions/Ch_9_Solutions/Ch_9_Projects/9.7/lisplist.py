"""
File: lisplist.py
Project 9.7

Adds an insert function for Lisp lists.
"""

class Node(object):
    """Represents a singly linked node."""

    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __repr__(self):
        """Returns the string representation of a nonempty lisp list."""
        def buildString(lyst):
            if isEmpty(rest(lyst)):
                return str(first(lyst))
            else:
                return str(first(lyst)) + " " + buildString(rest(lyst))

        return "(" + buildString(self) + ")"

THE_EMPTY_LIST = None

# Basic functions

def isEmpty(lyst):
    """Returns True if lyst is empty or False otherwise."""
    return lyst is THE_EMPTY_LIST

def first(lyst):
    """Returns the item at the head of lyst.
    Precondition: lyst is not empty."""
    return lyst.data

def rest(lyst):
    """Returns a list of items in lyst, after the first one.
    Precondition: lyst is not empty."""
    return lyst.next

def cons(item, lyst):
    """Adds item to the head of lyst and
    returns the resulting list."""
    return Node(item, lyst)

# Auxiliary functions

def contains(item, lyst):
    """Returns True if item is in lyst or
    False otherwise."""
    if isEmpty(lyst):
        return False
    elif item == first(lyst):
        return True
    else:
        return contains(item, rest(lyst))

def get(index, lyst):
    """Returns the item at position index in lyst.
    Precondition: 0 <= index < length(lyst)"""
    if index == 0:
        return first(lyst)
    else:
        return get(index - 1, rest(lyst))

def length(lyst):
    """Returns the number of items in lyst."""
    if isEmpty(lyst): return 0
    else: return 1 + length(rest(lyst))
    
def buildRange(lower, upper):
    """Returns a list containing the numbers from
    lower through upper.
    Precondition: lower <= upper"""
    if lower == upper:
        return cons(lower, THE_EMPTY_LIST)
    else:
        return cons(lower, buildRange(lower + 1, upper))

def remove(index, lyst):
    """Returns a list with the item at index removed.
    Precondition: 0 <= index < length(lyst)"""
    if index == 0:
        return rest(lyst)
    else:
        return cons(first(lyst),
                    remove(index - 1, rest(lyst)))

def insert(index, item, lyst):
    """Returns a list with the item inserted at index.
    Precondition: 0 <= index < length(lyst)"""
    if index == 0:
        return cons(item, lyst)
    else:
        return cons(first(lyst),
                    insert(index - 1, item, rest(lyst)))


def main():
    """Test insert."""
    lyst = buildRange(1, 5)
    print("List =", lyst)
    print("Inserting 66 at position 2, expect (1 2 66 3 4 5):",
          insert(2, 66, lyst))

if __name__ == "__main__":
    main()
        
