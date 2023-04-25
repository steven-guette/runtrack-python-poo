from classes.whiteshield import WShield
from classes.shape import Shape

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()

        self.__Width = 0
        self.__Height = 0

        self.SetWidth(width)
        self.SetHeight(height)

    # region SETTERS ###############

    def SetWidth(self, width):
        if WShield.IsNumeric(width, 0):
            self.__Width = width

    def SetHeight(self, height):
        if WShield.IsNumeric(height, 0):
            self.__Height = height

    # endregion ####################

    # region GETTERS ###############

    def GetWidth(self):
        return self.__Width

    def GetHeight(self):
        return self.__Height

    def GetArea(self):
        return self.__Height * self.__Width

    # endregion ####################
