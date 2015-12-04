#-*- coding:utf-8-*-
import sqlite3
from datetime import date, datetime
from Emprunt import Emprunt
from Utilisateur import Utilisateur
from Jeu import Jeu
from Exemplaire import Exemplaire

conn = sqlite3.connect("Ludotheque.db")
conn.execute('pragma foreign_keys = on')
conn.commit()
cur = conn.cursor()

#  Est-ce que l'emprunt est supprimé une fois qu'il est rendu ?
def createTable():
        cur.execute("""CREATE TABLE IF NOT EXISTS EnsEmprunt(
                        emprunt_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                        user_id INTEGER,
                        exemplaire_id INTEGER,
                        date_emprunt DATE,
                        date_echeance DATE)""")  #DATE est représenté comme : YYYY-MM-DD
        conn.commit()

def destroyTable():
        cur.execute("""DROP TABLE EnsEmprunt""")
        conn.commit()
def emprunt_to_table(Emprunt):
		emprunt_table = (Emprunt.get_User_id(), Emprunt.get_Exemplaire_id(), Emprunt.get_date_emprunt(), Emprunt.get_date_echeance())
		return emprunt_table

def delete_emprunt(Emprunt):
        cur.execute("""DELETE FROM EnsEmprunt WHERE emprunt_id = ?""",(Emprunt.get_emprunt_id(),))
        conn.commit()

def insert_emprunt(Emprunt):
        cur.execute("""INSERT INTO EnsEmprunt(user_id,jeu_id,date_emprunt,date_echeance) VALUES (?, ?, ?, ?)""",emprunt_to_table(Emprunt))
        conn.commit()

#  A modifier => Renvoyer des instances d'emprunts dans un tableau
def rechercher_emprunt (Emprunt_id):
        cur.execute("""SELECT * FROM EnsEmprunt WHERE emprunt_id = (?)""",(Emprunt_id,))
        res = cur.fetchone()
        return res


# ????
def rechercher_user(User):
        cur.execute("""SELECT * FROM EnsEmprunt WHERE user_id = ?""",(User.get_user_id()) )
        res = cur.fetchone()
        return res

# ????
def rechercher_jeu (Jeu_id):
        cur.execute("""SELECT * FROM EnsEmprunt WHERE jeu_id = Jeu_id""")
        res = cur.fetchall()
        return res

#  A modifier => Renvoyer des instances d'emprunts dans un tableau
def rechercher_date_emprunt (Date_emprunt):
        cur.execute("""SELECT * FROM EnsEmprunt WHERE date_emprunt = Date_emprunt""")
        res = cur.fetchall()
        return res

def rechercher_date_echeance (Date_echeance):
        cur.execute("""SELECT * FROM EnsEmprunt WHERE date_echeance = Date_echeance""" )
        res = cur.fetchall()
        return res

def printAll():
        cur.execute("""SELECT * FROM EnsEmprunt""")
        rows = cur.fetchall()
        return rows
        #for row in rows:
                #print('{0} : {1} - {2}'.format(row[0], row[1], row[2]))
"""
date = str( year + "-"+month+"-"+day);
date = date (date)
"""
