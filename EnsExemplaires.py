import sqlite3

from EnsJeux import EnsJeux
class EnsExemplaires:

        def __init__(self):
                self.conn = sqlite3.connect("Ludotheque.db")
                self.conn.execute('pragma foreign_keys = on')
                self.conn.commit()
                self.cur = self.conn.cursor()

        def createTable(self):
                self.cur.execute("""CREATE TABLE IF NOT EXISTS EnsExemplaires(
                                Exemplaire_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                                Jeu_id INTEGER)""")
                self.conn.commit()

        def destroyTable(self):
                self.cur.execute("""DROP TABLE EnsExemplaires""")
                self.conn.commit()

        

                
        def insert(self,Exemplaire):
                # PRECONDITION: Jeu_id doit EXISTER ! (A FAIRE)
                try:	
                        self.cur.execute("""INSERT INTO EnsExemplaires(Jeu_id) VALUES (?)""",(Exemplaire[1],))
                        self.conn.commit()
                        print("Exemplaire ajoute avec succes !")
                except:
                        print("Erreur lors de l'ajout de l'exemplaire")
                
                        

        def printAll(self):
                self.cur.execute("""SELECT * FROM EnsExemplaires""")
                rows = self.cur.fetchall()
                ListeJeux = EnsJeux()
                for row in rows:
                        print('{0} : {1}'.format(row[0], ListeJeux.get_Jeu(row[1])[1]))

        def __del__(self):
                self.conn.close()
