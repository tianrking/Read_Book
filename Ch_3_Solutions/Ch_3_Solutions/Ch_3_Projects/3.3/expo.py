"""
File: expo.py
Project 3.3

Defines a function to raise a number to a given power.
The complexity is O(n), where n is the exponent.
"""

def expo(base, exponent):
    """Raises base to exponent."""
    if exponent == 0:
        return 1
    else:
        return base * expo(base, exponent - 1)


def main():
    """Tests with powers of 2."""
    for exponent in range (5):
        print(exponent, expo(2, exponent))

if __name__ == "__main__":
    main()    

