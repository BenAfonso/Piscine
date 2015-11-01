### Type Utilisateur

# username : string
# password : string
# 

from EnsAdmins import EnsAdmins

class Admin:

    def __init__(self,user_id):
        self.user_id = user_id

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

    

    



   
    
