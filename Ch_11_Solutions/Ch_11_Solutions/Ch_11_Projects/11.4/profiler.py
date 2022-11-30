"""
File: profiler.py
Project 11.4

Profile the get method for a hash table.
"""

from hashtable import HashTable

def stringHash(item):
    """Generates an integer key from a string."""
    if len(item) > 4 and \
       (item[0].islower() or item[0].isupper()):
        item = item[1:]           # Drop first letter
    sum = 0
    for ch in item:
        sum += ord(ch)
    if len(item) > 2:
        sum -= 2 * ord(item[-1])  # Subtract last ASCII
    return sum

class Profiler(object):
    "Represents a profiler for hash tables."""

    def __init__(self):
        self.table = None
        self.collisions = 0
        self.probeCount = 0

    def test(self, table, data):
        """Inserts the data into table and gather statistics."""
        self.table = table
        # Insert items here
        for item in data:
            table.insert(item)
        print("Table:", table)
        # Now remove half of the items
        for i in range(1, len(data), 2):
            table.remove(data[i])
        print("Table:", table)
        self.collisions = 0
        self.probeCount = 0
        self.result = "Load Factor  Item Accessed  Home Index  Actual Index   Probes\n"
        # Now get every third item from index 1
        for i in range(0, len(data), 2):
            loadFactor = table.getLoadFactor()
            table.get(data[i])
            homeIndex = table.getHomeIndex()
            actualIndex = table.getActualIndex()
            probes = table.getProbeCount()
            self.probeCount += probes
            if probes > 0:
                self.collisions += 1
            line = "%8.3f%14d%12d%12d%14d" % (loadFactor, data[i],
                                               homeIndex, actualIndex,
                                               probes)
            self.result += line + "\n"
        self.result += "Total collisions: " + str(self.collisions) + \
                        "\nTotal probes: " + str(self.probeCount) + \
                        "\nAverage probes per collision: " + \
                        str(self.probeCount / float(self.collisions))
                        

    def __str__(self):
        if self.table is None:
            return "No test has been run yet."
        else:
            return self.result

    def getCollisions(self):
        return self.collisions

    def getProbeCount(self):
        return self.probeCount
        
def main():
    # Create a table with 8 cells, an identity hash function,
    # and linear probing.
    table = HashTable(8, lambda x: x)
    # The data are the numbers from 10 through 70, by 10s
    data = range(10, 71, 10)
    profiler = Profiler()
    profiler.test(table, data)
    print(profiler)

if __name__ == "__main__": main()



        



