# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
import EnsUtilisateurs
from Connexion import Connexion
from Session import Session
import EnsAdmins

class ConnexionView(QtGui.QWidget):
	def __init__(self):
		super(ConnexionView, self).__init__()
		self.usernameText = None
		self.passwordText = None
		self.state=False
		self.grid=QtGui.QGridLayout()
		self.initUI()


	def initUI(self):
		
		username = QtGui.QLabel("Nom d'utilisateur: ")
		password = QtGui.QLabel("Mot de passe: ")
		self.usernameText = QtGui.QLineEdit()
		self.passwordText = QtGui.QLineEdit()
		self.passwordText.setEchoMode(QtGui.QLineEdit.Password) # Masquer un mot de passe
		ok = QtGui.QPushButton("Se connecter",self)
		ok.clicked.connect(self.ouvrirDialogue)

		#grid.setSpacing(4)
		

		self.grid.addWidget(username,1,1,1,2)
		self.grid.addWidget(self.usernameText,2,1,1,2)

		self.grid.addWidget(password,3,1,1,2)
		self.grid.addWidget(self.passwordText,4,1,1,2)
		self.grid.addWidget(ok,5,2)

		self.setLayout(self.grid)

		self.setGeometry(200,50,200,40)
		self.setWindowTitle(':: LudoConnexion ::')

		self.show()

	def ouvrirDialogue(self): # Renvoie le résultat de la connexion
		username=str(self.usernameText.text()) # Récupération des entrées 
		password=str(self.passwordText.text())
		conn=Connexion(username,password) # Création d'une connexion avec les paramètres des textboxes
		
		if conn.est_valide():
			reponse = QtGui.QMessageBox.information(self,    # Création d'une message box d'information (SUCCES)
             self.trUtf8("Bienvenue"), 
             self.trUtf8("Bienvenue "+username))
			self.state = True
			self.close()

		else:
			QtGui.QMessageBox.warning(self, 		# Création d'une message box d'avertissement (ECHEC)
             self.trUtf8("Erreur"), 
             self.trUtf8("Nom d'utilisateur et/ou mot de passe incorrect !"))
			self.state=False



