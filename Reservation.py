#-*- coding:utf-8-*-
import EnsUtilisateurs
import EnsJeux
import EnsExtensions
import EnsExemplaires
import EnsReservation
from datetime import date, datetime, timedelta

# Rajouter implementation de la date (date automatique lors de la creation) voir Classe Emprunt de Jean
# Faire en sorte qu'on rentre des Instances Utilisateurs et non des user (pareil pour exemplaire, ...)
# Jeu inutile parce qu'on a l'exemplaire qui est associé au jeu

class Reservation :

    def __init__(self,Reservation_id = None, user = None, Jeu = None, Extension = None ,Exemplaire = None,date_Reservation = None, Terminer = False) :

        self.Reservation_id = Reservation_id
        self.user = user
        self.Jeu = Jeu
        self.Extension = Extension
        if Reservation_id == None:
            # Test si l'exemplaire est disponible
            if EnsExemplaires.get_nombre_exemplaires(Jeu,disponible=1) > 0:
                self.Exemplaire = EnsExemplaires.get_Exemplaire_dispo(Jeu)
            else:
                self.Exemplaire=None
                print "Oops, ce jeu n'est pas disponible !"
                raise
        self.Terminer = Terminer
        if date_Reservation == None:
            self.date_Reservation = date.today()
        else:
            self.date_Reservation = date_Reservation
            reservation_perime()




  ### GETTERS###

    def get_Reservation_id(self):
        return self.Reservation_id
    def get_user(self):
        return self.user
    def get_Jeu(self):
        return self.Jeu
    def get_Exemplaire_id(self):
        return self.Exemplaire.get_Exemplaire_id()
    def get_date_Reservation(self):
        return self.date_Reservation
    def get_Extension_id(self):
        return self.Extension_id
    def get_Terminer(self):
        return self.Terminer

    ##### SETTERS #####

    def set_user(self, user):
        self.user = user
    def set_Jeu(self, Jeu):
        self.Jeu = Jeu
    def set_Exemplaire_id(self, Exemplaire_id):
        self.Exemplaire_id = Exemplaire_id
    def set_Terminer(self) :
        self.Terminer = True
    def set_Extension_id(self, Extension_id) :
        self.Extension_id = Extension_id
    def set_Reservation_date(self):
        self.date_Reservation = date.today()


  ##### FONCTIONS ANNEXES #####

    def calcul_date_echeance(self):
        # 2 SEMAINES POUR A LA RESERVATION ?
        date_echeance=self.date_Reservation+timedelta(days=15)
        return date_echeance
    # Wtf ?
    def reservation_perime(self):
        if (self.date_Reservation < date.today()):
            self.Terminer = True

    def display(self):
        return "= Nom du jeu: "+str(self.Exemplaire.get_Jeu_Exemplaire().get_Nom_jeu())+"\n= Date Reservation: "+str(self.date_Reservation)+"\n= Valide: "+str(self.Terminer)
    def save(self):
        EnsReservation.Ajouter_Reservation(self)
