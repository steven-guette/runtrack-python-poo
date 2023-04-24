from classes.book import Book

book = Book("Père riche, père pauvre", "Robert Kiyosaki", 320)

print("\nValeurs de base :\n")
print("Titre: {}\nAuteur: {}\nPages: {}\n".format(book.GetTitle(), book.GetAuthor(), book.GetPageNumber()))

book.SetTitle("Albert Einstein")
book.SetAuthor("La physique quantique")
book.SetPageNumber(560)

print("\nModification avec des données valides :\n")
print("Titre: {}\nAuteur: {}\nPages: {}\n".format(book.GetTitle(), book.GetAuthor(), book.GetPageNumber()))

print("\nModification avec des données invalides :\n")

book.SetTitle("")
book.SetAuthor("")
book.SetPageNumber("...")
book.SetPageNumber(-5)
