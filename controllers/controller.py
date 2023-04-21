from flask import render_template, request
from app import app
from models.catalogue import books, add_book, del_book
from models.book import Book

@app.route('/')
def index():
    return render_template('index.html',title="Home Page")

@app.route('/', methods=['POST'])
def adddel_book():
    if request.form['submit'] == "Add Book":
        book_title = request.form['title']
        book_author = request.form['author']
        book_genre = request.form['genre']
        new_book = Book(book_title,book_author,book_genre)
        add_book(new_book)
        return index()
    elif request.form['submit'] == "Delete Book":
        # book_title = str(request.form['title'])
        # book_author = str(request.form['author'])
        # book_genre = str(request.form['genre'])
        # new_book = Book(book_title,book_author,book_genre)
        # del_book(new_book)
        return index()
    else:
        return index()

@app.route('/catalogue/')
def catalogue():
    return render_template('catalogue.html',title="Catalogue",books=books) 

@app.route('/catalogue/<index>')
def book_page(index):
    book = books[int(index)]
    return render_template('book.html',title=index,book=book)

