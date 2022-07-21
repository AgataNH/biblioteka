from datetime import datetime
from app import db

class Author(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(100), index=True, unique=True)
   surname = db.Column(db.String(200), index=True, unique=True)
   books = db.relationship("Book", backref="author")

   def __str__(self):
       return f"<Author {self.username}>"

class Book(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(200), index=True, unique=True)
   author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
   rentals = db.relationship("Rental", backref="book")

   def __str__(self):
       return f"<Book {self.id} {self.title}>"

class Rental(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   rental_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
   return_date = db.Column(db.DateTime, index=True)   
   book_id = db.Column(db.Integer, db.ForeignKey('book.id'))

   def __str__(self):
       return f"<Rental {self.id} {self.rental_date} {self.return_date}>"