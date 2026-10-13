class Book:
    def __init__(self,name, author):
        self.name = name
        self.author = author


class Library:
    def __init__(self):
        self.book = Book("кітап1", "автор")
    def lend_book(self):
        book = {"name" : self.book.name,"author" : self.book.author}
        return book
    def create_book(self, name, author):
        self.book = Book(name, author)

library = Library()
print(library.lend_book())
library.create_book("кітап2", "автор")
print(library.lend_book())
        
    