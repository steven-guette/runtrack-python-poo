from random import randint
from classes.student import Student

students = list()
studentsList = [
    {"name": "prunier",     "firstname": "cédric",      "cardID": randint(100, 10000)},
    {"name": "bremaud",     "firstname": "benoit",      "cardID": randint(100, 10000)},
    {"name": "ayadi",       "firstname": "saber",       "cardID": randint(100, 10000)},
    {"name": "fernandes",   "firstname": "stéphanie",   "cardID": randint(100, 10000)},
    {"name": "guette",      "firstname": "léa",         "cardID": randint(100, 10000)},
    {"name": "duval",       "firstname": "matteo",      "cardID": randint(100, 10000)},
    {"name": "frigo",       "firstname": "marie",       "cardID": randint(100, 10000)},
    {"name": "jacquin",     "firstname": "dylan",       "cardID": randint(100, 10000)}
]

student = Student("Doe", "John", 145)

for i in range(3):
    student.SetCredits(10)

print("\nAjout de crédits :")
student.DisplayCredits()

print("\nInformations sur l'étudiant :")
student.StudentInfo()

print("\nAller plus loin :\n")

for student in studentsList:
    s = Student(student["name"].capitalize(), student["firstname"].capitalize(), student["cardID"])

    for i in range(3):
        s.SetCredits(randint(15, 33))

    students.append(s)

for student in students:
    student.DisplayCredits()
    student.StudentInfo()
    print("\n--------------------------------\n")
