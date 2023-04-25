from classes.car import Car
from classes.motorbike import Motorbike

car = Car("Renault", "Scénic", 2009, 3400)
bike = Motorbike("Yamaha", "1200 Vmax", 1987, 4500)

print("\nMa voiture :")
car.VehicleInformation()
car.Start()

print("\n-----------------------------------------------\n\nMa moto :")
bike.VehicleInformation()
bike.Start()
