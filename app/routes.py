from flask import Flask, request, url_for, redirect, jsonify
import sqlite3
from sqlite3 import Error

from app import app, db_manager


@app.route("/create/author", methods=["POST"])
def create_author():
    data = request.json
    db_manager.create_author(data["name"], data["surname"])
    return redirect(url_for("homepage"))


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
    return redirect(url_for("homepage"))

@app.route("/list/books", methods=["GET"])
def list_books():
    result = []
    db_books = db_manager.get_books()
    for book in db_books:
        result.append(
            {
                "id": book.id,
                "title": book.title,
                "author_id": book.author_id
            }
        )
    return jsonify(result)

@app.route("/rent/<book_id>", methods=["POST"])
def rent_book():
    data = request.json
    db_manager.rent_book(data["book_id"], data["rental_date"])
    return redirect(url_for("homepage"))

@app.route('/')
def homepage():
    hello = "To jest moja biblioteka"
    return f"{hello}"

