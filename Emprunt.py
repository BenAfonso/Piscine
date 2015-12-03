from datetime import date


class Emprunt : #Donne les infos concernant un emprunt
	"""un emprunt est def par :
		-l'Adherent qui emprunte
		-le jeu emprunté
		-la date d'emprunt
		-son échéance
		-son statut (en retard ou à l'heure)
		-sa validité  """
	def __init__(self, Emprunt_id = None, Adherent_id, Jeu_id, date_emprunt=date.today()):
		self.emprunt_id = Emprunt_id   		#Id de l'emprunt
		self.adherent_id = Adherent_id  			#Id de l'adhérent
		self.jeu_id = Jeu 						#Id du jeu emprunté
		self.date_emprunt = date_emprunt	
		self.date_echeance = calcul_echeance(self)

	def get_adherent_id (self):
		return(self.adherent_id)

	def get_jeu_id (self):
		return(self.jeu_id)

	def get_date_emprunt (self):
		return(self.date_emprunt)

	def get_date_echeance (self):
		return(self.date_echeance)


	def calcul_Date_Echeance(self):
		""" calcul_date_echeance: Emprunt -> Date, renvoie la date d'echeance de l'emprunt"""
		""" nouvelle date d'échance : 3 semaines """
		new_Day = int(self.get_date_emprunt().day + 21)
		date_echeance=(self.get_date_emprunt()).replace(day=new_Day)
		return date_echeance

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

	def emprunt_valide(self, adherent_id):
		""" emprunt_valide : Emprunt x Adherent -> Bool, renvoie True si l'utilisateur a les droits d'emprunt et qu'il n'a pas d'emprunt en cours, False sinon"""
		User = EnsUtilisateurs.get_user(adherent_id,)
		return User.empruntEnCours == False
		""" Il manque le droit d'emprunt dans utilisateurs, que faire si il y a une reservation en cours (conflit de dates)"""




"""
	def calcul_echeance (self):
		date_emprunt = self.date_emprunt
		date_echeance = []						#Date de retour. gère les années bissectiles de **** et les mois.
		mois_de_31_jours = [1, 3, 5, 7, 8, 10, 12]
		jour_de_retour = date_emprunt[0] + 7
		mois_de_retour = date_emprunt[1]
		annee_de_retour = date_emprunt[2]

		if date_emprunt[1] == 2 :	#check mois de février ?
			if date_emprunt[2] %4 == 0 : #check année bissextile ?
				if jour_de_retour > 29 : #check dépasse le nombre de jours du mois
					jour_de_retour = jour_de_retour -29
					mois_de_retour = mois_de_retour +1
			else :
				if jour_de_retour > 28 : #check dépasse le nombre de jours du mois
					jour_de_retour = jour_de_retour -28
					mois_de_retour = mois_de_retour +1

		elif date_emprunt[1] in mois_de_31_jours: #check tous les mois de 31 jours
			if jour_de_retour > 31 :
				jour_de_retour = jour_de_retour - 31
				mois_de_retour = mois_de_retour +1
				if mois_de_retour == 13 :	#check si on dépasse le 31 décembre
					mois_de_retour = mois_de_retour - 12
					annee_de_retour = annee_de_retour +1 #Bonne année !

		else :
			if jour_de_retour > 30:
				jour_de_retour = jour_de_retour - 30
				mois_de_retour = mois_de_retour +1

		date_echeance.append(jour_de_retour)
		date_echeance.append(mois_de_retour)
		date_echeance.append(annee_de_retour)
		return (date_echeance)
"""


"""
	def est_en_retard (self, date_retour):
		date_echeance = self.date_echeance
		retard = (date_retour[0] > date_echeance[0] and date_retour[1] == date_echeance[1]) or (date_retour[1] > date_echeance[1]) or (date_retour[2] > date_echeance[2])
		 #si on rend trop tard retard = True
		return (retard)
"""
