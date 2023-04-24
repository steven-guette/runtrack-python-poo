class Animal:
    def __init__(self):
        self.Name = ""
        self.Age = 0

    def MakeOld(self):
        self.Age += 1

    def SetName(self, name):
        self.Name = name
