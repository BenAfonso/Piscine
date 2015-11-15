import sqlite3

from Reservation import Reservation

conn = sqlite3.connect("Ludotheque.db")
conn.execute('pragma foreign_keys = on')
conn.commit()
cur = conn.cursor()

def createTable():
        cur.execute("""CREATE TABLE IF NOT EXISTS EnsReservation(
                        Reservation_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE
                                        )""")
                                        
        conn.commit()
        
        
def destroyTable():
        cur.execute("""DROP TABLE EnsReservation""")
        conn.commit()
