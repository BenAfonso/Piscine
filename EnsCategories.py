import sqlite3

conn = sqlite3.connect("Ludotheque.db")
conn.execute('pragma foreign_keys = on')
conn.commit()
cur = conn.cursor()

def createTable():
        cur.execute("""CREATE TABLE IF NOT EXISTS EnsCategories(
                        Categorie_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                        Categorie STRING)""")
        conn.commit()


def destroyTable():
        cur.execute("""DROP TABLE EnsCategories""")
        conn.commit()

def ajouterCategorie(nomCategorie):
        if nomCategorie != None:
                cur.execute("""INSERT INTO EnsCategories(Categorie) VALUES (?)""",(nomCategorie,))
                conn.commit()
        else:
                print "Renseignez un nom !"

def supprimerCategorie(Categorie_id):
        try:
                cur.execute("""DELETE FROM EnsCategories WHERE Categorie_id = ?""",(Categorie_id,))
                conn.commit()
        except:
                print "Erreur lors de la suppression !"

def categorieExiste(Categorie_id):
        cur.execute("""SELECT * FROM EnsCategories WHERE Categorie_id = ?""", (Categorie_id,))
        result = cur.fetchone()
        return result != None


def get_Categorie(Categorie_id=None,Categorie=None):
        if Categorie_id != None and Categorie == None:
                cur.execute("""SELECT * FROM EnsCategories WHERE Categorie_id = ?""", (Categorie_id,))
                result = cur.fetchone()
        elif Categorie != None and Categorie_id == None:
                cur.execute("""SELECT * FROM EnsCategories WHERE Categorie = ?""", (Categorie,))
                result = cur.fetchone()
        else:
                print "Erreur."
        return result

def printAll():
        cur.execute("""SELECT * FROM EnsCategories""")
        rows = cur.fetchall()
        for row in rows:
                print('{0} : {1}'.format(row[0], row[1]))
