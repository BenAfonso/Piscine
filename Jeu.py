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
import EnsJeux
import EnsExemplaires

class Jeu:

    def __init__(self,Jeu_id=None,Nom_jeu="",AgeMini="",Description=""):
        self.Jeu_id = Jeu_id
        self.Nom_jeu = Nom_jeu
        self.AgeMini = AgeMini
        self.Description = Description

    def get_Nom_jeu(self):
        return self.Nom_jeu

    def get_AgeMini(self):
        return self.AgeMini

    def get_Description(self):
        return self.Description

    def get_Jeu_id(self):
        return self.Jeu_id

    def get_nombre_exemplaires(self,disponible=2):
        return EnsExemplaires.get_nombre_exemplaires(self,disponible)

    def get_nombre_exemplaires_dispo(self,disponible=1):
        return EnsExemplaires.get_nombre_exemplaires(self,disponible)

    def set_Nom_jeu(self,Nom_jeu):
        self.Nom_jeu = Nom_jeu

    def set_AgeMini(self,AgeMini):
        self.AgeMini = AgeMini

    def set_Description(self,Description):
        self.Description = Description




    def save(self):
        print("TEST")
        if (self.Jeu_id==None):
            EnsJeux.insert(self)
        else:
            EnsJeux.update(self)


   
    

   
    
