import sqlite3
class EnsAdmins:

        def __init__(self):
                self.conn = sqlite3.connect("Ludotheque.db")
                self.conn.execute('pragma foreign_keys = on')
                self.conn.commit()
                self.cur = self.conn.cursor()

        def createTable(self):
                self.cur.execute("""CREATE TABLE IF NOT EXISTS EnsAdmins(
                                admin_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                                user_id INTEGER)""")
                self.conn.commit()

        def destroyTable(self):
                self.cur.execute("""DROP TABLE EnsAdmins""")
                self.conn.commit()

        def est_admin(self,user_id):
                self.cur.execute("""SELECT admin_id FROM EnsAdmins WHERE user_id = ?""",(user_id,))
                res=self.cur.fetchone()
                return res != None

        def insert(self,user_id):
                try:    
                        self.cur.execute("""INSERT INTO EnsAdmins(user_id) VALUES (?)""",(user_id,))
                        self.conn.commit()
                except:
                        print("Erreur lors de la promotion de l'utilisateur")
                finally:
                        print("#NAME passe admin avec succes !")

        def printAll(self):
                self.cur.execute("""SELECT user_id,admin_id FROM EnsAdmins""") # Enlever passwords
                rows = self.cur.fetchall()
                
                for row in rows:
                        print('{0} : {1}'.format(row[0], row[1]))

        def __del__(self):
                self.conn.close()
