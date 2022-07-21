import sqlite3
from .models import Author, Book, Rental
from app import db


def create_author(name, surname):
    #sql alchemy
    author = Author()
    author.name = name
    author.surname = surname
    db.session.add(author)
    db.session.commit()


def create_book(author_id, title):
    book = Book()
    book.author_id = author_id
    book.title = title
    db.session.add(book)
    db.session.commit()


def get_authors():
    return Author.query.all()

def get_books():
    return Book.query.all()

def rent_book(book_id):
    rental = Rental()
    rental.book_id = book_id
    db.session.add(rental)
    db.session.commit()
