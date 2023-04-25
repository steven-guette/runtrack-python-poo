from classes.whiteshield import WShield
from classes.rectangle import Rectangle


class Parallelepiped(Rectangle):
    def __init__(self, width, length, depth):
        super().__init__(width, length)

        self.__Depth = 0
        self.SetDepth(depth)

    # region GETTERS ################

    def GetDepth(self):
        return self.__Depth

    def GetVolume(self):
        return self.GetArea() * self.__Depth

    # endregion #####################

    # region SETTERS ################

    def SetDepth(self, depth):
        if WShield.IsNumeric(depth, 0):
            self.__Depth = depth

    # endregion #####################
