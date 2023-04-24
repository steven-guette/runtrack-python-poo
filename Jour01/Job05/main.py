from classes.animal import Animal


a = Animal()

txt = f"L'âge de l'animal : {a.Age} ans.\n\n"
a.MakeOld()

txt += "# Age de l'animal après l'appel de la méthode vieillir\n"
txt += f"L'âge de l'animal : {a.Age} ans.\n"

print(txt)

a.SetName("Cléa")

print(f"L'animal se nomme {a.Name}.")
