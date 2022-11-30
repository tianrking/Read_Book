"""
File: algorithms.py
Project 12.3

Completes the function spanTree.

Graph processing algorithms
"""

from linkedstack import LinkedStack
from grid import Grid

INFINITY = "-"

def topoSort(g, startLabel = None):  
    stack = LinkedStack()
    g.clearVertexMarks()
    for v in g.getVertices():
        if not v.isMarked():
            dfs(g, v, stack)
    lyst = []
    return stack

def dfs(g, v, stack):
    v.setMark()
    for w in g.neighboringVertices(v.getLabel()):
        if not w.isMarked():
            dfs(g, w, stack)
    stack.push(v)


def spanTree(g, startLabel):
    g.clearVertexMarks()
    unVisitedVertices = set(g.getVertices())
    visitedVertices = []
    leastCostEdges = []
    startVertex = g.getVertex(startLabel)
    startVertex.setMark()
    visitedVertices.append(startVertex)
    unVisitedVertices.remove(startVertex)
    while len(unVisitedVertices) != 0:
        edge = findLeastCostEdge(visitedVertices, g)
        if edge is None:
            return leastCostEdges 
        u = edge.getToVertex()
        u.setMark()
        unVisitedVertices.remove(u)
        visitedVertices.append(u)
        leastCostEdges.append(edge)
    return leastCostEdges

def findLeastCostEdge(visitedVertices, g):
    def findLeastCost(v, g):
        resultEdge = None
        minWeight = INFINITY
        for edge in g.incidentEdges(v.getLabel()):
            toVertex = edge.getToVertex()
            if not toVertex.isMarked() and \
               isLessWithInfinity(edge.getWeight(), minWeight):
                minWeight = edge.getWeight()
                resultEdge = edge
        return resultEdge
    leastCostEdge = None
    for v in visitedVertices:
        leastCostEdge = findLeastCost(v, g)
        if leastCostEdge != None:
            return leastCostEdge
    return leastCostEdge

def shortestPaths(g, startLabel):
    # Exercise
    return ["Under development"]

   
def isLessWithInfinity(a, b):
    """Returns True if a < b, or False otherwise.
    a and/or b might be INFINITY."""
    if a == INFINITY and b == INFINITY: return False
    elif b == INFINITY: return True
    elif a == INFINITY: return False
    else: return a < b



