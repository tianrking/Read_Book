"""
File: testdirected.py

Project 12.7

Tests making a label table.
"""

from graph import LinkedDirectedGraph
import random

# Create a randomly ordered list of labels
lyst = list(map(lambda label: "Label" + str(label), range(1, 10)))
random.shuffle(lyst)
print("The listof labels:\n", lyst)

# Create and print a graph with those vertex labels
graph = LinkedDirectedGraph(lyst)
print("\nThe graph:\n", graph)

# Create and print the label table for the graph
table = graph.makeLabelTable()
print("\nThe label table:")
keys = list(table.keys())
keys.sort()
for key in keys:
    print(table[key], key)

