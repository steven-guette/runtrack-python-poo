from classes.person import Person


class Student(Person):
    def __init__(self):
        super().__init__()

    # region METHODS ################

    def DisplayAge(self):
        if self._Age > 1:
            print(f"J'ai {self._Age} ans.")
        else:
            print(f"J'ai {self._Age} an.")

    def GoToClass():
        print("Je vais en cours.")

    GoToClass = staticmethod(GoToClass)

    # endregion #####################
