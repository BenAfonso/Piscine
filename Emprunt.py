#-*- coding:utf-8-*-
from datetime import date
import EnsUtilisateurs
import EnsJeux
from Utilisateur import Utilisateur

class Emprunt : #Donne les infos concernant un emprunt
	"""un emprunt est def par :
		-l'Adherent qui emprunte
		-le jeu emprunté
		-la date d'emprunt
		-son échéance
		-son statut (en retard ou à l'heure)
		-sa validité  """
	# Sa validité ??
	def __init__(self, Emprunt_id = None, date_emprunt=date.today(), User=None, Jeu_id=None):
		self.Emprunt_id = Emprunt_id   		#Id de l'emprunt
		self.User_id = User.get_user_id() 			#Id de l'adhérent
		self.Jeu_id = Jeu_id 						#Id du jeu emprunté
		self.date_emprunt = date_emprunt
		self.date_echeance = self.calcul_Date_Echeance()

	# A Rajouter: Et l'plus important : get_emprunt_id(self)
	def get_emprunt_id(self):
		return self.Emprunt_id

	def get_User_id(self):
		return(self.User_id)

	def get_Jeu_id(self):
		return(self.Jeu_id)

	def get_date_emprunt (self):
		return(self.date_emprunt)

	def get_date_echeance (self):
		return(self.date_echeance)


	def calcul_Date_Echeance(self):
		""" calcul_date_echeance: Emprunt -> Date, renvoie la date d'echeance de l'emprunt"""
		""" nouvelle date d'échance : 3 semaines """
		# Est-ce que ça incrémente le mois si JJ > 10 ?
		new_Day = int(self.get_date_emprunt().day + 21)
		date_echeance=(self.get_date_emprunt()).replace(day=new_Day)
		return date_echeance

	# Si la date de retour est inférieure: Renvoyer False => A inverser
	# Mettre sur une seule ligne :: return (date_retour > self.get_date_echeance())
	def emprunt_En_Retard(self, date_retour):
		""" emprunt_En_Retard: Emprunt x Date -> Bool, True si le retour de l'emprunt dépasse la date d'echeance, False sinon """
		# Une date est considérée comme inférieure à une autre lorsqu'elle la précède dans le temps. cf doc python > date object
		if(date_retour <= self.calcul_Date_Echeance()):
			return True
		else:
			return False

	def calcul_retard (self):
		""" calcul_retard : Emprunt -> entier, 0 si emprunt_En_Retard est False, la difference entre date_retour et date_echeance sinon"""
		date_retour = datetime.today()
		if emprunt_En_Retard(self, date_retour):
			jour_de_retard = date_retour - date_echeance
		else :
			return 0

	# ???? Mauvais type pour cette fonction, on en discute demain
	def emprunt_valide(self, User_id):
		""" emprunt_valide : Emprunt x Adherent -> Bool, renvoie True si l'utilisateur a les droits d'emprunt et qu'il n'a pas d'emprunt en cours, False sinon"""
		User = EnsUtilisateurs.get_user(User_id,)
		return User.empruntEnCours == False
		""" Il manque le droit d'emprunt dans utilisateurs, que faire si il y a une reservation en cours (conflit de dates)"""
