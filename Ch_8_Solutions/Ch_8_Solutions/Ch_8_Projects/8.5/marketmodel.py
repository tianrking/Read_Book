"""
File: model.py
Project 8.5

Picks the cashier with the shortest line length.
"""

from cashier import Cashier
from customer import Customer

class MarketModel(object):

    def __init__(self, lengthOfSimulation, averageTimePerCus,
                 probabilityOfNewArrival, numCashiers):
        self.probabilityOfNewArrival = probabilityOfNewArrival
        self.lengthOfSimulation = lengthOfSimulation
        self.averageTimePerCus = averageTimePerCus
        self.cashiers = list()
        for count in range(numCashiers):
            self.cashiers.append(Cashier(count + 1))
   
    def runSimulation(self):
        """Run the clock for n ticks."""
        for currentTime in range(self.lengthOfSimulation):
            # Attempt to generate a new customer
            customer = Customer.generateCustomer(
                self.probabilityOfNewArrival,
                currentTime,
                self.averageTimePerCus)

            # Send customer to a randomly chosen cashier
            # if successfully generated
            if customer != None:
                self.pickCashier().addCustomer(customer)
            # Tell all cashiers to provide another unit of service
            for cashier in self.cashiers:
                cashier.serveCustomers(currentTime)

    def __str__(self):
        """Returns the string rep of the results of the simulation."""
        return "CASHIER CUSTOMERS   AVERAGE     LEFT IN\n" + \
               "        PROCESSED   WAIT TIME   LINE\n" + \
               "\n".join(map(str, self.cashiers))

    def pickCashier(self):
        """Returns the cashier for the next customer, based on the
        shortest line of customers."""
        minIndex = 0
        minLineLength = 0
        for index in range(len(self.cashiers)):
            if self.cashiers[index].getLineLength() <= minLineLength:
                minIndex = index
                minLineLength = self.cashiers[index].getLineLength()
        return self.cashiers[minIndex]

