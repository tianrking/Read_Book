"""
File: algorithms.py

Project 12.2

Completes the other classes for this application.

Graph processing algorithms
"""

from linkedstack import LinkedStack

def topoSort(g, startLabel = None):  
    stack = LinkedStack()
    g.clearVertexMarks()
    for v in g.getVertices():
        if not v.isMarked():
            dfs(g, v, stack)
    return stack

def dfs(g, v, stack):
    v.setMark()
    for w in g.neighboringVertices(v.getLabel()):
        if not w.isMarked():
            dfs(g, w, stack)
    stack.push(v)

def shortestPaths(g, startLabel):
    # Exercise
    return ["Under development"]

def spanTree(g, startLabel):
    # Exercise
    return ["Under development"]


