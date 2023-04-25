from classes.rectangle import Rectangle

rectangle = Rectangle(17, 42)

print(
    "\nLes attributs de mon rectangle :\nLa largeur = {} cm\nLa hauteur = {} cm"
    .format(rectangle.GetWidth(), rectangle.GetHeight())
)

print(f"\nSon aire est de {rectangle.GetArea()} cm²")
