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
import EnsCategories

class Jeu:

    def __init__(self,Jeu_id=None,Nom_jeu="",Annee="",Editeur="",AgeMini="",NombreJoueurs="",Description="",Categorie_id=None):
        self.Jeu_id = Jeu_id
        self.Nom_jeu = Nom_jeu
        self.Annee = Annee
        self.Editeur = Editeur
        self.AgeMini = AgeMini
        self.NombreJoueurs = NombreJoueurs
        self.Description = Description
        self.Categorie_id = Categorie_id

###### GETTERS ########
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

    def get_NombreJoueurs(self):
        return self.NombreJoueurs
    def get_Editeur(self):
        return self.Editeur
    def get_Annee(self):
        return self.Annee

    def get_Categorie_id(self):
        return self.Categorie_id

    def set_Categorie_id(Categorie_id):
        if EnsCategories.categorieExiste():
            self.Categorie_id = Categorie_id
            # AJOUTER FONCTION UPDATE
        else:
            print ("Oops, la categorie n'existe pas !")



###### SETTERS ########
    def set_Nom_jeu(self,Nom_jeu):
        self.Nom_jeu = Nom_jeu
        self.save()
    def set_AgeMini(self,AgeMini):
        self.AgeMini = AgeMini
        self.save()
    def set_Description(self,Description):
        self.Description = Description
        self.save()
    def set_NombreJoueurs(self,NombreJoueurs):
        self.NombreJoueurs=NombreJoueurs
        self.save()
    def set_Editeur(self,Editeur):
        self.Editeur = Editeur
        self.save()
    def set_Annee(self,Annee):
        self.Annee = Annee
        self.save()

    def supprimer_Exemplaire(self):
        try:
            Exemplaire=EnsExemplaires.get_Exemplaire_dispo(self)
            EnsExemplaires.supprimerExemplaire(Exemplaire)
        except:
            print ("[ERREUR] Jeu :: Erreur lors de la suppression !")
            raise



    def save(self):

        if (self.Jeu_id==None):
            EnsJeux.insert(self)
        else:
            EnsJeux.update(self)
