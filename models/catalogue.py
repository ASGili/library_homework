from models.book import Book

book1 = Book("Gateway","Frederick Pohl","Science Fiction")
book2 = Book("The Shining","Stephen King","Horror")
book3 = Book("American Psycho","Bret Easton Ellis","Contemporary")

books = [book1,book2,book3]

def add_book(book):
    books.append(book)

def del_book(book):
    books.remove(book)