#-*-coding: utf-8 -*-
import sqlite3
from datetime import date, datetime
from Reservation import Reservation
#from Utilisateur import Utilisateur
import EnsUtilisateurs
import EnsExemplaires
#import EnsExtension
import EnsJeux

conn = sqlite3.connect("Ludotheque.db")
conn.execute('pragma foreign_keys = on')
conn.commit()
cur = conn.cursor()

# Rajouter une fonction qui prend une reservation_id et qui renvoie la reservation (instance)
# Rajouter une fonction qui prend un exemplaire et qui renvoie true s'il est reservé

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

# Il faut aussi que la reservation n'ait pas "Terminer == True" à rajouter dans la requête
def Reservation_EnCours(User) :

	cur.execute(""" SELECT * FROM EnsReservation WHERE Terminer = 0 AND user_id = ? """, (User.get_user_id(),))
	result=cur.fetchone()
	return result != None

# Historique de reservation ( Boolean ??????)
def Reservation_Termine(User) :

    cur.execute(""" SELECT * FROM EnsReservation WHERE user_id = ? AND Terminer = 0 """, (User.get_user_id(),))
    result=cur.fetchone()
    return result != None

# fonction qui prend un user et qui renvoie la reservation (instance)
def get_Reservation_User(User) :

	if self.Reservation_EnCours(User):
		cur.execute(""" SELECT * FROM EnsReservation WHERE Terminer = 0 AND user_id = ? """, (User.get_user_id(),))
		ReservationCur = cur.fetchone()
		Reservation(ReservationCur[0],ReservationCur[1],ReservationCur[2],ReservationCur[3],ReservationCur[4],ReservationCur[5],ReservationCur[6])
	else:
		print "Pas de reservation."

# fonction qui prend une reservation_id et qui renvoie la reservation (instance)
def get_Reservation(Reservation_id):
	cur.execute("""SELECT * FROM EnsReservation WHERE Reservation_id = (?)""",(Reservation_id,))
	res = cur.fetchone()
	return Reservation(Reservation_id=res[0],User=EnsUtilisateurs.get_user(res[1]),Jeu=EnsJeux.get_Jeu(res[2]),Exemplaire=EnsExemplaires.get_Exemplaire(res[3]),Extension=EnsExtension.get_Extension(res[4]),date_Reservation=res[5])

def Ajouter_Reservation(Reservation):
	#Ajouter_Reservation : Reservation x Utilisateur x EnsReservation -> EnsReservation
	if (not(Reservation_EnCours(Reservation.get_user()))):
		#try:
		cur.execute(""" INSERT INTO EnsReservation(Reservation_id, user_id, Exemplaire_id, date_Reservation)
			VALUES(?, ?, ?, ?) """, (Reservation.get_Reservation_id(), Reservation.get_user().get_user_id(),Reservation.get_Exemplaire_id(), Reservation.get_date_Reservation(), ))
		conn.commit()
		print(" Reservation ajoutée !")
		#except:
		#	print ("Erreur lors de l'ajout d'une reservation")

	else:
		print ("Une reservation est deja en cours " )

# Reservation_id = User_id <== Faux - faut mettre get_reservation_id
def supprimer_Reservation(Reservation):
	#Supprime une reservation
	try:
		cur.execute(""" DELETE FROM EnsReservation WHERE Reservation_id = ?""", (Reservation.get_reservation_id()))
		conn.commit()

	except:
		print "Erreur lors de la suppression de la Reservation"


def Nombre_De_Reservation():
	# nombre_Reservation: EnsReservation -> Entier, renvoie le nombre de Reservation . """

	cur.execute(""" SELECT COUNT (Reservation_id) FROM EnsReservation""")
	result = cur.fetchone()
	return result[0]

# même chose que get_reservation => mettre get_reservation_en_cours et il faut Terminer = False dans la requête et il faut le User.get_user_id()
def rechercher_Reservation_User(User):
       #rechercher_Reservation_User: Int -> EnsReservation, renvoie la reservation de l'utilisateur que l'on veut connaitre.

	cur.execute("""SELECT * FROM EnsReservation WHERE user_id LIKE ?""",(user_id,))
	Reservaton_user = cur.fetchall()
	return Reservaton_user

#  A modifier => Renvoyer des instances d'emprunts dans un tableau
def rechercher_date_reservation (Date):
    cur.execute("""SELECT * FROM EnsReservation WHERE date_Reservation = ? """,Date)
    res = cur.fetchall()
    return res

def Reservation_to_table(Reservation):
	# Reservation -> List
	ReservationTable=(Reservation.get_Reservation_id(),Reservation.get_user_id(),Reservation.get_Jeu_id(),Reservation.get_Exemplaire_id(),Reservation.get_date_Reservation())
	return ReservationTable

def printAll():
	cur.execute(""" SELECT * FROM EnsReservation""")
	result = cur.fetchall()
	return result
