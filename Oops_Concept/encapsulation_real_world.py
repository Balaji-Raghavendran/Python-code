class library:
    def __init__(self):
        self.__book = []

    def add_books(self,books):
        self.__book.append(books)
        print("the book",books,"is added")

    def remove_book(self,books):
        if books in self.__book:
            self.__book.remove(books)
            print("the book",books,"is removed ")
        else:
            print("book unavailable")
    
    def view_books(self):
        print("the books are:",self.__book)


Library = library()
Library.add_books("scarface")
Library.add_books("Godfather")
Library.add_books("Shawshank Redemption")
Library.add_books("San Andreas")

Library.view_books()

Library.remove_book("San Andreas")
Library.view_books()

        
    

