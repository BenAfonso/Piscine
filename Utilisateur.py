### Type Utilisateur

# username : string
# password : string
# 

from EnsUtilisateurs import EnsUtilisateurs
from EnsAdmins import EnsAdmins

class Utilisateur:

    def __init__(self,username="",password="",user_id=0):
        Ens = EnsUtilisateurs()
        self.user_id = user_id
        if (user_id == 0):
            self.username = username
            self.password = password
        else:
            self.username = Ens.get_username(user_id)
            self.password = Ens.get_password(user_id)

    def get_user(self):
        return [self.username,self.password]
    
    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    def make_admin(self):
        if (self.user_id != 0):
            AdminListe = EnsAdmins()
            AdminListe.insert(self.user_id)
        else:
            print "Pas d'utilisateur selectionne !"


    def save(self):
        Userlist = EnsUtilisateurs()
        Userlist.insert(self.get_username(),self.get_password())
        
        # SAVE AN USER IN DATABASE

    

    



   
    
