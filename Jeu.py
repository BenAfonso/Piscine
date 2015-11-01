# -*- coding: utf-8 -*-
### Type Jeu : Jeu

# Représentation des données:
#
# idJeu : int (UNIQUE)
# nomJeu : String
# nbExemplaire : int (calculé FAIRE FONCTION)
# disponibilité: bool (faire fonction)
# 

# Fonctionnalités:
#
# get_jeu : idJeu --> Jeu
# get_nombre_exemplaire : idJeu --> int
# set_nom_jeu: String x Jeu --> Jeu
# set_description_jeu: String x Jeu --> Jeu
# new_jeu: String x String --> Jeu
# est_disponible : idJeu --> bool
#
#
from EnsJeux import EnsJeux

class Jeu:

    def __init__(self,Jeu_id=0,Nom_jeu="",AgeMini="",Description=""):
        Ens=EnsJeux()
        if (Jeu_id==0):
            self.Jeu_id = Jeu_id
            self.Nom_jeu = Nom_jeu
            self.AgeMini = AgeMini
            self.Description = Description
        else:
            Jeu=Ens.get_Jeu(Jeu_id)
            self.Jeu_id = Jeu_id
            self.Nom_jeu = Jeu[1]
            self.AgeMini = Jeu[2]
            self.Description = Jeu[3]

    def get_Nom_jeu(self):
        return self.Nom_jeu

    def get_AgeMini(self):
        return self.AgeMini

    def get_Description(self):
        return self.Description

    def get_Jeu_id(self):
        return self.Jeu_id

    def set_Nom_jeu(self,Nom_jeu):
        self.Nom_jeu = Nom_jeu

    def set_AgeMini(self,AgeMini):
        self.AgeMini = AgeMini

    def set_Description(self,Description):
        self.Description = Description

    def set_Jeu_id(self,Jeu_id):
        self.Jeu_id = Jeu_id

    def save(self):
        listeJeux = EnsJeux()
        Jeu = [self.Jeu_id,self.Nom_jeu,self.AgeMini,self.Description]
        listeJeux.insert(Jeu)


   
    

   
    
