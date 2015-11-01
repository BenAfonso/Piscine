# -*- coding: utf-8 -*-
### Type Exemplaire : Exemplaire

from EnsExemplaires import EnsExemplaires

class Exemplaire:

    def __init__(self,Jeu_id,Exemplaire_id=0):
        self.Exemplaire_id = Exemplaire_id
        self.Jeu_id = Jeu_id

    def get_Jeu_id(self):
        return self.Jeu_id

    def set_Jeu_id(self,Jeu_id):
        self.Jeu_id = Jeu_id

    def save(self):
        listeExemplaires = EnsExemplaires()
        Exemplaire = [self.Exemplaire_id,self.Jeu_id]
        listeExemplaires.insert(Exemplaire)


   
    

   
    
