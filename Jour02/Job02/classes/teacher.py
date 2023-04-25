from classes.person import Person


class Teacher(Person):
    def __init__(self):
        super().__init__()
        self.__TaughtSubject = "Python"

    # region METHODS ################

    def Teach():
        print("Le cours va commencer.")

    Teach = staticmethod(Teach)

    # endregion #####################
