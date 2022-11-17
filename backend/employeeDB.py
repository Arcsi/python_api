import sqlite3

con = sqlite3.connect("cars.db")
print("Database opened successfully")

con.execute(
    "create table Cars (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, address TEXT NOT NULL, number TEXT NOT NULL, country TEXT NOT NULL)")

print("Table created successfully")

con.close()