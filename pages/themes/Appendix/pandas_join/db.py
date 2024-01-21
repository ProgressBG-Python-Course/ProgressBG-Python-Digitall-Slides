import os
import sqlite3
import csv

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), '/db/database.sqlite3')

def connect(db_path=DEFAULT_PATH):
  con = sqlite3.connect(db_path)
  return con

def create_tables(con):
  c = con.cursor()

  tableA = """
  CREATE TABLE IF NOT EXISTS tableA (
      -- id integer PRIMARY KEY,
      a1 integer NOT NULL,
      a2 integer NOT NULL,
      tac integer)"""
  c.execute(tableA)

  tableB = """
  CREATE TABLE IF NOT EXISTS tableB  (
      -- id integer PRIMARY KEY,
      btac integer,
      b1 integer,
      b2 integer)"""
  c.execute(tableB)

def show_tables(con):
  c = con.cursor()
  c.execute("SELECT name FROM sqlite_master WHERE type='table'")
  print(c.fetchall())

def insert(con, table,data):
  """insert_row(con, table,data)

  Args:
      con (TYPE): Description
      table (TYPE): Description
      data (TYPE): Description
  """
  cur = con.cursor()

  for row in data:
    keys = tuple(row.keys())
    values = tuple(row.values())

    sql = "INSERT INTO {} {} VALUES {}".format(table, keys, values)
    print("SQL: ", sql)
    cur.execute(sql)

def show_table(con, table):
  cur = con.cursor()
  cur.execute("SELECT * FROM " + table)
  data = cur.fetchall()

  print(data)

def db_to_csv(con, file):
  csvWriter = csv.writer(open(file, "w"))

  rows = con.fetchall()
  csvWriter.writerows(rows)

