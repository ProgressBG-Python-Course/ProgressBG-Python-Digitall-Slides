import os
import sqlite3

DEFAULT_PATH = 'db/default.sqlite3')

def db_connect(db_path=DEFAULT_PATH):
    con = sqlite3.connect(db_path)
    return con