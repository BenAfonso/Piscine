#-*-coding: utf-8 -*-
import sqlite3
from Extension import Extension
from Jeu import Jeu 
from Reservation import Reservation


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
			Terminer BOOLEAN,
			
					)""")
					
	conn.commit()
	
	
def destroyTable():
	cur.execute("""DROP TABLE EnsReservation""")
	conn.commit()

# Il faut aussi que la reservation n'ait pas "Terminer == True" à rajouter dans la requête
def Reservation_EnCours(User) :

	cur.execute=(""" SELECT user_id FROM EnsReservation WHERE user_id = ? """, (Reservation.get_user_id()))
	result=cur.fetchone()
	return result != None

def get_Reservation(User) :

	cur.execute=(""" SELECT * FROM EnsReservation WHERE user_id = ? """, (Reservation.get_user_id()))
	result = cur.fetchall()

	for ReservationCur in result :
		ReservationCur = Reservation(ReservationCur[0],ReservationCur[1],ReservationCur[2],ReservationCur[3],ReservationCur[4],ReservationCur[5],ReservationCur[6])
	

def Ajouter_Reservation(Reservation):
	#Ajouter_Reservation : Reservation x Utilisateur x EnsReservation -> EnsReservation
	if (not(Reservation_EnCours(User))):
		try:
			cur.execute=(""" INSERT INTO EnsReservation(Reservation_id, Jeu_id, user_id, Exemplaire_id, date_Reservation) VALUES(?, ?, ?, ?, ?) """, (Reservation.get_Reservation_id(), Reservation.get_Jeu_id(), Reservation.get_user_id(), Extension.get_date_Reservation() ))
			conn.commit()
			print(" Reservation ajoutée !")
		except:
			print ("Erreur lors de l'ajout d'une reservation")

	else:
		print ("Une reservation est deja en cours " ) 
		
# Reservation_id = User_id <== Faux - faut mettre get_reservation_id
def supprimer_Reservation(Reservation):
	#Supprime une reservation
	try:
		cur.execute=(""" DELETE FROM EnsReservation WHERE Reservation_id = ?""", (Reservation.get_user_id()))
		conn.commit()
		
	except:
		print "Erreur lors de la suppression de la Reservation"
		
		
def Nombre_De_Reservation():
	# nombre_Reservation: EnsReservation -> Entier, renvoie le nombre de Reservation . """

	cur.execute =(""" SELECT COUNT (Reservation_id) FROM EnsReservation""")
	result = cur.fetchone()
	return result[0]

# même chose que get_reservation => mettre get_reservation_en_cours et il faut Terminer = False dans la requête et il faut le User.get_user_id()
def rechercher_Reservation_User(User):
       #rechercher_Reservation_User: Int -> EnsReservation, renvoie la reservation de l'utilisateur que l'on veut connaitre.
	
	cur.execute("""SELECT * FROM EnsReservation WHERE user_id LIKE ?""",(user_id,))
	Reservaton_user = cur.fetchall()
	return Reservaton_user
	
def Reservation_to_table(Reservation):
	# Reservation -> List
	ReservationTable=(Reservation.get_Reservation_id(),Reservation.get_user_id(),Reservation.get_Jeu_id(),Reservation.get_Exemplaire_id(),Reservation.get_date_Reservation())
	return ReservationTable
		
