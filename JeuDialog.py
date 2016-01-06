#-*-coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import EnsJeux

import sys



 
class JeuDialog(QWidget):

    #def __init__(self,item="", *args):
    def __init__(self,item=None):
        self.item=item
        self.initUI()
	
    def initUI(self):
    	#self.item = int(item)
        #QWidget.__init__(self)
    	self.btn=QPushButton('Dialog')
    	self.btn.move(20,20)
    	self.btn.clicked.connect(self.showDialog)
    	self.le = QLineEdit(self)
    	self.le.move(130,22)
    	self.setGeometry(300,300,290,150)
    	self.setWindowTitle('Jeu')
    	self.show()

    def showDialog(self):
    	text, ok = QInputDialog.getText(self, 'Input Dialog','Enter your name:')
    	if ok:
    	    self.le.setText(str(text))
        #selectedGame=EnsJeux.get_Jeu(self.item)
        #NomJeu = QLabel("Nom du jeu: "+str(selectedGame.get_Nom_jeu()))
        #Editeur = QLabel("Editeur: "+str(selectedGame.get_Editeur()))
        #Annee = QLabel("Annee: "+str(selectedGame.get_Annee()))
        #AgeMini = QLabel("Age minimum: "+str(selectedGame.get_AgeMini()))
        #NombreJoueurs = QLabel("Nombre Joueurs: "+str(selectedGame.get_NombreJoueurs()))

        #self.setLayout(Layout)









