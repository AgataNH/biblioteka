from flask import Flask, request, url_for, redirect, jsonify, Response
import sqlite3
from sqlite3 import Error

from app import app, db_manager


@app.route("/create/author", methods=["POST"])
def create_author():
    data = request.json
    db_manager.create_author(data["name"], data["surname"])
    return Response(status=201)


@app.route("/list/author", methods=["GET"])
def list_author():
    result = []
    db_authors = db_manager.get_authors()
    for author in db_authors:
        result.append(
            {
                "id": author.id,
                "name": author.name,
                "surname": author.surname
            }
        )
    return jsonify(result)

@app.route("/create/book", methods=["POST"])
def create_book():
    data = request.json
    db_manager.create_book(data["author_id"], data["title"])
    return Response(status=201)

@app.route("/list/books", methods=["GET"])
def list_books():
    result = []
    db_books = db_manager.get_books()
    for book in db_books:
        result.append(
            {
                "id": book.id,
                "title": book.title,
                "author": f"{book.author.name} {book.author.surname}",
                "rentals_date": book.rentals[0].rental_date if book.rentals else "-"
            }
        )
    return jsonify(result)

@app.route("/rent/<book_id>", methods=["GET"])
def rent_book(book_id):
    db_manager.rent_book(book_id)
    return Response(status=201)


