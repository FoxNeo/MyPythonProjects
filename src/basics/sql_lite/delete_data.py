import sqlite3

connect = sqlite3.connect("production.db")

cursor = connect.cursor()

cursor.execute("DELETE FROM PERSON WHERE apellido = 'Duck'")

connect.commit()
connect.close()