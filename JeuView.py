#-*-coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import EnsJeux

import sys



 
class JeuView(QWidget):
    def __init__(self,item="", *args):
    	self.item = int(item)
        QWidget.__init__(self)
        Layout = QVBoxLayout()
        FirstLayout = QVBoxLayout()
        Blank = QHBoxLayout()
        Bottom = QHBoxLayout()

        Bottom.addWidget(QPushButton("Emprunter"))

        selectedGame=EnsJeux.get_Jeu(self.item)
        NomJeu = QLabel("Nom du jeu: "+str(selectedGame.get_Nom_jeu()))
        Editeur = QLabel("Editeur: "+str(selectedGame.get_Editeur()))
        Annee = QLabel("Annee: "+str(selectedGame.get_Annee()))
        AgeMini = QLabel("Age minimum: "+str(selectedGame.get_AgeMini()))
        NombreJoueurs = QLabel("Nombre Joueurs: "+str(selectedGame.get_NombreJoueurs()))
        FirstLayout.addWidget(NomJeu)
        FirstLayout.addWidget(Editeur)
        FirstLayout.addWidget(Annee)
        FirstLayout.addWidget(AgeMini)
        FirstLayout.addWidget(NombreJoueurs)
        Layout.addLayout(FirstLayout)
        Layout.addLayout(Blank)
        Layout.addLayout(Bottom)
  
        self.setLayout(Layout)









