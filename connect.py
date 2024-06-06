import sqlite3
from contextlib import contextmanager


database = 'university_db.sqlite'

@contextmanager
def connect_database(database):
    conn = sqlite3.connect(database)
    yield conn
    conn.rollback()
    conn.close()