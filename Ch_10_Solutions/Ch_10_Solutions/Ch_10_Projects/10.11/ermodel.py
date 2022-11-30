"""
File: ermodel.py
Project 10.11

Defines the classes ERModel, Patient, and Condition for an
emergency room scheduler.  Uses a heap-based priority queue.
"""

from heappriorityqueue import HeapPriorityQueue

class Condition(object):
    """Represents a condition."""

    def __init__(self, rank):
        self.rank = rank

    def __eq__(self, other):
        return self.rank == other.rank

    def __lt__(self, other):
        return self.rank < other.rank

    def __le__(self, other):
        return self.rank <= other.rank

    def __str__(self):
        """Returns the string rep of a condition."""
        if   self.rank == 1: return "critical"
        elif self.rank == 2: return "serious"
        else:                 return "fair"

class Patient(object):
    """Represents a patient with a name and a condition."""

    def __init__(self, name, condition):
        self.name = name
        self.condition = condition

    def __eq__(self, other):
        return self.condition == other.condition

    def __lt__(self, other):
        return self.condition < other.condition

    def __le__(self, other):
        return self.condition <= other.condition

    def __str__(self):
        """Returns the string rep of a patient."""
        return self.name + " / " + str(self.condition)

class ERModel(object):
    """Model of a scheduler."""

    def __init__(self):
        self.patients = HeapPriorityQueue()

    def isEmpty(self):
        """Returns True if there are patients in the model
        or False otherwise."""
        return self.patients.isEmpty()

    def schedule(self, p):
        """Adds a patient to the schedule."""
        self.patients.add(p)

    def treatNext(self):
        """Returns the patient treated or None if there are none."""
        if self.patients.isEmpty():
            return None
        else:
            return self.patients.pop()
