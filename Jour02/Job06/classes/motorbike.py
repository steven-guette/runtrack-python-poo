from classes.vehicle import Vehicle


class Motorbike(Vehicle):
    def __init__(self, brand, model, old_year, price):
        super().__init__(brand, model, old_year, price)

        self.Wheels = 2

    def VehicleInformation(self):
        print(
            "Marque = {}\nModèle = {}\nRoues = {}\nPrix = {}"
            .format(self.Brand, self.Model, self.Wheels, self.OldYear, self.Price)
        )

    def Start(self):
        print("Je démarre ma moto.")
