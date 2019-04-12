import sqlite3

connection = sqlite3.connect("production.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM PERSON")

loaded_persons = cursor.fetchall()

for person in loaded_persons:
    print(person)

connection.close()