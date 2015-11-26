#-*-coding: utf-8 -*-
from Extension import Extension 
import EnsJeux
import sqlite3

conn = sqlite3.connect("Ludotheque.db")
conn.execute('pragma foreign_keys = on')
conn.commit()
cur = conn.cursor()


def create_table_Extension():

	cur.execute(""" CREATE TABLE IF NOT EXISTS EnsExtensions(
						Extension_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
						Jeu_id INTEGER,
						Nom_Extension VARCHAR,
						Disponibilité BOOLEAN) """)
	conn.commit()


def destroy_table_Extension():
	cur.execute(""" DROP TABLE EnsExtensions """)
	cur.commit()


def est_Presente_Extension(Extension):
	""" est_Presente_Extension: Text x EnsExtensions -> Bool, True si l'extension est dans EnsExtensions, False sinon """

	cur.execute(""" SELECT Extension_id FROM EnsExtensions WHERE Extension_id = ? """, (Extension.get_Extension_id(),))
	#recupère le premier résultat correspondant à la recherche, vide sinon.
	result=cur.fetchone()
	return result != None


def ajouter_Extension(Extension):
	""" ajouter_extension: Extension x EnsExtensions -> EnsExtensions, est_Presente_Extension(Extension.get_Nom_Extension) == False avant ajout. """
	if (not(est_Presente_Extension(Extension))):
		try:
			cur.execute(""" INSERT INTO EnsExtensions(Extension_id, Jeu_id, Nom_Extension, Disponibilité) VALUES(?, ?, ?, ?) """, (Extension.get_Extension_id(), Extension.get_Id_Jeu_Associe(), Extension.get_Nom_Extension(), Extension.get_Disponible(),))
			conn.commit()
		except:
			print "Erreur lors de l'ajout de l'extension"

	else:
		print "L'extension est déjà présente dans la base."

def supprimer_Extension(Extension):
	try:
		cur.execute(""" DELETE FROM EnsExtensions WHERE Extension_id = ?""", (Extension.get_Extension_id(),))
		conn.commit()
	except:
		print "Erreur lors de la suppression de l'extension"

def nombre_extensions_Jeu(Jeu): # A tester apres avoir corriger les bugs de cle primaire et attribut dispo
	""" nombre_extensions: Jeu -> Entier, renvoie le nomrbe d'extension d'un jeu donné. Le jeu doit être dans EnsJeux"""

	if not(has_jeu(Jeu.get_Nom_jeu())):
		cur.execute =(""" SELECT COUNT (Extension_id) FROM EnsExtensions WHERE EnsExtensions.Jeu_id = ?""", (Jeu.get_Jeu_id(),))
		result = cur.fetchone()
		return result[0]
	else:
		print "Impossible de récupérer le nombre d'extensions de ce jeu car il n'est pas dans la base"

def nombre_Extensions():
	""" nombre_extensions: EnsExtensions -> Entier, renvoie le nombre d'extensions en base. """

	cur.execute(""" SELECT COUNT (Extension_id) FROM EnsExtensions""")
	result = cur.fetchone()
	return result[0]

def rechercher_Extensions_Jeu(Jeu):  # A tester apres avoir corriger les bugs de cle primaire et attribut dispo
	""" rechercher_extension: Text -> EnsExtensions, renvoie une ou plusieurs extensions présentes en base
	correspondant au Jeu donné en paramètre """

	cur.execute =(""" SELECT Extension_id, Nom_Extension FROM EnsExtensions  WHERE EnsExtensions.Jeu_id = ? ) """, (Jeu.get_Jeu_id(),))
	all_Extensions = cur.fetchall()
	return all_Extensions

def est_Disponible_Extension(Extension): # A debugger: retourne un entier au lieu d'un boolean...
	""" est_Disponible_Extension: Extension -> Bool, True si l'extension est disponible, False sinon. """

	cur.execute(""" SELECT Disponibilité FROM EnsExtensions WHERE Extension_id = ?""", (Extension.get_Extension_id(),))
	disponibility = cur.fetchone()

	return disponibility[0]

def afficher_Extensions():
	""" affiche les extensions de la table EnsExtensions """

	cur.execute(""" SELECT Extension_id FROM EnsExtensions""")
	res = cur.fetchall
	return res

def update_Extension(Extension):
	""" update_Extension: Extension -> Extension, modifie les informations d'une extension donnée """
	if (est_Presente_Extension(Extension)):
		cur.execute(""" UPDATE EnsExtensions SET Jeu_id = ?, Nom_Extension = ?, Disponibilité = ? """, (Extension.get_Id_Jeu_Associe(), Extension.get_Nom_Extension(), Extension.get_Disponible(),))
	else:
		print "L'extension à modifier n'existe pas."

