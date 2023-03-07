import sqlite3

conn = sqlite3.connect('data.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE dati(
            darba_id INTEGER PRIMARY KEY AUTOINCREMENT,
            summa float,
            drops text,
            daudzums integer
            )""")

conn.commit()
conn.close()