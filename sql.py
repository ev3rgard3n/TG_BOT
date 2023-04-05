import sqlite3

db = sqlite3.connect('promocode.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS netflix (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   promocode TEXT
) """)
db.commit()
sql.execute("""CREATE TABLE IF NOT EXISTS yandex (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   promocode TEXT
) """)
db.commit()
