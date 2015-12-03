import sqlite3
from datetime import date, datetime


conn = sqlite3.connect("Ludotheque.db")
conn.execute('pragma foreign_keys = on')
conn.commit()
cur = conn.cursor()

def createTable():
        cur.execute("""CREATE TABLE IF NOT EXISTS EnsEmprunt(
                        emprunt_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                        user_id INTEGER,
                        jeu_id INTEGER,
                        date_emprunt DATE,
                        date_echeance DATE)""")  #DATE est représenté comme : YYYY-MM-DD
        conn.commit()

def destroyTable():
        cur.execute("""DROP TABLE EnsEmprunt""")
        conn.commit()
def emprunt_to_table(self, Emprunt):
		emprunt_table = (Emprunt.get_emprunt_id(), Emprunt.get_adherent_id(), Emprunt.get_jeu_id(), Emprunt.get_date_emprunt())
		return (emprunt_table)

def delete_emprunt(self, Emprunt):
        cur.execute("""DELETE FROM EnsEmprunt WHERE emprunt_id = ?""",(Emprunt.get_emprunt_id(),))
        conn.commit()

def insert_emprunt(self, Emprunt):
	cur.execute("""INSERT INTO EnsEmprunt(emprunt_id,user_id,jeu_id,date_emprunt) VALUES (?, ?, ?, ?)""",emprunt_to_table(Emprunt))
        conn.commit()

def rechercher_emprunt (self, Emprunt_id):
        cur.execute("""SELECT * FROM EnsEmprunt WHERE emprunt_id = Emprunt_id""")
        res = cur.fetchone()
        return res

def rechercher_user (self, User_id):
        cur.execute("""SELECT * FROM EnsEmprunt WHERE user_id = User_id""" )
        res = cur.fetchone()
        return res

def rechercher_jeu (self, Jeu_id):
        cur.execute("""SELECT * FROM EnsEmprunt WHERE jeu_id = Jeu_id""")
        res = cur.fetchall()
        return res

def rechercher_date_emprunt (self, Date_emprunt):
        cur.execute("""SELECT * FROM EnsEmprunt WHERE date_emprunt = Date_emprunt""")
        res = cur.fetchall()
        return res

def rechercher_date_echeance (self, Date_echeance):
        cur.execute("""SELECT * FROM EnsEmprunt WHERE date_echeance = Date_echeance""" )
        res = cur.fetchall()
        return res


"""
date = str( year + "-"+month+"-"+day);
date = date (date)
"""