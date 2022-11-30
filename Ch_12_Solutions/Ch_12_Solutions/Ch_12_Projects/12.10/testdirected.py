"""
File: testdirected.py

Project 12.10
Tests +, ==, in, and clone operations.
"""

from graph import LinkedDirectedGraph

# Create a directed graph using an adjacency list
g = LinkedDirectedGraph("ABCD")

# Insert edges with different weights and print the graph
g.addEdge("A", "B", 1)
g.addEdge("B", "C", 3)
g.addEdge("C", "B", 2)
g.addEdge("B", "D", 5)
print("The graph:", g)

# Test the in operator
print("Expect True:", "B" in g)
print("Expect False:", "E" in g)

# Test the clone method
g2 = g.clone()
print("The clone:", g2)

#Test +
g3 = LinkedDirectedGraph("EFG")
g3.addEdge("E", "F", 6)
g3.addEdge("G", "E", 8)
print("First graph:", g)
print("New graph:", g3)
print("Add first graph and new graph with +:")
print(g + g3)

#Test ==
print("Expect True:", g == g)
print("Expect False:", g == list("ABCD"))
print("Expect False:", g == LinkedDirectedGraph("ABCD"))
print("Expect True:", g == g2)
print("Expect False:", g == g3)

# Precondition on +
print("Expect an error when running g + g:")
print(g + g)

