from classes.whiteshield import WShield
from classes.card import Card


class Player:
    def __init__(self):
        self.__Cards = []
        self.__Score = 0

    # region METHODS ##################

    def AddCard(self, card):
        if isinstance(card, Card):
            self.__Cards.append(card)
            self.SetScore(card.GetValue())

    def DisplayYourGame(self):
        for card in self.__Cards:
            print(f"[{card.GetValue()} de {card.GetColor()}]")

        print(f"Score total = {self.__Score} points.")

    # endregion #######################

    # region GETTERS ##################

    def GetCards(self):
        return self.__Cards

    def GetScore(self):
        return self.__Score

    # endregion #######################

    # region SETTERS ##################

    def SetScore(self, newValue):
        if WShield.IsString(newValue):
            if newValue == "As":
                if (self.__Score + 11) > 21:
                    self.__Score += 1
                else:
                    self.__Score += 11
            else:
                self.__Score += 10
        else:
            self.__Score += newValue

    # endregion #######################
