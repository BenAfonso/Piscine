# -*- coding: utf-8 -*-


import EnsExtensions
import EnsJeux

class Extension:
    def __init__(self,Extension_id=None, Jeu_id = int(0), Nom_Extension="", Disponible=True):
        self.Extension_id = Extension_id
        self.Jeu_id = Jeu_id
        self.Disponible = Disponible
        self.Nom_Extension = Nom_Extension

###### GETTERS ########
    def get_Id_Jeu_Associe(self):
        return self.Jeu_id

    def get_Disponible(self):
        return self.Disponible
	
    def get_Nom_Extension(self):
        return self.Nom_Extension

   
    def get_Extension_id(self):
        return self.Extension_id

    


###### SETTERS ########
	
    def set_Id_Jeu_Associe(self,Jeu):
        self.Jeu_id = Jeu.get_Jeu_id()
    
    def set_Disponible(self,Disponible):
        self.Disponible = Disponible
    
    def set_Nom(self,Nom):
        self.Nom_Extension = Nom_Extension

    def save_Extension(self):
        print("Test de sauvegarde")
        if (self.Extension_id==None):
            EnsExtensions.ajouter_Extension(self)
        else:
            EnsExtensions.update_Extension(self)

