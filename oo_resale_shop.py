from computer import *


class ResaleShop:


    inventory: list


    def __init__(self):
        self.inventory = []

        
        def buyComputer(self):
            # example:
            comp = Computer(2023, 169.00, "OS", "Silver", "M1", "1 TB", "500 GB")
            # need to make it so that the comp is aligned with an itemID
            # so you're really appending the itemID i think
            self.inventory.append(comp)



        # def sell(self, c: Computer):
        # if c in self.inventory:
        #   self.inventory.pop(c)





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
            # you can do this in computer, the computer.py class, use it as a method there
            # for comp in self.inventory
            #   printDetails()
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


# questions
# do i need to connect an ID to the comp in the list, or is the comp index just the ID
# response: dont need ID, the index is the ID for the comp compiuter class
# what other computer class methods do i need
# response: probab;y just the print details
# if i create a print details method in computer class, do i access that method in resale shop class or?
# response: no hehe