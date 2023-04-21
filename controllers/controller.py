from flask import render_template, request
from app import app
from models.catalogue import books
from models.book import Book

@app.route('/')
def index():
    return render_template('index.html',title="Home Page")

@app.route('/catalogue/')
def catalogue():
    return render_template('catalogue.html',title="Catalogue",books=books) 

@app.route('/catalogue/<index>')
def book_page(index):
    book = books[int(index)]
    return render_template('book.html',title=index,book=book)