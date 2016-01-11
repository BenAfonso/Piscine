#-*-coding: utf-8 -*-
from Extension import Extension
import EnsJeux
import sqlite3

conn = sqlite3.connect("Ludotheque.db")
conn.execute('pragma foreign_keys = on')
conn.text_factory = str
conn.commit()
cur = conn.cursor()


def create_table_Extension():

	cur.execute(""" CREATE TABLE IF NOT EXISTS EnsExtensions(
						Extension_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
						Jeu_id INTEGER,
						Nom_Extension VARCHAR,
						Disponibilite BOOLEAN) """)
	conn.commit()


def destroy_table_Extension():
	cur.execute(""" DROP TABLE EnsExtensions """)
	conn.commit()


def get_Extension(Extension_id=None,Nom_Extension=None):
	""" get_Extension: Int x Text -> Extension , renvoie un objet de type Extension correspondant à l'identifiant et/ou au nom donné en parametre"""
        if (Extension_id!=None): cur.execute("""SELECT * FROM EnsExtensions WHERE Extension_id = ?""",(Extension_id,))
        if (Nom_Extension!=None): cur.execute("""SELECT * FROM EnsExtensions WHERE Nom_Extension = ?""",(Nom_Extension,))
        try:
                result=cur.fetchone()
                return Extension(result[0],result[1],result[2],result[3])
        except:
                print ("Erreur: ID du jeu non valide")



def est_Presente_Extension(Extension):
	""" est_Presente_Extension: Text x EnsExtensions -> Bool, True si l'extension est dans EnsExtensions, False sinon """

	cur.execute(""" SELECT Extension_id FROM EnsExtensions WHERE Nom_Extension = ?  """, (Extension.get_Nom_Extension(),))
	#recupère le premier résultat correspondant à la recherche, vide sinon.
	result=cur.fetchone()
	return result != None


def ajouter_Extension(Extension):
	""" ajouter_extension: Extension x EnsExtensions -> EnsExtensions, est_Presente_Extension(Extension.get_Nom_Extension) == False avant ajout. """
	if (not(est_Presente_Extension(Extension))):
		try:
			cur.execute(""" INSERT INTO EnsExtensions(Extension_id, Jeu_id, Nom_Extension, Disponibilite) VALUES(?, ?, ?, ?) """, (Extension.get_Extension_id(), Extension.get_Id_Jeu_Associe(), Extension.get_Nom_Extension(), Extension.get_Disponible(),))
			conn.commit()
			print ("L'extension a bien ete ajoutee")
		except:
			print ("Erreur lors de l'ajout de l'extension")

	else:
		print ("L'extension est déjà présente dans la base.")

def supprimer_Extension(Extension):
	""" supprimer_Extension: Extension x EnsExtensions -> EnsExtensions, est_Presente_Extension(Extension.get_Nom_Extension) == True avant suppression."""
	if(est_Presente_Extension(Extension)):
		try:
			cur.execute(""" DELETE FROM EnsExtensions WHERE Extension_id = ?""", (Extension.get_Extension_id(),))
			conn.commit()
		except:
			print ("Erreur lors de la suppression de l'extension")
			raise
	else:
		print ("Impossible de supprimer une extension non présente dans la base.")
		raise

def nombre_extensions_Jeu(Jeu):
	""" nombre_extensions: Jeu -> Entier, renvoie le nomrbe d'extension d'un jeu donné. Le jeu doit être dans EnsJeux"""

	cur.execute(""" SELECT COUNT(Extension_id) FROM EnsExtensions WHERE Jeu_id = (?)""", (Jeu.get_Jeu_id(),))
	result = cur.fetchone()
	return result[0]


def nombre_Extensions():
	""" nombre_extensions: EnsExtensions -> Entier, renvoie le nombre d'extensions en base. """

	cur.execute(""" SELECT COUNT (Extension_id) FROM EnsExtensions""")
	result = cur.fetchone()
	return result[0]

def rechercher_Extensions_Jeu(Jeu):
	""" rechercher_extension: Text -> EnsExtensions, renvoie une ou plusieurs extensions présentes en base
	correspondant au Jeu donné en paramètre """

	cur.execute(""" SELECT * FROM EnsExtensions  WHERE Jeu_id = ? """, (Jeu.get_Jeu_id(),))
	all_Extensions = cur.fetchall()
	return all_Extensions

def est_Disponible_Extension(Extension):
	""" est_Disponible_Extension: Extension -> Bool, True si l'extension est disponible, False sinon. """

	cur.execute(""" SELECT Disponibilite FROM EnsExtensions WHERE Extension_id = ?""", (Extension.get_Extension_id(),))
	disponibility = cur.fetchone()

	return disponibility != None

def afficher_Extensions():
	""" affiche les extensions de la table EnsExtensions """

	cur.execute(""" SELECT Extension_id FROM EnsExtensions""")
	res = cur.fetchall()
	return res

def get_Extension_Jeu(Jeu):
	cur.execute("""SELECT * FROM EnsExtensions WHERE Jeu_id = ?""",(Jeu.get_Jeu_id(),))
	res = cur.fetchall()
	resultat = []
	i=0
	for ext in res:
		ext = Extension(ext[0],ext[1],ext[2],ext[3])
		resultat.append(ext)
	return resultat



def update_Extension(Extension):
	""" update_Extension: Extension -> Extension, modifie les informations d'une extension donnée """
	try:
		cur.execute(""" UPDATE EnsExtensions SET Jeu_id = ?, Nom_Extension = ?, Disponibilite = ? WHERE Extension_id = ?""", (Extension.get_Id_Jeu_Associe(), Extension.get_Nom_Extension(), Extension.get_Disponible(), Extension.get_Extension_id(),))
		print ("L'extension a bien ete mise a jour")
	except:
		raise

def printAll():
        cur.execute("""SELECT * FROM EnsExtensions""")
        rows = cur.fetchall()
        return rows
