"""
File: fib.py
Project 3.6

Employs memoization to improve the efficiency of recursive Fibonacci.
"""

def fib(n, table):
    """Fibonacci function with a table for memoization."""
    if n < 3:
        return 1
    else:
        # Attempt to get values for n - 1 and n - 2
        # from the table
        # If unsuccessful, recurse and add results to
        # the table
        result1 = table.get(n - 1, None)
        if result1 is None:
            result1 = fib(n - 1, table)
            table[n - 1] = result1
        result2 = table.get(n - 2, None)
        if result2 is None:
            result2 = fib(n - 2, table)
            table[n - 2] = result2
        return result1 + result2

def main():
    """Tests the function with some powers of 2."""
    problemSize = 2
    print("%4s%12s" % ("n", "fib"))
    for count in range(5):
        print("%4d%12d" % (problemSize, fib(problemSize, {})))
        problemSize *= 2

if __name__ == "__main__":
    main()
