# -*- coding: utf-8 -*-
### Type Exemplaire : Exemplaire

import EnsExemplaires

class Exemplaire:

    def __init__(self,Jeu_id,Est_disponible=True,Exemplaire_id=None):
        self.Exemplaire_id = Exemplaire_id
        self.Jeu_id = Jeu_id
        self.Est_disponible = Est_disponible
    #### GETTERS ####

    def get_Jeu_id(self):
        return self.Jeu_id
    def get_Est_disponible(self):
        return self.Est_disponible
    def get_Exemplaire_id(self):
        return self.Exemplaire_id
    #### SETTERS ####
    def set_Jeu_id(self,Jeu_id):
        self.Jeu_id = Jeu_id
    def set_Est_disponible(self,Est_disponible):
        self.Est_disponible = Est_disponible



    def save(self):
        EnsExemplaires.insert(self)


   
    

   
    
