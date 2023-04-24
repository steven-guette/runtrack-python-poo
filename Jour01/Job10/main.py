from classes.car import Car

car = Car("Peugeot", "307", 123000.37, 2002)

print("\nModèle d'origine :")
print(
    "Une {} {} qui possède {} kilomètre au compteur et a été fabriquée en {}."
    .format(car.GetBrand(), car.GetModel(), car.GetMileage(), car.GetOldYear())
)

car.SetBrand("Renault")
car.SetModel("5 Sport")
car.SetMileage(203189.872)
car.SetOldYear(1986)

print("\nNouveau modèle modifié à l'aide des méthodes :")
print(
    "Une {} {} qui possède {} kilomètre au compteur et a été fabriquée en {}."
    .format(car.GetBrand(), car.GetModel(), car.GetMileage(), car.GetOldYear())
)

print("\nDémarrage du véhicule :")
car.StartTheCar()

car.SetTank(43.79)

print("\nExtinction du véhicule :")
car.StopTheCar()
