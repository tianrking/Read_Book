"""
File: path.py
Project 12.6

Defines and tests the hasPath function.

"""

from graph import LinkedDirectedGraph
from linkedqueue import LinkedQueue

def breadthFirst(g, startLabel):
    """Returns a list of the vertex labels in the
    order in which the vertices were visited."""
    result = list()
    g.clearVertexMarks()
    queue = LinkedQueue()
    queue.add(g.getVertex(startLabel))
    while not queue.isEmpty():
        vertex = queue.pop()
        if not vertex.isMarked():
            vertex.setMark()
            result.append(vertex.getLabel()) 
            for neighbor in vertex.neighboringVertices():
                if not neighbor.isMarked():
                    queue.add(neighbor)
    return result

def hasPath(g, startLabel, endLabel):
    """Returns True if there is a path from startLabel to endLabel
    or False otherwise."""
    route = breadthFirst(g, startLabel)
    for label in route:
        if label == endLabel and label != startLabel:
            return True
    return False


def main():
    g = LinkedDirectedGraph()

    # Insert vertices
    g.addVertex("A")
    g.addVertex("B")
    g.addVertex("C")
    g.addVertex("D")
    g.addVertex("E")

    # Insert weighted edges
    g.addEdge("A", "B", 3)
    g.addEdge("A", "C", 2)
    g.addEdge("B", "D", 1)
    g.addEdge("C", "D", 1)
    g.addEdge("D", "E", 2)

    print("The graph:\n", g)
    for vertex in g:
        label = vertex.getLabel()
        print("Path from B to " + label + ": " + str(hasPath(g, "B", label)))
    print ("Path from B to X: " + str(hasPath(g, "B", "X")))

if __name__ == "__main__": main()
