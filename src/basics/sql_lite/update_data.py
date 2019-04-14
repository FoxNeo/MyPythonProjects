import sqlite3

connect = sqlite3.connect("production.db")
cursor = connect.cursor()
cursor.execute("UPDATE PERSON SET edad = 19 WHERE nombre = 'Conker'")
connect.commit()
connect.close()
