# SQLLite
# download SQL Lite browser to open the db file
import sqlite3

connection = sqlite3.connect("production.db")

connection.close()