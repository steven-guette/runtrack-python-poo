from classes.game import Game
from classes.player import Player
import includes.functions as func


playAgain = True

CardGame = Game()
Bank = Player()
User = Player()

User.AddCard(CardGame.GetCard())
Bank.AddCard(CardGame.GetCard())

while playAgain:
    func.ClearTerminal()
    User.AddCard(CardGame.GetCard())

    print("\nJeu de la banque :")
    Bank.DisplayYourGame()

    print("\nTon jeu :")
    User.DisplayYourGame()

    if Game.ExceedLimit(User.GetScore()):
        print("\nVotre score est trop élevé, vous avez perdu !")
        playAgain = False
    else:
        again = input("\nVoulez vous tirer une carte ? ")

        if again.lower() == "non":
            func.ClearTerminal()

            while Game.BankDraw(Bank.GetScore()):
                Bank.AddCard(CardGame.GetCard())

            print("\nJeu de la banque :")
            Bank.DisplayYourGame()

            print("\nTon jeu :")
            User.DisplayYourGame()

            if Game.ExceedLimit(Bank.GetScore()) or Bank.GetScore() < User.GetScore():
                print("\nLa banque saute, félicitations !")
            elif Bank.GetScore() == User.GetScore():
                print("\nMatch nul !")
            else:
                print("\nLa banque gagne !")

            playAgain = False
