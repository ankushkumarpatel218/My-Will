import sqlite3 as sql

con = sql.connect('Library Management System/Library.db')
cur = con.cursor()

con.close()