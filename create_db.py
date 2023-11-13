import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password"
)

my_cursor = mydb.cursor()

my_cursor.execute("CREATE DATABASE sql")

my_cursor.execute("SHOW DATABASE")
databases = my_cursor.fetchall()
for db in my_cursor:
    print(db)