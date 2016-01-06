#-*-coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import EnsJeux

import sys




class JeuView(QWidget):
    def __init__(self,item="", *args):
        # ESPACEMENT
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)


        self.Display = QWidget()
        self.Display.setMinimumSize(300, 300)
        self.item = int(item)
        QWidget.__init__(self)
        HBox1 = QHBoxLayout()

        Grid = QVBoxLayout()


        # Titre Principale
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(36)
        selectedGame=EnsJeux.get_Jeu(self.item)
        Titre = QLabel(str(selectedGame.get_Nom_jeu()))
        Titre.setFont(font)

        HBox1.addWidget(spacer)
        HBox1.addWidget(Titre)
        HBox1.addWidget(spacer)

        Grid.addLayout(HBox1)
        Grid.addWidget(spacer)


        # TOUS LES CHAMPS
        NomJeuTxt = QLabel("Nom du jeu: ")
        NomJeu=QLabel(str(selectedGame.get_Nom_jeu()))
        EditeurTxt = QLabel("Editeur: ")
        Editeur=QLabel(str(selectedGame.get_Editeur()))
        AnneeTxt=QLabel("Annee: ")
        Annee=QLabel(str(selectedGame.get_Annee()))
        AgeMinTxt=QLabel("Age minimum: ")
        AgeMin=QLabel(str(selectedGame.get_AgeMini()))
        NbJoueursTxt=QLabel("Nombre de joueurs: ")
        NbJoueurs=QLabel(str(selectedGame.get_NombreJoueurs()))
        NbExTxt=QLabel("Nombre d'exemplaires: ")
        NbEx=QLabel(str(selectedGame.get_nombre_exemplaires()))
        NbExDispoTxt=QLabel("Nombre d'exemplaires disponibles: ")
        NbExDispo=QLabel(str(selectedGame.get_nombre_exemplaires_dispo()))





        # ESPACEMENT
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        Grid.addWidget(spacer)

        Grid.addWidget(QPushButton("Emprunter"))




        self.setLayout(Grid)
