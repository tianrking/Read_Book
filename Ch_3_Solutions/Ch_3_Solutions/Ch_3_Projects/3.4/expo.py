"""
File: expo.py
Project 3.4

Defines a function to raise a number to a given power.
Uses a recursive strategy to reduce the complexity to O(log n).
"""

def expo(base, exponent):
    """Raises base to exponent."""
    if exponent == 0:
        return 1
    elif exponent % 2 == 1:
        return base * expo(base, exponent - 1)
    else:
        result = expo(base, exponent // 2)
        return result * result

def main():
    """Tests with powers of 2."""
    for exponent in range (5):
        print(exponent, expo(2, exponent))

if __name__ == "__main__":
    main()    

