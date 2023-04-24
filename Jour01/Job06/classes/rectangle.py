class Rectangle:
    def __init__(self, width, length):
        self.__Width = width
        self.__Length = length

    # region SETTERS

    def SetWidth(self, width):
        self.__Width = width

    def SetLength(self, length):
        self.__Length = length

    # endregion

    # region GETTERS

    def GetWidth(self):
        return self.__Width

    def GetLength(self):
        return self.__Length

    # endregion
