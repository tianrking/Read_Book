"""
File: test.py
Project 10.10

Runs a profile of a heap sort with increasing list sizes.

"""

from profiler import Profiler
from algorithms import heapSort

p = Profiler()
for size in (100, 1000, 10000, 100000):
    p.test(heapSort, size = size)
