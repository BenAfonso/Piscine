#! /usr/bin/python
#-*-coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from JeuxView import JeuxView
from UsersView import UsersView
from Session import Session
from ConnexionWidget import ConnexionWidget
from Utilisateur import Utilisateur
from functools import partial

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Definition de la zone centrale de la fenetre
        zoneCentrale = QWidget()

        # Connexion :: Ouverture du widget
        self.connexion()

        # Connecté ou non ?






        # Paramètres de la fenêtre
        #self.resize(300,100)    # Taille
        self.setWindowTitle("Gestion Ludotheque") # Titre
        self.setWindowIcon(QIcon('img/game.png')) # Icône
	    #self.jeux()


    def connected(self):
        self.session = self.conn.ActiveSession
        EST_ADMIN = self.session.est_admin()
        USERNAME = self.session.get_session_User().get_username()

        self.toolbar.close()
        self.toolbar = self.addToolBar('ToolBar')

        # Ajout d'items (=> Actions)
        self.toolbar.addAction(QIcon('img/icon.png'),'Jeux',self.jeux)


        # Affichage de ce bouton seulement pour les admins
        if EST_ADMIN:
            self.toolbar.addAction(QIcon('img/user.png'),'Utilisateurs',self.user)

        # Séparation pour avoir les widgets à droite
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.toolbar.addWidget(spacer)

        # Profil & Deconnexion
        self.toolbar.addAction(USERNAME,self.userprofile)
        self.toolbar.addAction('Deconnexion',self.logout)
        self.jeux()

        # Création d'une toolbar de menu


    def userprofile(self):
        return 1

    def logout(self):

        self.toolbar.close()
        del self.session
        self.connexion()


    def connexion(self):

        self.toolbar = self.addToolBar('ToolBar')

        self.setBaseSize(400,200)

        # Séparation pour avoir les widgets à droite
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.toolbar.addWidget(spacer)

        self.toolbar.addAction("Afficher les jeux",self.jeux)

        self.toolbar.addAction('Quitter',self.close)
        self.conn = ConnexionWidget()

        self.setCentralWidget(self.conn)
        self.adjustSize()



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

        Jeux=JeuxView()
        self.setCentralWidget(Jeux)

    def rechercheUser(self):
        self.Users.searchmydata(str(self.RechercheText.text()))
