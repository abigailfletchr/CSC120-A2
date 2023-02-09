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
    Method to sell the computer which returns the computer taken off of the inventory list.
    """
    def sellComputer(self, comp: Computer):
        if comp in self.inventory:
            return self.inventory.pop(comp)
            # self.inventory.remove(comp)
        else:
            return "Sorry item", comp, "can not be found."
        


    """
    Method to update the price of a computer.
    """
    def updatePrice(self, comp: Computer, newPrice):
        if comp in self.inventory:
            # self.inventory[comp.ogPrice] = self.newPrice
            # self.inventory[comp][comp.ogPrice] = newPrice
            self.inventory[comp].ogPrice = newPrice
        else:
            print("Item", comp, "not found. Cannot update price.")



    """
    Method to refurbish a computer which updates its price and operating system.
    """
    def refurbish(self, comp: Computer):
        newOperatingSystem = "MacOS Monteray"

        if comp in self.inventory:

            self.inventory[comp].operatingSystem = newOperatingSystem

            if int(self.inventory[comp].yearMade) < 2000:
                self.inventory[comp].ogPrice = 0
            elif int(self.inventory[comp].yearMade) < 2012:
                self.inventory[comp].ogPrice = 250
            elif int(self.inventory[comp].yearMade) < 2018:
                self.inventory[comp].ogPrice = 550
            else:
                self.inventory[comp].ogPrice = 1000
        else:
            print("Item", comp, "not found. Please select another item to refurbish.")

    """
    Method to print the inventory of the resale store.
    """
    def printInventory(self):
        for i in range(len(self.inventory)):
            print(self.inventory[i].printDetails())
        # for comp in self.inventory:
        #     print(comp.printDetails())


"""
The main method
"""
def main():
    # pass
    rs = ResaleShop()

    rs.buyComputer(2020, 4000, "23.234.", "ugly", "intel", 128, 64)

    rs.printInventory()


main()