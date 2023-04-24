class Book:
    def __init__(self, title, author, page_number):
        self.__Title = title
        self.__Author = author
        self.__PageNumber = page_number

    # region SETTERS

    def SetTitle(self, title):
        if len(title) > 0:
            self.__Title = title
        else:
            print("Vous essayez de modifier le titre du livre par une chaine vide !")

    def SetAuthor(self, author):
        if len(author) > 0:
            self.__Author = author
        else:
            print("Vous essayez de modifier le nom de l'auteur du livre par une chaine vide !")

    def SetPageNumber(self, page_number):
        if not isinstance(page_number, int):
            try:
                page_number = int(page_number)
            except:
                print("Veuillez indiquer un nombre entier pour modifier le nombre de pages du livre.")
                return False

        if page_number > 0:
            self.__PageNumber = page_number
        else:
            print("Vous essayez de modifier le nombre de pages du livre par un nombre inférieur ou égal à zéro !")

    # endregion

    # region GETTERS

    def GetTitle(self):
        return self.__Title

    def GetAuthor(self):
        return self.__Author

    def GetPageNumber(self):
        return self.__PageNumber

    # endregion
