class Computer:

    # What attributes will it need?

    yearMade: int
    ogPrice: bool
    operatingSytem: str
    description: str
    processorType: str
    hardDriveCapacity: int
    memory: int
  

    def __init__(self, yearMade, ogPrice, operatingSystem, description, processorType, hardDriveCapacity, memory):

        self.yearMade = 0
        self.ogPrice = 0.0
        self.operatingSystem = ""
        self.description = ""
        self.processorType = ""
        self.hardDriveCapacity = 0
        self.memory = 0

    # What methods will you need?