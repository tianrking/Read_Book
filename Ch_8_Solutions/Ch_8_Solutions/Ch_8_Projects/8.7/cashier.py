"""
File: cashier.py
Project 8.5

Get the line length.
"""

from linkedqueue import LinkedQueue

class Cashier(object):
    """Represents a cashier."""

    def __init__(self, number):
        """Maintains a cashier number, a queue of customers,
        number of customers served, total customer wait time,
        and a current customer being processed."""
        self.number = number
        self.totalCustomerWaitTime = 0
        self.customersServed = 0
        self.currentCustomer = None
        self.queue = LinkedQueue()

    def getLineLength(self):
        """Returns the number of customers in the line."""
        return len(self.queue)

    def addCustomer(self, c):
        """Adds an arriving customer to my line."""
        self.queue.add(c)
   
    def serveCustomers(self, currentTime):
        """Serves my cuatomers during a given unit of time."""
        if self.currentCustomer is None:
            # No customers yet
            if self.queue.isEmpty():
                return
            else:
                # Pop first waiting customer and tally results
                self.currentCustomer = self.queue.pop()
                self.totalCustomerWaitTime += \
                                            currentTime - \
                                            self.currentCustomer.getArrivalTime()
                self.customersServed += 1

        # Give a unit of service
        self.currentCustomer.serve()

        # If current customer is finished, send it away   
        if self.currentCustomer.getAmountOfServiceNeeded() == 0:
            self.currentCustomer = None
   
    def __str__(self):
        """Returns my results: my number, my total customers served,
        my average wait time per customer, and customers left on my queue."""
        if self.customersServed != 0:
            aveWaitTime = float(self.totalCustomerWaitTime) /\
                          self.customersServed
        else:
            aveWaitTime = 0.0
        result = "%4d %8d %13.2f %8d" % (self.number,
                                         self.customersServed,
                                         aveWaitTime,
                                         len(self.queue))
        return result
