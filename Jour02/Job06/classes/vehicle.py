class Vehicle:
    def __init__(self, brand, model, old_year, price):
        self.Brand = brand
        self.Model = model
        self.OldYear = old_year
        self.Price = price

    # region METHODS ######################

    def VehicleInformation(self):
        print(f"{self.Brand} {self.Model} manufacturé en {self.OldYear} et acheté {self.Price}€")

    def Start(self):
        print("Attention, je roule.")

    # endregion ###########################

