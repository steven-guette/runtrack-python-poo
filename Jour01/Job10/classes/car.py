from datetime import date
from classes.whiteshield import WShield


class Car:
    CurrentYear = date.today().year
    FirstCarYear = 1789

    def __init__(self, brand, model, mileage, old_year):
        self.__Brand = brand
        self.__Model = model
        self.__Mileage = mileage
        self.__OldYear = old_year

        self.__Tank = 50
        self.__Running = False

    # region METHODS ############################

    def StartTheCar(self):
        if not self.__Running:
            if self.CheckTheFuel() > 5:
                self.__Running = True
                print(f"La {self.__Brand} {self.__Model} démarre, il reste {self.__Tank} litre de carburant.")
            else:
                print("Le tableau de bord indique que vous manquez de carburant.")
        else:
            print("La voiture est déjà en marche.")

    def StopTheCar(self):
        if self.__Running:
            self.__Running = False
            print(f"La {self.__Brand} {self.__Model} s'arrête, il reste {self.__Tank} litre de carburant.")
        else:
            print("La voiture est déjà à l'arrêt.")

    def CheckTheFuel(self):
        return self.__Tank

    # endregion #################################

    # region SETTERS ############################

    def SetBrand(self, brand):
        if WShield.IsString(brand):
            self.__Brand = brand

    def SetModel(self, model):
        if WShield.IsString(model):
            self.__Model = model

    def SetMileage(self, mileage):
        if WShield.IsNumeric(mileage, 0):
            self.__Mileage = mileage

    def SetOldYear(self, old_year):
        if WShield.IsInt(old_year, Car.FirstCarYear, Car.CurrentYear):
            self.__OldYear = old_year

    def SetTank(self, tank):
        if WShield.IsNumeric(tank, 0):
            self.__Tank = tank

    # endregion #################################

    # region GETTERS ############################

    def GetBrand(self):
        return self.__Brand

    def GetModel(self):
        return self.__Model

    def GetMileage(self):
        return self.__Mileage

    def GetOldYear(self):
        return self.__OldYear

    # endregion #################################
