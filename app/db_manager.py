import sqlite3
from .models import Author, Book
from app import db


def create_author(name):
    #sql alchemy
    author = Author()
    author.name = name
    db.session.commit()


def create_book(author_id, title):
    book = Book()
    book.author_id = author_id
    book.title = title
    db.session.commit()


def get_authors():
    return Author.query.all()

def get_books():
    return Book.query.all()