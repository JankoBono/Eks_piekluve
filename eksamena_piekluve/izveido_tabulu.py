import sqlite3

conn = sqlite3.connect('data.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE dati(
            garums integer,
            platums integer,
            drops text,
            daudzums integer
            )""")
conn.commit()
conn.close()