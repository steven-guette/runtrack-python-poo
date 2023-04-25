class Card:
    def __init__(self, value, color):
        self.__Value = value
        self.__Color = color

    # region GETTERS ##################

    def GetValue(self):
        return self.__Value

    def GetColor(self):
        return self.__Color

    # endregion #######################
