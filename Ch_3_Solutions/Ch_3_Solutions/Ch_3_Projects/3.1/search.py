"""
File: search.py
Project 3.1

Optimizes linear search for sorted lists.
The complexity is O(n) in the worst case and O(1) in the best case.
The average case is less than n / 2, because there are many lists
for which the search for an absent target can stop early.  But the
average case is still approximately O(n).
"""

def linearSearch(target, lyst):
    """Returns the position of the target item if found,
    or -1 otherwise.
    The lyst is assumed to be sorted in ascending order."""
    position = 0
    while position < len(lyst):
        if target == lyst[position]:
            return position
        elif target < lyst[position]:  # Target less, so it
            return -1                  # can't be in sorted list
        position += 1
    return -1

def main():
    """Tests with three lists."""
    print(linearSearch(3, [0, 1, 2, 3, 4]))
    print(linearSearch(3, [0, 1, 2]))
    # Will stop at second position.
    print(linearSearch(3, [0, 4, 5, 6]))

if __name__ == "__main__":
    main()
    

