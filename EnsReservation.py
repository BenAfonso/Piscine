import sqlite3

from Reservation import Reservation

conn = sqlite3.connect("Ludotheque.db")
conn.execute('pragma foreign_keys = on')
conn.commit()
cur = conn.cursor()

def createTable():
        cur.execute("""CREATE TABLE IF NOT EXISTS EnsReservation(
                        Reservation_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE
                        user_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                        Jeu_id INTEGER,
                        Exemplaire_id INTEGER,
                        date_Reservation VARCHAR,
                        
                                        )""")
                                        
        conn.commit()
        
        
def destroyTable():
        cur.execute("""DROP TABLE EnsReservation""")
        conn.commit()

def Reservation_EnCours() :

	cur.execute=(""" SELECT Reservation_id FROM EnsReservation WHERE Reservation_id = ? """, (Reservation.get_Reservation_id()))
	result=cur.fetchone()
	return result != None

def Ajouter_Reservation(Reservation):
        #Ajouter_Reservation : Reservation x Utilisateur x EnsReservation -> EnsReservation
   if (not(Reservation_EnCours(Reservation))):
		try:
			cur.execute=(""" INSERT INTO EnsReservation(Reservation_id, Jeu_id, user_id, Exemplaire_id, date_Reservation) VALUES(?, ?, ?, ?, ?) """, (Reservation.get_Reservation_id(), Reservation.get_Jeu_id(), Reservation.get_user_id(), Extension.get_date_Reservation() ))
			conn.commit()
			 print(" Reservation ajoutée !")
		except:
			print ("Erreur lors de l'ajout d'une reservation")

	else:
		print ("Une reservation est deja en cours " ) 
		
		
def supprimer_Reservation(Reservation):
        #Supprime une reservation
	try:
		cur.execute=(""" DELETE FROM EnsReservation WHERE Reservation_id = ?""", (Reservation.get_Reservation_id()))
		conn.commit()
		
	except:
		print "Erreur lors de la suppression de la Reservation"
		
		
def Nombre_De_Reservation():
        # nombre_Reservation: EnsReservation -> Entier, renvoie le nombre de Reservation . """

	cur.execute =(""" SELECT COUNT (Reservation_id) FROM EnsReservation""")
	result = cur.fetchone()
	return result[0]

def rechercher_Reservation_User(user_id):
       #rechercher_Reservation_User: Int -> EnsReservation, renvoie la reservation de l'utilisateur que l'on veut connaitre.
	
        cur.execute("""SELECT * FROM EnsReservation WHERE user_id LIKE ?""",(user_id,))
        Reservaton_user = cur.fetchall()
        return Reservaton_user
	
def Reservation_to_table(Reservation):
        # Reservation -> List
        ReservationTable=(Reservation.get_Reservation_id(),Reservation.get_user_id(),Reservation.get_Jeu_id(),Reservation.get_Exemplaire_id(),Reservation.get_date_Reservation())
        return ReservationTable
		
