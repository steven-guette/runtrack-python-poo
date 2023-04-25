from classes.whiteshield import WShield


class Rectangle:
    def __init__(self, width, length):
        self.__Width = 0
        self.__Length = 0

        self.SetWidth(width)
        self.SetLength(length)

    # region SETTERS ################

    def SetWidth(self, width):
        if WShield.IsNumeric(width, 0):
            self.__Width = width

    def SetLength(self, length):
        if WShield.IsNumeric(length, 0):
            self.__Length = length

    # endregion #####################

    # region GETTERS ################

    def GetWidth(self):
        return self.__Width

    def GetLength(self):
        return self.__Length

    def GetPerimeter(self):
        return sum(((self.__Width * 2), (self.__Length * 2)))

    def GetArea(self):
        return self.__Width * self.__Length

    # endregion #####################
