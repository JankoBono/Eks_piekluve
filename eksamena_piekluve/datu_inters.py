import sqlite3

def ievieto_darbu(darba_id,summa,drops,daudzums):
    conn = sqlite3.connect('data.db')
    conn.execute("""INSERT INTO dati (darba_id,summa,drops,daudzums)  VALUES(?,?,?,?);""",(darba_id, summa,drops,daudzums))
    conn.commit()
    conn.close()
def parbaude():
    results = []
    conn = sqlite3.connect('data.db')
    cursor = conn.execute("SELECT * from dati")
    # Contact records are tuples and need to be converted into an array
    for row in cursor:
        results.append(list(row))
    return results
def izdzest_darbu(darba_id):
    conn = sqlite3.connect('data.db')
    conn.execute("DELETE from dati where darba_id = ?",(darba_id))
    conn.close()