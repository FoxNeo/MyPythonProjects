import sqlite3

connection = sqlite3.connect("production.db")

cursor = connection.cursor()

lista_personas = [('Bugs', 'Bunny', 75), ('Lola', 'Bunny', 23), ('Duffy', 'Duck', 74)]

cursor.executemany("INSERT INTO PERSON VALUES (?,?,?)", lista_personas)

connection.commit()
connection.close()