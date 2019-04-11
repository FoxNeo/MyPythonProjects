import sqlite3

connection = sqlite3.connect("production.db")

cursor = connection.cursor()

cursor.execute("INSERT INTO PERSON VALUES ('Conker', 'Squirrel', 18)")

connection.commit()

connection.close()