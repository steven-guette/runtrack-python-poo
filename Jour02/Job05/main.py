from classes.rectangle import Rectangle
from classes.circle import Circle


rectangle = Rectangle(7, 23)
circle = Circle(9)

print(
    "\nMon rectangle :\nSa largeur = {} cm\nSa longueur = {} cm\nSon aire = {} cm²"
    .format(rectangle.GetWidth(), rectangle.GetHeight(), rectangle.GetArea())
)

print("\n-----------------------------------------\n")

print(
    "Mon cercle :\nSon rayon = {} cm\nSon diamètre = {} cm\nSon aire = {} cm²"
    .format(circle.GetRadius(), circle.GetDiameter(), circle.GetArea())
)
