import sqlite3


conn = sqlite3.connect("Ludotheque.db")
conn.execute('pragma foreign_keys = on')
conn.execute("PRAGMA busy_timeout = 30000") 
conn.commit()
cur = conn.cursor()

def createTable():
        cur.execute("""CREATE TABLE IF NOT EXISTS EnsAdmins(
                        admin_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                        user_id INTEGER)""")
        conn.commit()

def destroyTable():
        cur.execute("""DROP TABLE EnsAdmins""")
        conn.commit()

def est_admin(User):
        cur.execute("""SELECT admin_id FROM EnsAdmins WHERE user_id = ?""",(User.get_user_id(),))
        res=cur.fetchone()
        return res != None

def delete_admin(User):
        try:
                cur.execute("""DELETE FROM EnsAdmins WHERE user_id = ?""",(User.get_user_id(),))
                conn.commit()
        except: 
                print ("Erreur lors de la suppression !")

def insert(User):
        try:    
                cur.execute("""INSERT INTO EnsAdmins(user_id) VALUES (?)""",(User.get_user_id(),))
                conn.commit()
        except:
                print("Erreur lors de la promotion de l'utilisateur")
        finally:
                print("#NAME passe admin avec succes !")

def printAll():
        cur.execute("""SELECT user_id,admin_id FROM EnsAdmins""") # Enlever passwords
        rows = cur.fetchall()
        
        for row in rows:
                print('{0} : {1}'.format(row[0], row[1]))

