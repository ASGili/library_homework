from models.book import Book

book1 = Book("Gateway","Frederick Pohl","Science Fiction")
book2 = Book("The Shining","Stephen King","Horror")
book3 = Book("American Psycho","Bret Easton Ellis","Contemporary")

books = [book1,book2,book3]

def add_book(book):
    books.append(book)

def del_book(books_index):
   books.remove(books[books_index])

def check_out_book(books_index):
    if books[books_index].checked == False:
        books[books_index].checked = True
    else:
        books[books_index].checked = False