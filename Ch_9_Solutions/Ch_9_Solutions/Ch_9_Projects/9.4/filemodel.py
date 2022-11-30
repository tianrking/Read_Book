"""
File: filemodel.py
Project 9.4

Data model for a file viewer.  Supports navigation
through the lines of a file.
"""

from linkedlist import LinkedList

class FileModel(object):

    def __init__(self, filename):
        file = open(filename, 'r')
        self._list = LinkedList().listIterator()
        for line in file:
            self._list.insert(line)
        file.close()    

    def first(self):
        self._list.first()
        return self.next()

    def last(self):
        self._list.last()
        return self.previous()

    def next(self):
        if self._list.hasNext():
            return self._list.next()
        else:
            return None

    def previous(self):
        if self._list.hasPrevious():
            return self._list.previous()
        else:
            return None

