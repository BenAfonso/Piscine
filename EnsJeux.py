import sqlite3
from Jeu import Jeu



conn = sqlite3.connect("Ludotheque.db")
conn.execute('pragma foreign_keys = on')
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
                        Description TEXT)""")
        conn.commit()

def destroyTable():
        cur.execute("""DROP TABLE EnsJeux""")
        conn.commit()

def jeu_to_table(Jeu):
        # User -> List
        JeuTable=(Jeu.get_Jeu_id(),Jeu.get_Nom_jeu(),Jeu.get_Annee(),Jeu.get_Editeur(),Jeu.get_AgeMini(),Jeu.get_NombreJoueurs(),Jeu.get_Description())
        return JeuTable

def get_Jeu(Jeu_id=None,Nom_jeu=None):
        if (Jeu_id!=None): cur.execute("""SELECT * FROM EnsJeux WHERE Jeu_id = ?""",(Jeu_id,))
        if (Nom_jeu!=None): cur.execute("""SELECT * FROM EnsJeux WHERE Nom_jeu = ?""",(Nom_jeu,))
        try:     
                result=cur.fetchone()
                return Jeu(result[0],result[1],result[2],result[3],result[4],result[5],result[6])
        except:
                print "Erreur: ID du jeu non valide"

def delete_Jeu(Jeu):
        try:
                cur.execute("""DELETE FROM EnsJeux WHERE Jeu_id = ?""",(Jeu.get_Jeu_id(),))
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
                        cur.execute("""INSERT INTO EnsJeux(Jeu_id,Nom_jeu,Annee,Editeur,AgeMini,NombreJoueurs,Description) VALUES (?, ?, ?, ?, ?, ?, ?)""",jeu_to_table(Jeu))
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
                print(Nom,Annee,Editeur,AgeMini,NombreJoueurs)
##########################################################################
     

                
def rechercher(nom): # RAJOUTER PLUSIEURS RESULTATS :: fetchall()
        cur.execute("""SELECT * FROM EnsJeux WHERE Nom_jeu LIKE ?""",(nom,))
        rows = cur.fetchall()
        return rows

def update(Jeu):
        """ Fonction permettant d'actualiser les infos d'un jeu dans l'ensemble de Jeux"""
        # A FAIRE !

def printAll():
        cur.execute("""SELECT * FROM EnsJeux""") 
        rows = cur.fetchall()
        return rows
        #for row in rows:
                #print('{0} : {1} - {2} : {3}'.format(row[0], row[1], row[2], row[3]))
