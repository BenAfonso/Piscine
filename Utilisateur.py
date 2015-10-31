### Type Utilisateur

# username : string
# password : string
# 

from EnsUtilisateurs import EnsUtilisateurs

class Utilisateur:

    def __init__(self,username,password):
        self.username = username
        self.password = password

    def get_user(self):
        return self
    
    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    def save(self):
        Userlist = EnsUtilisateurs()
        Userlist.insert(self.get_username(),self.get_password())
        
        # SAVE AN USER IN DATABASE

    

    



   
    
