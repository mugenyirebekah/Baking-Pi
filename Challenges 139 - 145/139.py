import sqlite3

with sqlite3.connect("PhoneBook.db") as db:
    cursor = db.cursor()


cursor.execute("""CREATE TABLE IF NOT EXISTS Names(
               id integer PRIMARY KEY,
               firstname text,
               surname text,
               phonenumber text);""")

cursor.execute("""INSERT INTO Names(id,firstname,surname,phonenumber)
               VALUES("1","Simon","Howels","01223 349752")""")
db.commit()

cursor.execute("""INSERT INTO Names(id,firstname,surname,phonenumber)""")