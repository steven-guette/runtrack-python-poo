from classes.personne import Personne


namesList = [
    "cédric prunier", "benoit bremaud",
    "stéphanie fernandes", "léa guette",
    "matteo duval", "saber ayadi"
]
Person = list()

for name in namesList:
    n = name.split(" ", 2)
    Person.append(Personne(n[1].capitalize(), n[0].capitalize()))

for p in Person:
    p.SePresenter()
