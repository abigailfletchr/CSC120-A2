class Computer:

    # What attributes will it need?

    itemID: int = 0
    yearMade: int = 0
    ogPrice: bool = 0.0
    operatingSytem: str = ""

  
    # How will you set up your constructor?
    # idk what this means

    def __init__(self, itemID, yearMade, ogPrice, operatingSystem):
        self.itemID = itemID
        self.yearMade = yearMade
        self.ogPrice = ogPrice
        self.operatingSystem = operatingSystem

    # What methods will you need?

    def updateOS(self, operatingSystem):
        if refurbish(): # refurbish method from oo_resale_shop.py
            if operatingSystem not in "old OS" or "older OS" or "oldest OS":
                operatingSystem = "the newest OS"
            else:
                print("Operating System already updated!")
        
    def deleteID(self, itemID):
        if sellComputer(): # sell method from oo_resale_shop.py
            del itemID