import sqlite3

def connect_db():
    global sqlite_connection
    try:
        sqlite_connection = sqlite3.connect('translator.db')
        return sqlite_connection
    except sqlite3.Error as error:
        return error
