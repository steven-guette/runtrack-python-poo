from random import randint
from classes.card import Card


class Game:
    CardColors = ["pique", "trèfle", "carreau", "coeur"]
    CardValues = []

    def __init__(self):
        self.__Cards = []

        self.__SetCardValues()
        self.__SetCards()

    # region METHODS ##################

    def BankDraw(score):
        return score <= 16

    BankDraw = staticmethod(BankDraw)

    def ExceedLimit(score):
        return score > 21

    ExceedLimit = staticmethod(ExceedLimit)

    # endregion #######################

    # region GETTERS ##################

    def GetCard(self):
        rand = randint(0, len(self.__Cards)-1)
        card = self.__Cards[rand]
        self.__Cards.pop(rand)

        return card

    # endregion #######################

    # region SETTERS ##################

    def __SetCards(self):
        for color in Game.CardColors:
            for value in Game.CardValues:
                self.__Cards.append(Card(value, color))

    def __SetCardValues(cls):
        for i in range(10):
            if i < 2:
                continue

            Game.CardValues.append(i)

        Game.CardValues.append("Valet")
        Game.CardValues.append("Dame")
        Game.CardValues.append("Roi")
        Game.CardValues.append("As")

    __SetCardValues = classmethod(__SetCardValues)

    # endregion #######################
