import sqlite3
class EnsUtilisateurs:

        def __init__(self):
                self.conn = sqlite3.connect("Ludotheque.db")
                self.conn.execute('pragma foreign_keys = on')
                self.conn.commit()
                self.cur = self.conn.cursor()

        def createTable(self):
                self.cur.execute("""CREATE TABLE IF NOT EXISTS EnsUtilisateurs(
                                user_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                                username STRING,
                                password STRING)""")
                self.conn.commit()

        def destroyTable(self):
                self.cur.execute("""DROP TABLE EnsUtilisateurs""")
                self.conn.commit()

        def has_username(self,username):
                self.cur.execute("""SELECT user_id FROM EnsUtilisateurs WHERE username = ?""",(username,))
                result=self.cur.fetchone()
                if result != None:
                	return result[0]
                else:
                	return False

        def is_password(self,password,user_id):
                self.cur.execute("""SELECT password FROM EnsUtilisateurs WHERE user_id = ?""",(user_id,))
                result=self.cur.fetchone()
                return str(result[0]) == password

        def get_nombre_utilisateurs(self):
                self.cur.execute("""SELECT COUNT(User_id) FROM EnsUtilisateurs""")
                result=self.cur.fetchone()
                return result[0]

        def get_username(self,user_id):
                self.cur.execute("""SELECT username FROM EnsUtilisateurs WHERE user_id = ?""",(user_id,))
                result=self.cur.fetchone()
                return result[0]

        def get_password(self,user_id):
                self.cur.execute("""SELECT password FROM EnsUtilisateurs WHERE user_id = ?""",(user_id,))
                result=self.cur.fetchone()
                return result[0]

        def delete_user(self,user_id):
                try:
                        self.cur.execute("""DELETE FROM EnsUtilisateurs WHERE user_id = ?""",(user_id,))
                        self.conn.commit()
                except: 
                        print "Erreur lors de la suppression !"

        def insert(self,username,password):
                # VERIFIER SI USERNAME EXISTES PAS DEJA
                try:	
                        self.cur.execute("""INSERT INTO EnsUtilisateurs(username, password) VALUES (?, ?)""",(username,password))
                        self.conn.commit()
                        print("Utilisateur ajoute avec succes !")
                except:
                        print("Erreur lors de l'ajout de l'utilisateur")
                        

        def printAll(self):
                self.cur.execute("""SELECT user_id,username,password FROM EnsUtilisateurs""") # Enlever passwords
                rows = self.cur.fetchall()
                return rows
                #for row in rows:
                        #print('{0} : {1} - {2}'.format(row[0], row[1], row[2]))

        def __del__(self):
                self.conn.close()
