from computer import *


class ResaleShop:


    inventory: list


    def __init__(self):
        self.inventory = []

        
        def buyComputer(self):
            # example:
            # comp = Computer(2023, 169.00, "OS", "Silver", "M1", "1 TB", "500 GB")
            # comp = Computer(yearMade, ogPrice, operatingSystem, description, processorType, hardDriveCapacity, memory)
            comp = Computer
            # need to make it so that the comp is aligned with an itemID
            # so you're really appending the itemID i think
            self.inventory.append(comp)




        def sellComputer(self, comp: Computer):
            # need it so when its sold the comp/or itemID is removed from the list ig
            if comp in self.inventory:
                self.inventory.pop(comp)
            else:
                return "Sorry item", comp, "can not be found."
            



        def updatePrice(self, comp: Computer, newPrice):
            # im confused about this method and i dont know if i even need it
            if comp in self.inventory:
                self.inventory[comp]["price"] = self.newPrice
            else:
                print("Item", comp, "not found. Cannot update price.")





        def refurbish(self, comp: Computer, newOperatingSystem):
            # this needs to update all the stuff and do all the stuff on the computer
            if comp in self.inventory:
                if int(comp[self.yearMade]) < 2000:
                    comp[self.newPrice] = 0
                elif int(comp[self.yearMade]) < 2012:
                    comp[self.newPrice] = 250
                elif int(comp[self.yearMade]) < 2018:
                    comp[self.newPrice] = 550
                else:
                    comp[self.newPrice] = 1000
                if self.newOperatingSystem is not None:
                    comp[self.operatingSystem] = self.newOperatingSystem
            else:
                print("Item", comp, "not found. Please select another item to refurbish.")





    def main():
        pass
    
    main()