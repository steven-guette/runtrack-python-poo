from classes.rectangle import Rectangle

r = Rectangle(5, 10)

print("\nLargeur initiale : {}".format(r.GetWidth()))
print("Longueur initiale : {}\n".format(r.GetLength()))

r.SetWidth(7)
r.SetLength(3)

print("Largeur finale : {}".format(r.GetWidth()))
print("Longueur finale : {}\n".format(r.GetLength()))
