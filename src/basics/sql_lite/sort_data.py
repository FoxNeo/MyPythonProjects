import sqlite3

connection = sqlite3.connect("production.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM PERSON ORDER BY edad")

orderData = cursor.fetchall()

for person in orderData:
    print(person)

connection.close()