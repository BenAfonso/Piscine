#-*-coding: utf-8 -*-
import sqlite3
from datetime import date, datetime
from Reservation import Reservation
import EnsUtilisateurs
import EnsExemplaires
import EnsJeux

conn = sqlite3.connect("Ludotheque.db")
conn.execute('pragma foreign_keys = on')
conn.commit()
cur = conn.cursor()



def createTable():
	cur.execute("""CREATE TABLE IF NOT EXISTS EnsReservation(
			Reservation_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
			user_id INTEGER,
			Jeu_id INTEGER,
			Extension_id INTEGER,
			Exemplaire_id INTEGER,
			date_Reservation DATE,
			Terminer BOOLEAN

					)""")

	conn.commit()


def destroyTable():
	cur.execute("""DROP TABLE EnsReservation""")
	conn.commit()


def Reservation_EnCours(User) :
""" Reservation_EnCours: User -> Bool ,True si l'User à une réservation qui n'est pas terminé, false sinon"""
					
	cur.execute(""" SELECT * FROM EnsReservation WHERE Terminer = 0 AND user_id = ? """, (User.get_user_id(),))
	result=cur.fetchone()
	return result != None


def Reservation_Termine(User) :
""" Reservation_Termine: User -> bool ,True si la reservation de l'User est Terminer, false sinon"""

    cur.execute(""" SELECT * FROM EnsReservation WHERE user_id = ? AND Terminer = 1 """, (User.get_user_id(),))
    result=cur.fetchone()
    return result != None


def get_Reservation_User(User) :
""" get_Reservation_User: User -> Reservation , renvoie un objet de type Reservation correspondant à l'User donné en parametre"""

	if self.Reservation_EnCours(User):
		cur.execute(""" SELECT * FROM EnsReservation WHERE Terminer = 0 AND user_id = ? """, (User.get_user_id(),))
		ReservationCur = cur.fetchone()
		Reservation(ReservationCur[0],ReservationCur[1],ReservationCur[2],ReservationCur[3],ReservationCur[4],ReservationCur[5],ReservationCur[6])
	else:
		print ("Pas de reservation.")


def get_Reservation(Reservation_id):
""" get_Reservation: Entier -> Reservation , renvoie un objet de type Reservation correspondant à l'identifiant de la reservation donné en parametre"""	

	cur.execute("""SELECT * FROM EnsReservation WHERE Reservation_id = (?)""",(Reservation_id,))
	res = cur.fetchone()
	return Reservation(Reservation_id=res[0],User=EnsUtilisateurs.get_user(res[1]),Jeu=EnsJeux.get_Jeu(res[2]),Exemplaire=EnsExemplaires.get_Exemplaire(res[3]),Extension=EnsExtension.get_Extension(res[4]),date_Reservation=res[5])

def Ajouter_Reservation(Reservation):
""" Ajouter_Reservation: Reservation -> Reservation, Il faut que Reservation_EnCours soit False pour pouvoir reserver  """

	if (not(Reservation_EnCours(Reservation.get_user()))):
		
		cur.execute(""" INSERT INTO EnsReservation(Reservation_id, user_id, Exemplaire_id, date_Reservation)
			VALUES(?, ?, ?, ?) """, (Reservation.get_Reservation_id(), Reservation.get_user().get_user_id(),Reservation.get_Exemplaire_id(), Reservation.get_date_Reservation(), ))
		conn.commit()
		print(" Reservation ajoutée !")
		

	else:
		print ("Une reservation est deja en cours " )


def supprimer_Reservation(Reservation):
""" supprimer_Reservation: Reservation -> EnsReservation, fonction qui permet de supprimer une réservation"""
	try:
		cur.execute(""" DELETE FROM EnsReservation WHERE Reservation_id = ?""", (Reservation.get_reservation_id()))
		conn.commit()

	except:
		print ("Erreur lors de la suppression de la Reservation")


def Nombre_De_Reservation():
""" Nombre_De_Reservation:  -> Entier, renvoie le nombre de reservation en cours"""

	cur.execute(""" SELECT COUNT (Reservation_id) FROM EnsReservation""")
	result = cur.fetchone()
	return result[0]


def rechercher_Reservation(User):
""" rechercher_Reservation: Text -> EnsReservation, renvoie la réservation présentes en base de l"User donné en paramètre"""
	
	cur.execute("""SELECT * FROM EnsReservation WHERE User_id = ? """, (User.get_User_id(),))
	Reservation_user = cur.fetchall()
	return Reservation_user


def rechercher_date_reservation (Date):
""" rechercher_Reservation: Date -> EnsReservation, renvoie une ou plusieurs reservations correspondant a la date donné en paramètre """
   
    cur.execute("""SELECT * FROM EnsReservation WHERE date_Reservation = ? """,Date)
    res = cur.fetchall()
    return res

def Reservation_to_table(Reservation):

	ReservationTable=(Reservation.get_Reservation_id(),Reservation.get_user_id(),Reservation.get_Jeu_id(),Reservation.get_Exemplaire_id(),Reservation.get_date_Reservation())
	return ReservationTable

def printAll():
	cur.execute(""" SELECT * FROM EnsReservation""")
	result = cur.fetchall()
	return result
