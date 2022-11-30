"""
File: abstractdict.py
Project 10

Adds an unzip method to all dictionaries
"""

from abstractcollection import AbstractCollection

class AbstractDict(AbstractCollection):
    """Common data and method implementations for dictionaries."""

    def __init__(self, keys, values):
        """Will copy entries to the dictionary
        from keys and values if they are present."""
        AbstractCollection.__init__(self)
        if keys and values:
            valuesIter = iter(values)
            for key in keys:
                self[key] = next(valuesIter)

    def __str__(self):
        return " {" + ", ".join(map(str, self.entries())) + "}"

    def __add__(self, other):
        """Returns a new dictionary containing the contents
        of self and other."""
        result = type(self)(self.keys(), self.values())
        for key in other:
            result[key] = other[key]
        return result

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if self is other: return True
        if type(self) != type(other) or \
           len(self) != len(other):
            return False
        for key in self:
            if not key in other:
                return False
        return True

    def keys(self):
        """Returns an iterator on the keys in the dictionary."""
        return iter(self)

    def values(self):
        """Returns an iterator on the values in the dictionary."""
        return map(lambda key: self[key], self)

    def entries(self):
        """Returns an iterator on the entries in the dictionary."""
        return map(lambda key: Entry(key, self[key]), self)

    def get(self, key, defaultValue = None):
        """Returns the value associated with key if key is
        present, or defaultValue otherwise."""
        # Exercise       
        if not key in self:
            return defaultValue
        else:
            return self[key]

    def unzip(self):
        """Returns a tuple containing a list of keyes and
        a list of values in self."""
        return (list(self.keys()), list(self.values()))

class Entry(object):
    """Represents a dictionary entry.
    Supports comparisons by key."""

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.key) + ":" + str(self.value)

    def __eq__(self, other):
        if type(self) != type(other): return False
        return self.key == other.key

    def __lt__(self, other):
        if type(self) != type(other): return False
        return self.key < other.key

    def __le__(self, other):
        if type(self) != type(other): return False
        return self.key <= other.key
