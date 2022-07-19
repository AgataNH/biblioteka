from flask import Flask
import sqlite3
from sqlite3 import Error

app = Flask(__name__)

db_file = "biblioteka.db"

def create_connection(db_file):
   """ create a database connection to the SQLite database
       specified by db_file
   :param db_file: database file
   :return: Connection object or None
   """
   conn = None
   try:
       conn = sqlite3.connect(db_file)
       return conn
   except Error as e:
       print(e)

   return conn

def select_all(conn, table):
   """
   Query all rows in the table
   :param conn: the Connection object
   :return:
   """
   cur = conn.cursor()
   cur.execute(f"SELECT * FROM {table}")
   rows = cur.fetchall()

   return rows

@app.route('/')
def homepage():
    hello = "To jest moja biblioteka"
    return f"{hello}"

@app.route('/books')
def books():
    print("to są moje książki")
    conn = create_connection("db_file")
    return select_all(conn, "book")

@app.route('/authors')
def authors():
    print("autorzy w mojej bilbiotece:")
    conn = create_connection("db_file")
    return select_all(conn, "author")

@app.route('/rentals')
def rentals():
    print("wyporzyczenia w mojej bilbiotece:")
    conn = create_connection("db_file")
    return select_all(conn, "rental")

if __name__ == "__main__":
    app.run(debug=True)

