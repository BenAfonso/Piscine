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

import EnsExtensions
import EnsJeux

class Extension:

    def __init__(self,Jeu=None,Disponible=True,Nom="",Annee="",Editeur="",AgeMini="",NombreJoueurs="",Description="",Extension_id=None):
        self.Extension_id = Extension_id
		    self.Jeu_id = Jeu.Jeu_id
		    self.Disponible = Disponible
        self.Nom = Nom
        self.Annee = Annee
        self.Editeur = Editeur
        self.AgeMini = AgeMini
        self.NombreJoueurs = NombreJoueurs
        self.Description = Description

###### GETTERS ########
	def get_Id_Jeu_Associe(self):
        return self.Jeu_id

    def get_Disponible(self):
        return self.Disponible
	
	def get_Nom_Extension(self):
        return self.Nom

    def get_AgeMini(self):
        return self.AgeMini

    def get_Description(self):
        return self.Description

    def get_Extension_id(self):
        return self.Extension_id

    def get_NombreJoueurs(self):
        return self.NombreJoueurs
		
    def get_Editeur(self):
        return self.Editeur
		
    def get_Annee(self):
        return self.Annee


###### SETTERS ########
	  def set_Id_Jeu_Associe(self,Jeu):
        self.Jeu_id = Jeu.Jeu_id
    def set_Disponible(self,Disponible):
        self.Disponible = Disponible
    def set_Nom(self,Nom):
        self.Nom = Nom
    def set_AgeMini(self,AgeMini):
        self.AgeMini = AgeMini
    def set_Description(self,Description):
        self.Description = Description
    def set_NombreJoueurs(self,NombreJoueurs):
        self.NombreJoueurs=NombreJoueurs
    def set_Editeur(self,Editeur):
        self.Editeur = Editeur
    def set_Annee(self,Annee):
        self.Annee = Annee


    def save(self):
        print("TEST")
        if (self.Extension_id==None):
            EnsExtension.ajouter_Extension(self)
        else:
            EnsExtension.update(self)

