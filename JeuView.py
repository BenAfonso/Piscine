#-*-coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import EnsJeux

import sys



 
class JeuView(QWidget):
    def __init__(self,item="", *args):
        self.Display = QWidget()
        self.Display.setMinimumSize(300, 300)
    	self.item = int(item)
        QWidget.__init__(self)
        Grid = QGridLayout()
        Grid.setSpacing(0)
        
	Grid.setOriginCorner(Qt.TopLeftCorner)
        selectedGame=EnsJeux.get_Jeu(self.item)
        NomJeu = QLabel("Nom du jeu: "+str(selectedGame.get_Nom_jeu())+"\nEditeur: "+str(selectedGame.get_Editeur())+"\nAnnee: "+str(selectedGame.get_Annee())+"\nAge minimum: "+str(selectedGame.get_AgeMini())+"\nNombre Joueurs: "+str(selectedGame.get_NombreJoueurs()))
        Grid.addWidget(NomJeu,0,0)
        Grid.addWidget(QPushButton("Emprunter"),0,1)


  
        self.setLayout(Grid)









