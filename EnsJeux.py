#-*- coding:utf-8 -*-
import sqlite3
from Jeu import Jeu
import EnsCategories


conn = sqlite3.connect("Ludotheque.db")
conn.execute('pragma foreign_keys = on')
conn.text_factory = str
conn.commit()
cur = conn.cursor()
def createTable():
        cur.execute("""CREATE TABLE IF NOT EXISTS EnsJeux(
                        Jeu_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                        Nom_jeu STRING,
                        Annee STRING,
                        Editeur STRING,
                        AgeMini STRING,
                        NombreJoueurs STRING,
                        Description TEXT,
                        Categorie_id INTEGER)""")
        conn.commit()

def destroyTable():
        cur.execute("""DROP TABLE EnsJeux""")
        conn.commit()

def jeu_to_table(Jeu):
        # User -> List
        JeuTable=(Jeu.get_Jeu_id(),Jeu.get_Nom_jeu(),Jeu.get_Annee(),Jeu.get_Editeur(),Jeu.get_AgeMini(),Jeu.get_NombreJoueurs(),Jeu.get_Description(),Jeu.get_Categorie_id())
        return JeuTable

def get_Jeu(Jeu_id=None,Nom_jeu=None):
        if (Jeu_id!=None): cur.execute("""SELECT * FROM EnsJeux WHERE Jeu_id = ?""",(Jeu_id,))
        if (Nom_jeu!=None): cur.execute("""SELECT * FROM EnsJeux WHERE Nom_jeu = ?""",(Nom_jeu,))
        try:
                result=cur.fetchone()
                return Jeu(result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7])
        except:
                print "Erreur: ID du jeu non valide"

def delete_Jeu(Jeu):
        try:
                cur.execute("""DELETE FROM EnsJeux WHERE Jeu_id = ?""",(Jeu.get_Jeu_id(),))
                conn.commit()
                cur.execute("""DELETE FROM EnsExemplaires WHERE Jeu_id = ?""",(Jeu.get_Jeu_id(),))
                conn.commit()
        except:
                print "Erreur lors de la suppression !"

def has_Jeu(Nom_jeu):
        cur.execute("""SELECT Jeu_id FROM EnsJeux WHERE Nom_jeu = ?""",(Nom_jeu,))
        result=cur.fetchone()
        return result != None

def get_nombre_jeux():
        cur.execute("""SELECT COUNT(Jeu_id) FROM EnsJeux """)
        result = cur.fetchone()
        return result[0]

def insert(Jeu):
        """Fonction permettant d'inserer un jeu dans l'ensemble de Jeux
        #Jeu x EnsJeux => EnsJeux
        >>>EnsJeux.insert(Type Jeu)"""
        if not(has_Jeu(Jeu.get_Nom_jeu())):
                try:
                        cur.execute("""INSERT INTO EnsJeux(Jeu_id,Nom_jeu,Annee,Editeur,AgeMini,NombreJoueurs,Description,Categorie_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",jeu_to_table(Jeu))
                        conn.commit()
                        print("Jeu ajoute avec succes !")
                except:
                        print (jeu_to_table(Jeu))
                        print("Erreur lors de l'ajout du jeu")
        else:
                print("Erreur: Un jeu est deja enregistre au meme nom.")


#### FONCTION SEULEMENT POUR IMPORTATION DE LA BASE INITIAL DES JEUX #####
def insertFromMain(Nom,Annee,Editeur,AgeMini,NombreJoueurs,Description=""):
        """Fonction permettant d'inserer un jeu dans l'ensemble de Jeux
        #Jeu x EnsJeux => EnsJeux
        >>>EnsJeux.insert(Type Jeu)"""
        try:
                cur.execute("""INSERT INTO EnsJeux(Nom_jeu,Annee,Editeur,AgeMini,NombreJoueurs,Description) VALUES (?, ?, ?, ?, ?, ?)""",(Nom,Annee,Editeur,AgeMini,NombreJoueurs,Description,))
                conn.commit()
        except:
                raise
##########################################################################



def rechercher(nom=None,categorie=None,editeur=None):
        if nom != None:
            cur.execute("""SELECT * FROM EnsJeux WHERE Nom_jeu LIKE ?""",(nom,))
            result = cur.fetchall()
        elif categorie != None:
            cat = EnsCategories.rechercherCategorie(categorie)
            cur.execute("""SELECT * FROM EnsJeux WHERE Categorie_id LIKE ?""",(cat,))
            result = cur.fetchall()
        elif editeur != None:
            cur.execute("""SELECT * FROM EnsJeux WHERE Editeur LIKE ?""",(editeur,))
            result = cur.fetchall()
        else:
            raise
        return result

def update(Jeu):
        """ Fonction permettant d'actualiser les infos d'un jeu dans l'ensemble de Jeux"""
        # A FAIRE !(Nom_jeu,Annee,Editeur,AgeMini,NombreJoueurs,Description,Categorie_id)
        try:
                cur.execute("""UPDATE EnsJeux SET Nom_jeu=?,Annee=?,Editeur=?,AgeMini=?,NombreJoueurs=?,Description=?,Categorie_id=? WHERE Jeu_id=?""", (Jeu.get_Nom_jeu(),Jeu.get_Annee(),Jeu.get_Editeur(),Jeu.get_AgeMini(),Jeu.get_NombreJoueurs(),Jeu.get_Description(),Jeu.get_Categorie_id(),Jeu.get_Jeu_id()))
                conn.commit()
                print "Le jeu a bien été modifié !"
        except:
                print "La modification du jeu à échouée"
                raise
def printAll():
        cur.execute("""SELECT * FROM EnsJeux""")
        rows = cur.fetchall()
        return rows
        #for row in rows:
                #print('{0} : {1} - {2} : {3}'.format(row[0], row[1], row[2], row[3]))
