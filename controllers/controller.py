from flask import render_template, request
from app import app
from models.catalogue import books, add_book
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
        pass


@app.route('/catalogue/')
def catalogue():
    return render_template('catalogue.html',title="Catalogue",books=books) 

@app.route('/catalogue/<index>')
def book_page(index):
    book = books[int(index)]
    return render_template('book.html',title=index,book=book)

