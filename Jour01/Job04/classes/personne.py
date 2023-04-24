class Personne:
    def __init__(self, name, firstname):
        self.Name = name
        self.Firstname = firstname

    def GetFullName(self):
        return f"{self.Firstname} {self.Name}"

    def SePresenter(self):
        print("Je suis {}".format(self.GetFullName()))
