from Extension import Extension
import EnsJeux
import sqlite3
import EnsJeux

conn = sqlite3.connect("Ludotheque.db")
conn.execute('pragma foreign_keys = on')
conn.commit()
cur = conn.cursor()


def create_table_extension():

	cur.execute=(""" CREATE TABLE IF NOT EXISTS EnsExtensions(
						Extension_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
						Jeu_id INTEGER,
						nom_extension VARCHAR,
						nombre_extension INTEGER) """)
	conn.commit()


def destroy_table_extension():
	cur.execute=(""" DROP TABLE EnsExtensions """)
	cur.commit()


def est_presente_extension(NomExtension):
	""" est_presente_extension: Text x EnsExtensions -> Bool, True si l'extension est dans EnsExtensions, False sinon """

	cur.execute=(""" SELECT nom_extension FROM EnsExtensions WHERE nom_extension = ? """, (NomExtension))
	#recupère le premier résultat correspondant à la recherche, vide sinon.
	result=cur.fetchone()
	return result != None


def ajouter_extension(Extension):
	""" ajouter_extension: Extension x EnsExtensions -> EnsExtensions, est_presente_extension(Extension.get_nom_extension) == False avant ajout. """
	if not(est_presente_extension(Extension.get_nom_extension())):
		try:
			cur.execute=(""" INSERT INTO EnsExtensions(Extension_id, Jeu_id, nom_extension, nombre_extension) VALUES(?, ?, ?, ?) """, (Extension.get_extension_id(), Extension.get_extension_jeu_id(), Extension.get_nom_extension(), Extension.get_nombre_extension() ))
			conn.commit()
		except:
			print "Erreur lors de l'ajout de l'extension"

	else:
		print "L'extension est déjà présente dans la base."

def supprimer_extension(Extension):
	try:
		cur.execute=(""" DELETE FROM EnsExtensions WHERE Extension_id = ?""", (Extension.get_extension_id()))
		conn.commit()
	except:
		print "Erreur lors de la suppression de l'extension"

def nombre_extensions_Jeu(Jeu):
	""" nombre_extensions: Jeu -> Entier, renvoie le nomrbe d'extension d'un jeu donné. Le jeu doit être dans EnsJeux"""

	if not(has_jeu(Jeu.get_Nom_jeu())):
		cur.execute =(""" SELECT COUNT (Extension_id) FROM EnsJeux, EnsExtensions WHERE EnsJeux.? = EnsExtensions.? """, (Jeu.get_Jeu_id, Extension.get_extension_id))
		result = cur.fetchone()
		return result[0]
	else:
		print "Impossible de récupérer le nombre d'extensions de ce jeu car il n'est pas dans la base"

def nombre_extensions():
	""" nombre_extensions: EnsExtensions -> Entier, renvoie le nombre d'extensions en base. """

	cur.execute =(""" SELECT COUNT (Extension_id) FROM EnsExtensions""")
	result = cur.fetchone()
	return result[0]

def rechercher_extension(nomExtension):
	""" rechercher_extension: Text -> EnsExtensions, renvoie une ou plusieurs extensions présentes en base
	correspondant au critère de recherche nom_extension """

	cur.execute =(""" SELECT * FROM EnsExtensions WHERE nom_extension LIKE ?) """, (nomExtension))
	result = cur.fetchall()
	return result
