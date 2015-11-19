
class Emprunt : #Donne les infos concernant un emprunt 
	"""un emprunt est def par :
		-l'Adherent qui emprunte
		-le jeu emprunté
		-la date d'emprunt
		-son échéance
		-son statut (en retard ou à l'heure)
		-sa validité  """
	def __init__(self, Adherent, Jeu, date_emprunt):
		self.adherent = Adherent  			#Nom de l'adhérent
		self.jeu = Jeu 						#Nom du jeu emprunté
		self.date_emprunt = date_emprunt 	#Date d'emprunt sous la forme de tableau [j(j), m(m), aaaa]
		self.date_echeance = calcul_echeance(self)

	def get_adherent (self):
		return(self.adherent)

	def get_jeu (self):
		return(self.jeu)

	def get_date_emprunt (self):
		return(self.date_emprunt)

	def get_date_echeance (self):
		return(self.date_echeance)

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

	def est_en_retard (self, date_retour):
		date_echeance = self.date_echeance
		retard = (date_retour[0] > date_echeance[0] and date_retour[1] == date_echeance[1]) or (date_retour[1] > date_echeance[1]) or (date_retour[2] > date_echeance[2]) 
		 #si on rend trop tard retard = True
		return (retard)
"""
	def calcul_retard (self):

"""





