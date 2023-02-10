from Computer import *

"""

Resale Shop class which holds an inventory (list) of computers.

Name: Abigail Fletcher
Professor: Jordan Crouser

"""

class ResaleShop:


    inventory: list


    """
    ResaleStore constructor
    """
    def __init__(self):
        self.inventory = []


    """
    Method to buy a computer given attributes of the computer.
    """
    def buyComputer(self, yearMade, ogPrice, operatingSystem, description, processorType, hardDriveCapacity, memory):
        comp = Computer(yearMade, ogPrice, operatingSystem, description, processorType, hardDriveCapacity, memory)
        self.inventory.append(comp)

    """
    Method to buy a computer given a computer.
    """
    def buyComputer(self, comp: Computer):
        self.inventory.append(comp)


    """
    Method to sell the computer which returns the computer taken off of the inventory list.
    """
    def sellComputer(self, comp: Computer):
        for c in self.inventory:
            if c == comp:
                removed = c
                self.inventory.remove(c)
                return removed
        print("This computer does not exist in the inventory!")
        # if comp in self.inventory:
        #     return self.inventory.pop(comp)
        # else:
        #     return "Sorry item", comp, "can not be found."
        

    """
    Method to update the price of a computer.
    """
    def updatePrice(self, comp: Computer, newPrice):
        # for c in self.inventory:
        #     if c == comp:
        #         c.
        comp.ogPrice = newPrice

    """
    Method to refurbish a computer which updates its price and operating system.
    """
    def refurbish(self, comp: Computer):
        newOperatingSystem = "MacOS Monteray"
        comp.operatingSystem = newOperatingSystem

        if int(comp.yearMade) < 2000:
            comp.ogPrice = 0
        elif int(comp.yearMade) < 2012:
            comp.ogPrice = 250
        elif int(comp.yearMade) < 2018:
            comp.ogPrice = 550
        else:
            comp.ogPrice = 1000


    """
    Method to print the inventory of the resale store.
    """
    def printInventory(self):
        for comp in self.inventory:
            print("___________________")
            comp.printDetails()
            print("___________________")


"""
The main method
"""
def main():

    print("@@@~~~~~~~~~~~~~~~~~~~@@@")
  
    rs = ResaleShop()

    comp1 = Computer(2023, 4000, "23.234", "ugly, very ugly", "M1", 128, 64)

    rs.buyComputer(comp1)

    rs.printInventory()

    print("1~~~~~~~~~~~~~~~~~~~1")

    rs.sellComputer(comp1)

    rs.printInventory()
    
    print("2~~~~~~~~~~~~~~~~~~~2\nShould be blank before here")

    comp2 = Computer(2000, 2000, "45.78", "white", "M1", 123, 23)

    rs.buyComputer(comp2)

    rs.printInventory()

    print("2~~~~~~~~~~~~~~~~~~~2\nREFURBISHING:")

    rs.refurbish(comp2)

    rs.printInventory()

    print("2~~~~~~~~~~~~~~~~~~~2\nUPDATING PRICE:")

    rs.updatePrice(comp2, 1500)

    rs.printInventory()


main()