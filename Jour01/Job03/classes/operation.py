class Operation:
    def __init__(self):
        self.nombre1 = 10
        self.nombre2 = 2

    def DisplayNumbers(self):
        print(f"Le nombre1 est : {self.nombre1}\nLe nombre2 est : {self.nombre2}")

    def Addition(self):
        print("Résultat de l'addition : {}".format((self.nombre1 + self.nombre2)))
