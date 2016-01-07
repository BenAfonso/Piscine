### Type Utilisateur

# username : string
# password : string
#

import EnsUtilisateurs
import EnsAdmins
import EnsEmprunt

class Utilisateur:

    def __init__(self,user_id=None,username="",password="",abonnementValide=False,empruntEnCours = False,reservationEnCours = False,nbRetard = 0):

        self.user_id = user_id
        self.username = username
        self.password = password
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
        self.save()
    def set_password(self, password):
        self.password = password
        self.save()
    def set_abonnementValide(self, Nbool):
        self.abonnementValide= Nbool
        self.save()
    def set_empruntEnCours(self,empruntEnCours):
        self.empruntEnCours = empruntEnCours
        self.save()
    def set_reservationEnCours(self, reservationEnCours):
        self.reservationEnCours = reservationEnCours
        self.save()
    def set_nbRetard(self, nbRetard):
        self.nbRetard = nbRetard
        self.save()

    def ajout_Retard(self,nbRetard):
        self.nbRetard = self.nbRetard + nbRetard
        self.save()


##### FONCTIONS ANNEXES #####
    def est_admin(self):
        return EnsAdmins.est_admin(self)

    def make_admin(self):
        if (self.user_id != 0):
            EnsAdmins.insert(self)
        else:
            print "Pas d'utilisateur selectionne !"

    def remove_admin(self):
        if (self.user_id != 0 and self.est_admin()):
            EnsAdmins.delete_admin(self)


    def delete_user(self):
        """Supprime un utilisateur de l'ensemble des EnsUtilisateurs
         (#) Si cet utilisateur est admin => Supprime l'utilisateur de l'ensemble des admins """
        if self.est_admin():
            EnsAdmins.delete_admin(self)
        EnsUtilisateurs.delete_user(self)

    def peut_emprunter(self):
        return (not(EnsEmprunt.a_un_emprunt_en_cours(self)) and self.abonnementValide)





    def save(self):
        if self.user_id == None:
            EnsUtilisateurs.insert(self)
        else:
            EnsUtilisateurs.update(self)

        # SAVE AN USER IN DATABASE
