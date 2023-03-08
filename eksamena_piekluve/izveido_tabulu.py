import sqlite3

conn = sqlite3.connect('data.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS dati(
            darba_id INTEGER PRIMARY KEY,
            summa float,
            drops text,
            daudzums integer
            )""")
cur.execute("""CREATE TABLE IF NOT EXISTS darba_koef(
            id INTEGER PRIMARY KEY,
            saraksta_id INTEGER,
            drops text,
            koef_darbam float,
            FOREIGN KEY (saraksta_id) REFERENCES users(darba_id)
            )""")

conn.commit()
conn.close()