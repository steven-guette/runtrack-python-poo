from classes.rectangle import Rectangle
from classes.parallelepiped import Parallelepiped


rectangle = Rectangle(13, 25)
parallelepiped = Parallelepiped(18, 37, 9)

print(
    "\nAttributs du Rectangle :\nLargeur = {} cm ; Longueur = {} cm"
    .format(rectangle.GetWidth(), rectangle.GetLength())
)

print(
    "\nSon périmètre : {}cm\nSon aire : {} cm²"
    .format(rectangle.GetPerimeter(), rectangle.GetArea())
)

print("\n----------------------------------------")

print(
    "\nAttributs du Parallélépipède :\nLargeur = {} cm ; Longueur = {} cm ; Profondeur = {} cm"
    .format(parallelepiped.GetWidth(), parallelepiped.GetLength(), parallelepiped.GetDepth())
)

print(
    "\nSon périmètre : {} cm\nSon aire : {} cm²\nSon volume : {} cm³"
    .format(parallelepiped.GetPerimeter(), parallelepiped.GetArea(), parallelepiped.GetVolume())
)
