from classes.book import Book

book = Book("Père riche, père pauvre", "Robert Kiyosaki", 320)

print("\nEmprunt du livre disponible :")
book.Borrow()

print("\nNouvel emprunt :")
book.Borrow()

print("\nRestitution du livre :")
book.Return()

print("\nNouvelle restitution :")
book.Return()

print("\nNouvel emprunt :")
book.Borrow()

print("\nNouvelle restitution :")
book.Return()


