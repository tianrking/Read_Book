"""
File: matrix.py
Project 4.7

Defines a matrix class to support simple matrix arithmetic.
"""

from grid import Grid

class Matrix(Grid):
    """Represents a matrix."""

    def __init__(self, rows, columns, fillValue = 0):
        Grid.__init__(self, rows, columns, fillValue)

    def __add__(self, other):
        """Returns the sum of self and other."""
        sum = Matrix(self.getHeight(), self.getWidth())
        for row in range(self.getHeight()):
            for col in range(self.getWidth()):
                sum[row][col] = self[row][col] + other[row][col]
        return sum

    def __sub__(self, other):
        """Returns the difference of self and other."""
        return Matrix(self.getHeight(), self.getWidth())
    
    def __mul__(self, other):
        """Returns the product of self and other."""
        return Matrix(self.getHeight(), self.getWidth())

def main():
    m1 = Matrix(3, 3, 2)
    print(m1)
    m2 = Matrix(3, 3, 4)
    print(m2)
    print(m1 + m2)

if __name__ == "__main__": main()
    
            
