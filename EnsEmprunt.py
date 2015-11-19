import sqlite3


conn = sqlite3.connect("Ludotheque.db")
conn.execute('pragma foreign_keys = on')
conn.commit()
cur = conn.cursor()

def createTable():
        cur.execute("""CREATE TABLE IF NOT EXISTS EnsEmprunt(
                        emprunt_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                        user_id INTEGER,
                        jeu_id INTEGER,
                        date_emprunt STRING)""")
        conn.commit()

def destroyTable():
        cur.execute("""DROP TABLE EnsEmprunt""")
        conn.commit()
def emprunt_to_table(Emprunt):
		emprunt_table = (Emprunt.get_emprunt_id(), Emprunt.get_adherent(), Emprunt.get_jeu_id(), Emprunt.get_date_emprunt())
		return (emprunt_table)

def delete_emprunt(Emprunt):
        cur.execute("""DELETE FROM EnsEmprunt WHERE emprunt_id = ?""",(Emprunt.get_emprunt_id(),))
        conn.commit()

def insert_emprunt(Emprunt):
		cur.execute("""INSERT INTO EnsEmprunt(emprunt_id,user_id,jeu_id,date_emprunt) VALUES (?, ?, ?, ?)""",emprunt_to_table(Emprunt))
                        conn.commit()
