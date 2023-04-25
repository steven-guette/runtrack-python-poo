from classes.whiteshield import WShield


class Person:
    def __init__(self):
        self._Age = 14

    # region METHODS ###########

    def DisplayAge(self):
        print(self._Age)

    def SayHello():
        print("Hello !")

    SayHello = staticmethod(SayHello)

    # endregion ################

    # region SETTERS ###########

    def SetAge(self, age):
        if WShield.IsInt(age, 0, 130):
            self._Age = age

    # endregion ################
