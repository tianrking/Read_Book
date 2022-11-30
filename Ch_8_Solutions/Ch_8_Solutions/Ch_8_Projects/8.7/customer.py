"""
File: customer.py
Project 8.7

Customer's processing time varies around the average,
so give it a random time between 1 and average time * 2 + 1.

"""

import random

class Customer(object):

    @classmethod
    def generateCustomer(cls, probabilityOfNewArrival,
                         arrivalTime,
                         averageTimePerCustomer):
        """Returns a Customer object if the probability 
        of arrival is greater than or equal to a random number.
        Otherwise, returns None, indicating no new customer.
        """                                     
        if random.random() <= probabilityOfNewArrival:
            return Customer(arrivalTime, averageTimePerCustomer)
        else:
            return None
       
    def __init__(self, arrivalTime, serviceNeeded):
        self.arrivalTime = arrivalTime
        self.amountOfServiceNeeded = random.randint(1, serviceNeeded * 2 + 1)

    def getArrivalTime(self):
        return self.arrivalTime
   
    def getAmountOfServiceNeeded(self):
        return self.amountOfServiceNeeded
   
    def serve(self):
        """Accepts a unit of service from the cashier."""
        self.amountOfServiceNeeded -= 1
