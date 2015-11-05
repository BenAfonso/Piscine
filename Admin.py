### Type Utilisateur

# username : string
# password : string
# 

import EnsAdmins

class Admin:

    def __init__(self,User):
        self.user_id = User.get_user_id()

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
            EnsAdmins.insert(self)
        else:
            print "Pas d'utilisateur selectionne !"


    def save(self):
        EnsUtilisateurs.insert(self.get_username(),self.get_password())
        
        # SAVE AN USER IN DATABASE

    

    



   
    
