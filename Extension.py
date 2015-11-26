# -*- coding: utf-8 -*-
### Type Extension : Extension

# Représentation des données:
#
# idExtension : int (UNIQUE)
# idJeu : int
# nomExtension : String
# anneeExtension : int 
# disponible: bool
# anneeExtension : Int
# editeurExtension : String
# ageminiExtension : Int
# nombrejoueursExtension : String
# descriptionExtension : String


import EnsJeux

class Extension:
    def __init__(self,Extension_id=None, Jeu_id = int(0), Nom_Extenion="", Disponible=True):
        self.Extension_id = Extension_id
        self.Jeu_id = Jeu_id
        self.Disponible = Disponible
        self.Nom_Extenion = Nom_Extenion

###### GETTERS ########
    def get_Id_Jeu_Associe(self):
        return self.Jeu_id

    def get_Disponible(self):
        return self.Disponible
	
    def get_Nom_Extension(self):
        return self.Nom_Extenion

   
    def get_Extension_id(self):
        return self.Extension_id

    


###### SETTERS ########
	
    def set_Id_Jeu_Associe(self,Jeu):
        self.Jeu_id = Jeu.get_Jeu_id()
    
    def set_Disponible(self,Disponible):
        self.Disponible = Disponible
    
    def set_Nom(self,Nom):
        self.Nom_Extenion = Nom_Extenion

    def save_Extension(self):
        print("TEST")
        if (self.Extension_id==None):
            EnsExtension.ajouter_Extension(self)
        else:
            EnsExtension.update(self)

