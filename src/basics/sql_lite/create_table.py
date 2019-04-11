import sqlite3

connection = sqlite3.connect("production.db")

cursor = connection.cursor()

cursor.execute("CREATE TABLE PERSON (nombre TEXT, apellido TEXT, edad INTEGER)")
connection.commit()
connection.close()