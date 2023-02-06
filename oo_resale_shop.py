from computer import *

class ResaleShop:

    inventory: list
   

    # How will you set up your constructor?
    # idk what this wants me to do


    def __init__(self):
        self.inventory = []


    # What methods will you need?

        
        def buyComputer(self):
            comp = Computer(2023, 169.00, "OS", "Silver", "M1", "1 TB", "500 GB")
            self.inventory.append(comp)

        def sellComputer(self):
            
           



























        def updatePrice(self, itemID, newPrice):
            if itemID in self.inventory:
                self.inventory[itemID]["price"] = newPrice
            else:
                print("Item", itemID, "not found.")

        def sellComputer(self, itemID):
            if itemID in self.inventory:
                del self.inventory[itemID]
                print("Item", itemID, "sold!")
            else: 
                print("Item", itemID, "not found. Please select another item to sell.")

        def printInventory(self, itemID):
            if self.inventory:
                for itemID in self.inventory:
                    print(f'Item ID: {itemID} : {self.inventory[itemID]}')
            else:
                print("No inventory to display.")

        def refurbish(self, itemID):
            if itemID in self.inventory:
                computer = self.inventory[itemID]
                if int(computer["yearMade"]) < 2000:
                    computer["newPrice"] = 0 
                elif int(computer["yearMade"]) < 2012:
                    computer["newPrice"] = 250
                elif int(computer["yearMade"]) < 2018:
                    computer["newPrice"] = 550
                else:
                    computer["newPrice"] = 1000
            else:
                print("Item", itemID, "not found. Please select another item to refurbish.")


        
    def main():

        computerOne = ResaleShop("01", {"2002, 3000, older OS"})
        computerOne.print()
    
    main()
