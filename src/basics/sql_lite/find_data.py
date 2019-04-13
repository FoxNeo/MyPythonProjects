import sqlite3

connection = sqlite3.connect("production.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM PERSON WHERE edad > 30")

selected_persons = cursor.fetchall()

for person in selected_persons:
    print(person)

connection.close()