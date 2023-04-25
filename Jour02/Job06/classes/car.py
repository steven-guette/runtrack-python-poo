from classes.vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, brand, model, year_old, price):
        super().__init__(brand, model, year_old, price)

        self.Doors = 4

    def VehicleInformation(self):
        print(
            "Marque = {}\nModèle = {}\nPortes = {}\nPrix = {}"
            .format(self.Brand, self.Model, self.Doors, self.OldYear, self.Price)
        )

    def Start(self):
        print("Je démarre ma voiture.")
