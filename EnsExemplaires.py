# -*- coding: utf-8 -*-
import sqlite3

from Exemplaire import Exemplaire
import EnsJeux


conn = sqlite3.connect("Ludotheque.db")
conn.execute('pragma foreign_keys = on')
conn.commit()
cur = conn.cursor()

def createTable():
        cur.execute("""CREATE TABLE IF NOT EXISTS EnsExemplaires(
                        Exemplaire_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                        Jeu_id INTEGER,
                        Est_disponible BOOLEAN)""")
        conn.commit()

def destroyTable():
        cur.execute("""DROP TABLE EnsExemplaires""")
        conn.commit()

def exemplaire_to_table(Exemplaire):
        # User -> List
        ExemplaireTable=(Exemplaire.get_Exemplaire_id(),Exemplaire.get_Jeu_id(),Exemplaire.get_Est_disponible())
        return ExemplaireTable

def get_Exemplaire_dispo(Jeu):
        cur.execute("""SELECT * FROM EnsExemplaires WHERE Jeu_id = ?""", (Jeu.get_Jeu_id()))
        result = cur.fetchone()
        return Exemplaire(EnsJeux.get_Jeu(result[1]),result[2],result[0])

def get_Exemplaire(exemplaire_id):
        cur.execute("""SELECT * FROM EnsExemplaires WHERE Exemplaire_id = ?""", (exemplaire_id,))
        result = cur.fetchone()
        return Exemplaire(EnsJeux.get_Jeu(result[1]),result[2],result[0])
        # Jeu => Est_Disponible => Exemplaire_id

def get_nombre_exemplaires(Jeu,disponible=2):
        # 1 Disponibles
        # 0 Indisponibles
        # 2 ALL

        if disponible==2:
                cur.execute("""SELECT COUNT(Exemplaire_id) FROM EnsExemplaires WHERE Jeu_id= ?""",(Jeu.get_Jeu_id(),))
                result = cur.fetchone()
                return result[0]
        elif disponible==1:
                cur.execute("""SELECT COUNT(Exemplaire_id) FROM EnsExemplaires WHERE Est_Disponible = 1 and Jeu_id= ?""",(Jeu.get_Jeu_id(),))
                result = cur.fetchone()
                return result[0]
        elif disponible==0:
                cur.execute("""SELECT COUNT(Exemplaire_id) FROM EnsExemplaires WHERE Est_Disponible = 0 and Jeu_id= ?""",(Jeu.get_Jeu_id(),))
                result = cur.fetchone()
                return result[0]





def insert(Exemplaire):

        # PRECONDITION: Jeu_id doit EXISTER ! (A FAIRE)
        #try:
        cur.execute("""INSERT INTO EnsExemplaires(Exemplaire_id,Jeu_id,Est_disponible) VALUES (?,?,?)""",(Exemplaire.get_Exemplaire_id(),Exemplaire.get_Jeu_Exemplaire().get_Jeu_id(),Exemplaire.get_Est_disponible(),))
        conn.commit()
        print("Exemplaire ajoute avec succes !")
        #except:

         #       print("Erreur lors de l'ajout de l'exemplaire")

def update(Exemplaire):
        cur.execute("""UPDATE EnsExemplaires SET Jeu_id = ?, Est_Disponible = ? WHERE Exemplaire_id=?""", (Exemplaire.get_Jeu_Exemplaire().get_Jeu_id(),Exemplaire.get_Est_disponible(),Exemplaire.get_Exemplaire_id()))
        conn.commit()
        print("Exemplaire modifie avec succes !")


def printAll():
        cur.execute("""SELECT * FROM EnsExemplaires""")
        rows = cur.fetchall()
        for row in rows:
                print('{0} : {1} => Dispo ? {2}'.format(row[0], EnsJeux.get_Jeu(row[1]).get_Nom_jeu(), row[2]))
