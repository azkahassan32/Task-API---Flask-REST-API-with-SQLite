import sqlite3 #Imports Python’s built-in SQLite library. SQLite is serverless, meaning the database is just a file on your disk.

def get_db_connection():                    #Defines a function that returns a connection to the DB
    conn = sqlite3.connect("tasks.db")      #Opens or creates a database file tasks.db
    conn.row_factory = sqlite3.Row          #Makes query results dictionary-like, so you can do task["title"] instead of task[1]
    return conn                             #Returns the connection object so other functions can use it
