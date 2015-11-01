# -*- coding: utf-8 -*-
### Type Exemplaire : Exemplaire

from EnsExemplaires import EnsExemplaires

class Exemplaire:

    def __init__(self,Jeu_id,Est_disponible=True,Exemplaire_id=0):
        self.Exemplaire_id = Exemplaire_id
        self.Jeu_id = Jeu_id
        self.Est_disponible = Est_disponible

    def get_Jeu_id(self):
        return self.Jeu_id

    def set_Jeu_id(self,Jeu_id):
        self.Jeu_id = Jeu_id

    def set_Est_disponible(self,Est_disponible):
        self.Est_disponible = Est_disponible

    def get_Est_disponible(self):
        return self.Est_disponible

    def save(self):
        listeExemplaires = EnsExemplaires()
        Exemplaire = [self.Exemplaire_id,self.Jeu_id,self.Est_disponible]
        listeExemplaires.insert(Exemplaire)


   
    

   
    
