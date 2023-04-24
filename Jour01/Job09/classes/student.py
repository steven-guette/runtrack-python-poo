class Student:
    def __init__(self, name, firstname, card_id):
        self.__Name = name
        self.__Firstname = firstname
        self.__CardID = card_id
        self.__Credits = 0
        self.__Level = ""

    # region METHODS

    def DisplayCredits(self):
        print(f"Le nombre de crédits de {self.__Firstname} {self.__Name} est de {self.__Credits} points.")

    def StudentInfo(self):
        self.__SetLevel()

        print(
            "Nom = {}\nPrénom = {}\nIdentifiant = {}\nNiveau = {}"
            .format(self.__Name, self.__Firstname, self.__CardID, self.__Level)
        )

    def __StudentEval(self):
        if self.__Credits >= 90:
            return "Excellent"
        elif self.__Credits >= 80:
            return "Très bien"
        elif self.__Credits >= 70:
            return "Bien"
        elif self.__Credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    # endregion

    # region SETTERS

    def SetCredits(self, add):
        if (isinstance(add, int) or isinstance(add, float)) and add > 0:
            self.__Credits += add

    def __SetLevel(self):
        self.__Level = self.__StudentEval()

    # endregion
