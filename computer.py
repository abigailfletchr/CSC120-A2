from ResaleShop import *

"""

Computer class which constructs computers with a year, price, 
operating system, description, processor type, hard drive capacity and memory.

Name: Abigail Fletcher
Professor: Jordan Crouser

"""

class Computer:

    yearMade: int
    ogPrice: float
    operatingSytem: str
    description: str
    processorType: str
    hardDriveCapacity: int
    memory: int
  
    """
    Computer constructor
    """
    def __init__(self, yearMade, ogPrice, operatingSystem, description, processorType, hardDriveCapacity, memory):

        self.yearMade = 0
        self.ogPrice = 0.0
        self.operatingSystem = ""
        self.description = ""
        self.processorType = ""
        self.hardDriveCapacity = 0
        self.memory = 0


    """
    Method to print all of the details of a computer.
    """
    def printDetails(self):
        for comp in self.inventory:
            print(self.yearMade)
            print(self.ogPrice)
            print(self.operatingSystem)
            print(self.description)
            print(self.processorType)
            print(self.hardDriveCapacity)
            print(self.memory)

