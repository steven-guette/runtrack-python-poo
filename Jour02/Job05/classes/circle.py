from math import pi

from classes.whiteshield import WShield
from classes.shape import Shape


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()

        self.__Radius = 0
        self.SetRadius(radius)

    # region SETTERS ################

    def SetRadius(self, radius):
        if WShield.IsNumeric(radius, 0):
            self.__Radius = radius

    # endregion #####################

    def GetRadius(self):
        return self.__Radius

    def GetDiameter(self):
        return self.__Radius * 2

    def GetArea(self):
        return self.GetDiameter() * pi
