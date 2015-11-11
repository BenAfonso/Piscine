#! /usr/bin/python
#-*-coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from JeuxView import JeuxView
from UsersView import UsersView
from functools import partial

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Definition de la zone centrale de la fenetre
        zoneCentrale = QWidget()

        # Création d'une toolbar de menu
        self.toolbar = self.addToolBar('ToolBar')
            # Ajout d'items (=> Actions)
        self.toolbar.addAction(QIcon('img/icon.png'),'Jeux',self.jeux)
        self.toolbar.addAction(QIcon('img/user.png'),'Utilisateurs',self.user)
        

      

        # Paramètres de la fenêtre
        self.resize(500,350)    # Taille
        self.setWindowTitle("Gestion Ludotheque") # Titre
        self.setWindowIcon(QIcon('img/game.png')) # Icône



    def user(self): # WIDGET USERS
        widget = QWidget()
        # Création du widget
        self.Users = UsersView()
        # Conteneur Vertical
        VLayout = QVBoxLayout() 
        # Element 1 du Conteneur Vertical : Label


        VLayout.addWidget(QLabel("Utilisateurs")) 

        # Layout de recherche
        RechercheLayout = QHBoxLayout()

        self.RechercheText = QLineEdit()

        RechercheButton = QPushButton("Rechercher")

        self.RechercheText.textEdited.connect(self.rechercheUser)
        # Ajout des widgets au layout de recherche
        RechercheLayout.addWidget(self.RechercheText)
        RechercheLayout.addWidget(RechercheButton)
        

        

        # Ajout du layout de recherche au layout principal
        VLayout.addLayout(RechercheLayout)

        # Connexion:
        
        VLayout.addWidget(self.Users)
        # Conteneur Horizontal pour boutons
        Buttons = QHBoxLayout() 
        # Ajout d'un bouton (2)
        AddUser = QPushButton("Ajouter un Utilisateur")
        Buttons.addWidget(AddUser) 
        #  Ajout du conteneur horizontal au conteneur principal (vertical)
        VLayout.addLayout(Buttons) 
        # On affecte le layout vertical au widget
        widget.setLayout(VLayout) 
        #  On change le widget central !
        self.setCentralWidget(widget)
        AddUser.clicked.connect(self.Users.AddUser)

        
    def jeux(self): # WIDGET JEUX
        widget = QWidget()
        # Création du widget
        self.Jeux = JeuxView()
        # Conteneur Vertical
        VLayout = QVBoxLayout() 
        # Element 1 du Conteneur Vertical : Label


        VLayout.addWidget(QLabel("Jeux")) 

        # Layout de recherche
        RechercheLayout = QHBoxLayout()

        self.RechercheText = QLineEdit()

        RechercheButton = QPushButton("Rechercher")

        self.RechercheText.textEdited.connect(self.rechercheJeu)
        # Ajout des widgets au layout de recherche
        RechercheLayout.addWidget(self.RechercheText)
        RechercheLayout.addWidget(RechercheButton)
        

        

        # Ajout du layout de recherche au layout principal
        VLayout.addLayout(RechercheLayout)

        # Connexion:
        
        VLayout.addWidget(self.Jeux)
        # Conteneur Horizontal pour boutons
        Buttons = QHBoxLayout() 
        # Ajout d'un bouton (2)
        AddJeu = QPushButton("Ajouter un jeu")
        Buttons.addWidget(AddJeu) 
        #  Ajout du conteneur horizontal au conteneur principal (vertical)
        VLayout.addLayout(Buttons) 
        # On affecte le layout vertical au widget
        widget.setLayout(VLayout) 
        #  On change le widget central !
        self.setCentralWidget(widget)
        AddJeu.clicked.connect(self.Jeux.AddJeu)

    def rechercheJeu(self):
        self.Jeux.searchmydata(str(self.RechercheText.text()))
    def rechercheUser(self):
        self.Users.searchmydata(str(self.RechercheText.text()))

        

