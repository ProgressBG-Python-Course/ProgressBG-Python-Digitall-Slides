import db
import json
import pandas as pd
import sqlite3
from pprint import pprint


db_path = "db/test.sqlite3"
con = db.connect(db_path)
db.create_tables(con)
# show_tables(con)


tableA = json.load(open('db/tableA.json'))
db.insert(con, "tableA",tableA)

tableB = json.load(open('db/tableB.json'))
db.insert(con, "tableB",tableB)

dfA = pd.read_sql_query("select * from tableA limit 10;", con)
dfB = pd.read_sql_query("select * from tableB limit 10;", con)
### to debug
# print(dfA.dtypes)
# print(dfB.dtypes)


tableA_B = dfA.join(dfB,on='tac',how="left", lsuffix='_caller', rsuffix='_other')
tableA_B.to_csv("tableA_B.csv")






