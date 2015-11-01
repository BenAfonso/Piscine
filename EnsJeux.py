import sqlite3
class EnsJeux:

        def __init__(self):
                self.conn = sqlite3.connect("Ludotheque.db")
                self.conn.execute('pragma foreign_keys = on')
                self.conn.commit()
                self.cur = self.conn.cursor()

        def createTable(self):
                self.cur.execute("""CREATE TABLE IF NOT EXISTS EnsJeux(
                                Jeu_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                                Nom_jeu STRING,
                                AgeMini STRING,
                                Description TEXT)""")
                self.conn.commit()

        def destroyTable(self):
                self.cur.execute("""DROP TABLE EnsJeux""")
                self.conn.commit()

        def get_Jeu(self,Jeu_id):
                self.cur.execute("""SELECT * FROM EnsJeux WHERE Jeu_id = ?""",(Jeu_id,))
                jeu=self.cur.fetchone()
                return jeu
                
        def insert(self,Jeu):
                try:	
                        self.cur.execute("""INSERT INTO EnsJeux(Nom_jeu, AgeMini, Description) VALUES (?, ?, ?)""",(Jeu[1],Jeu[2],Jeu[3]))
                        self.conn.commit()
                except:
                        print("Erreur lors de l'ajout du jeu")
                finally:
                        print("Jeu ajoute avec succes !")

        def printAll(self):
                self.cur.execute("""SELECT * FROM EnsJeux""") # Enlever passwords
                rows = self.cur.fetchall()
                return rows
                #for row in rows:
                        #print('{0} : {1} - {2} : {3}'.format(row[0], row[1], row[2], row[3]))

        def __del__(self):
                self.conn.close()
