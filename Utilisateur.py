### Type Utilisateur

# username : string
# password : string
# 

import EnsUtilisateurs
import EnsAdmins

class Utilisateur:

    def __init__(self,user_id=None,username="",password="",abonnementValide=False,empruntEnCours = False,reservationEnCours = False,nbRetard = 0):
        
        self.user_id = user_id
        self.username = username
        self.password = password
        if (user_id == None):
            self.abonnementValide = abonnementValide
            self.empruntEnCours = empruntEnCours
            self.reservationEnCours = reservationEnCours
            self.nbRetard = nbRetard
        else:
            self.abonnementValide = abonnementValide
            self.empruntEnCours = empruntEnCours
            self.reservationEnCours = reservationEnCours
            self.nbRetard = nbRetard

##### GETTERS ########
    def get_user_id(self):
        return self.user_id
    def get_username(self):
        return self.username
    def get_password(self):
        return self.password
    def get_abonnementValide(self):
        return self.abonnementValide
    def get_empruntEnCours(self):
        return self.empruntEnCours
    def get_reservationEnCours(self):
        return self.reservationEnCours
    def get_nbRetard(self):
        return self.nbRetard
##### SETTERS #####
    def set_username(self, username):
        self.username = username
    def set_password(self, password):
        self.password = password
    def get_abonnementValide(self):
        return self.abonnementValide
    def get_empruntEnCours(self):
        return self.empruntEnCours
    def get_reservationEnCours(self):
        return self.reservationEnCours
    def get_nbRetard(self):
        return self.nbRetard
##### FONCTIONS ANNEXES #####
    def est_admin(self):
        return EnsAdmins.est_admin(self)

    def make_admin(self):
        if (self.user_id != 0):
            EnsAdmins.insert(self)
        else:
            print "Pas d'utilisateur selectionne !"

    def delete_user(self):
        """Supprime un utilisateur de l'ensemble des EnsUtilisateurs
         (#) Si cet utilisateur est admin => Supprime l'utilisateur de l'ensemble des admins """
        if self.est_admin():
            EnsAdmins.delete_admin(self)
        EnsUtilisateurs.delete_user(self)





    def save(self):
        
        EnsUtilisateurs.insert(self)
        
        # SAVE AN USER IN DATABASE

    

    



   
    
