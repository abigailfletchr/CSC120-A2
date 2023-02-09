
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

        self.yearMade = yearMade
        self.ogPrice = ogPrice
        self.operatingSystem = operatingSystem
        self.description = description
        self.processorType = processorType
        self.hardDriveCapacity = hardDriveCapacity
        self.memory = memory


    """
    Method to print all of the details of a computer.
    """
    def printDetails(self):
        print("Year Made:", self.yearMade)
        print("Price:", self.ogPrice)
        print("Operating System:", self.operatingSystem)
        print("Description:", self.description)
        print("Processor Type:", self.processorType)
        print("Hard drive Capacity:", self.hardDriveCapacity)
        print("Memory:", self.memory)

