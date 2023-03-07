import sqlite3

def ievieto_darbu(garums,platums,drops,daudzums):
    conn = sqlite3.connect('data.db')
    conn.execute("""INSERT INTO dati (garums,platums,drops,daudzums)  VALUES(?,?,?,?);""",(garums,platums,drops,daudzums))
    conn.commit()
    conn.close()
