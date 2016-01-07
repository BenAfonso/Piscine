#-*- coding:utf-8-*-
import sqlite3
from datetime import date, datetime
from Emprunt import Emprunt

from Jeu import Jeu
from Exemplaire import Exemplaire
import EnsUtilisateurs
import EnsExemplaires
conn = sqlite3.connect("Ludotheque.db")
conn.execute('pragma foreign_keys = on')
conn.commit()
cur = conn.cursor()


# A RAJOUTER : Fonction d'update dans la base avec test si ID != None Sinon faut Insert
# Fonction: save() Qui va rediriger la requête vers Insert ou Update en fonction de si l'id existes
# Fonction: update_emprunt() Qui Met à jours un emprunt dans la base

#  Est-ce que l'emprunt est supprimé une fois qu'il est date_rendu ?


def createTable():
    # Rajouter extension id: Pour les tests, tester si empruntEncours.extension_id = None ou si emprunt.jeu = none
        cur.execute("""CREATE TABLE IF NOT EXISTS EnsEmprunt(
                        emprunt_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                        user_id INTEGER,
                        exemplaire_id INTEGER,

                        date_emprunt DATE,
                        date_echeance DATE,
                        date_rendu DATE)""")  #DATE est représenté comme : YYYY-MM-DD
        conn.commit()

def destroyTable():
        cur.execute("""DROP TABLE EnsEmprunt""")
        conn.commit()
def emprunt_to_table(Emprunt):
		emprunt_table = (Emprunt.get_User_Emprunt().get_user_id(), Emprunt.get_Exemplaire_Emprunt().get_Exemplaire_id(), Emprunt.get_date_emprunt(), Emprunt.get_date_echeance(), Emprunt.get_date_rendu())
		return emprunt_table

def delete_emprunt(Emprunt):
        cur.execute("""DELETE FROM EnsEmprunt WHERE emprunt_id = ?""",(Emprunt.get_emprunt_id(),))
        conn.commit()

def get_nombre_emprunts():
        cur.execute("""SELECT COUNT(Emprunt_id) FROM EnsEmprunt""")
        return cur.fetchone()[0]

def insert_emprunt(Emprunt):
        if Emprunt.get_Exemplaire_Emprunt() == None:
            print "Oops. Vous voulez inserer quelque chose de vide !"
        else:
            cur.execute("""INSERT INTO EnsEmprunt(user_id,exemplaire_id,date_emprunt,date_echeance,date_rendu) VALUES (?, ?, ?, ?, ?)""",emprunt_to_table(Emprunt))
            conn.commit()

def update(Emprunt):
        try:
            cur.execute("""UPDATE EnsEmprunt SET date_rendu=? WHERE Emprunt_id=?""", (Emprunt.get_date_rendu(),Emprunt.get_emprunt_id()))
            conn.commit()
            print("Emprunt modifie avec succes !")
        except:
            print "La modification de l'exemplaire à échouée"
            raise



def get_Emprunt (Emprunt_id):
        cur.execute("""SELECT * FROM EnsEmprunt WHERE emprunt_id = (?)""",(Emprunt_id,))
        res = cur.fetchone()
        return Emprunt(Emprunt_id=res[0],User=EnsUtilisateurs.get_user(res[1]),Exemplaire=EnsExemplaires.get_Exemplaire(res[2]),date_emprunt=res[3],date_echeance=res[4],date_rendu=res[5])


def get_emprunts_User(User):
        cur.execute("""SELECT * FROM EnsEmprunt WHERE user_id = ?""",(User.get_user_id(),) )
        res = cur.fetchall()
        return res

def a_un_emprunt_en_cours(User):
        cur.execute("""SELECT * FROM EnsEmprunt WHERE user_id = ? AND date_rendu IS NULL""",(User.get_user_id(),) )
        res = cur.fetchone()
        return res != None


def get_emprunt_en_cours(User):
        if a_un_emprunt_en_cours(User):
                cur.execute("""SELECT * FROM EnsEmprunt WHERE user_id = ? AND date_rendu IS NULL""",(User.get_user_id(),) )
                res = cur.fetchone()
                return Emprunt(Emprunt_id=res[0],User=EnsUtilisateurs.get_user(res[1]),Exemplaire=EnsExemplaires.get_Exemplaire(res[2]),date_emprunt=res[3],date_echeance=res[4],date_rendu=res[5])
        else:
                return None

def rechercher_Exemplaire (Exemplaire):
        cur.execute("""SELECT * FROM EnsEmprunt WHERE Exemplaire_id = ?""",(Exemplaire.get_Exemplaire_id()))
        res = cur.fetchall()
        return Emprunt(Emprunt_id=res[0],User=EnsUtilisateurs.get_user(res[1]),Exemplaire=EnsExemplaires.get_Exemplaire(res[2]),date_emprunt=res[3],date_echeance=res[4],date_rendu=res[5])

#  A modifier => Renvoyer des instances d'emprunts dans un tableau
def rechercher_date_emprunt (Date):
        cur.execute("""SELECT * FROM EnsEmprunt WHERE date_emprunt = ? """,Date)
        res = cur.fetchall()
        return res

def rechercher_date_echeance (Date_echeance):
        cur.execute("""SELECT * FROM EnsEmprunt WHERE date_echeance = Date_echeance""" )
        res = cur.fetchall()
        return res

def printAll():
        cur.execute("""SELECT * FROM EnsEmprunt""")
        rows = cur.fetchall()
        #for row in rows:
        #    print (str(row[0])+" "+str(EnsUtilisateurs.get_user(row[1]).get_username())+" "+str(EnsExemplaires.get_Exemplaire(row[2]).get_Jeu_Exemplaire().get_Nom_jeu())+" Emprunté le: "+str(row[3])+" a rendre le : "+str(row[4])+" rendu le "+str(row[5]))
        return rows
        #for row in rows:
                #print('{0} : {1} - {2}'.format(row[0], row[1], row[2]))
