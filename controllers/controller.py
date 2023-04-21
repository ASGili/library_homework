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