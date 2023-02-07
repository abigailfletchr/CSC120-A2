from computer import *


class ResaleShop:


    inventory: list


    def __init__(self):
        self.inventory = []

        
        def buyComputer(self):
            comp = Computer(2023, 169.00, "OS", "Silver", "M1", "1 TB", "500 GB")
            # need to make it so that the comp is aligned with an itemID
            # so you're really appending the itemID i think
            self.inventory.append(comp)


        def sellComputer(self):
            # need it so when its sold the comp/or itemID is removed from the list ig
            if itemID in self.inventory:
                self.inventory.pop(itemID)
            else:
                return "Sorry item", itemID, "can not be found."
            

        def updatePrice(self):
            # im confused about this method and i dont know if i even need it
            if itemID in self.inventory:
                pass


        def refurbish(self):
            # this needs to update all the stuff and do all the stuff on the computer
            if itemID in self.inventory:
                pass

        def printInventory(self):
            # prints out inventory for the user to see what's in it
            pass


            
        




        # this is to work off of ...
        
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
        pass
    
    main()
