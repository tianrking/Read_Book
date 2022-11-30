"""
File: model.py
Project 8.6

Picks the cashier with the shortest line length no further
than two lines away from a randomly chosen line.
"""

from cashier import Cashier
from customer import Customer
import random

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
        shortest line of customers no more than two lines away."""
        # Pick a random index and create a sublist of the allowable
        # cashiers
        randomIndex = random.randint(0, len(self.cashiers) - 1)
        if randomIndex == 0:
            shortList = self.cashiers[:3]
        elif randomIndex == len(self.cashiers) - 1:
            shortList = self.cashiers[-3:]
        elif randomIndex == 1:
            shortList = self.cashiers[:4]
        elif randomIndex == len(self.cashiers) - 2:
            shortList = self.cashiers[-4:]
        else:
            shortList = self.cashiers[randomIndex - 2:randomIndex + 3]
        # Search the short list for the cashier with the shortest line
        minIndex = 0
        minLineLength = 0
        for index in range(len(shortList)):
            if shortList[index].getLineLength() <= minLineLength:
                minIndex = index
                minLineLength = shortList[index].getLineLength()
        return shortList[minIndex]

