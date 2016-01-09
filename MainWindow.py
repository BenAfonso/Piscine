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
from EmpruntsView import EmpruntsView
from ProfileView import ProfileView

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Definition de la zone centrale de la fenetre
        zoneCentrale = QWidget()
        self.session = None
        # Connexion :: Ouverture du widget
        self.toolbar = None
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
        ## On fixe la toolbar pour plus qu'elle bouge.
        self.toolbar.setMovable(False)

        # Ajout d'items (=> Actions)
        # ICONES ?
        self.toolbar.addAction(QIcon('img/icon.png'),'Jeux',self.jeux)
        # Sans ICONES ?
        #self.toolbar.addAction('Jeux',self.jeux)


        # Affichage de ce bouton seulement pour les admins
        if EST_ADMIN:
            self.toolbar.addSeparator();
            # ICONES ?
            self.toolbar.addAction(QIcon('img/user.png'),'Utilisateurs',self.user)
            # Sans ICONES
            #self.toolbar.addAction('Utilisateurs',self.user)
            self.toolbar.addSeparator();
            self.toolbar.addAction("Emprunts",self.emprunts)
            self.toolbar.addSeparator();
        # Séparation pour avoir les widgets à droite
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.toolbar.addWidget(spacer)

        # Profil & Deconnexion
        self.toolbar.addSeparator();
        self.toolbar.addAction(USERNAME,self.profile)
        self.toolbar.addSeparator();
        self.toolbar.addAction('Deconnexion',self.logout)
        self.jeux()

        # Création d'une toolbar de menu



    def logout(self):

        self.toolbar.close()
        del self.session
        self.connexion()


    def connexion(self):

        if self.toolbar != None:
            self.toolbar.close()
        self.toolbar = self.addToolBar('ToolBar')
        # On fixe la toolbar
        self.toolbar.setMovable(False)

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


    def profile(self):
        Profile=ProfileView(self.session)
        self.setCentralWidget(Profile)

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
        ReinitAll = QPushButton(u"Ré-initialiser tous abonnements")
        Buttons.addWidget(ReinitAll)
        #  Ajout du conteneur horizontal au conteneur principal (vertical)
        VLayout.addLayout(Buttons)
        # On affecte le layout vertical au widget
        widget.setLayout(VLayout)
        #  On change le widget central !
        self.setCentralWidget(widget)
        AddUser.clicked.connect(self.Users.AddUser)
        ReinitAll.clicked.connect(self.Users.ReinitAll)


    def emprunts(self):
        Emprunts=EmpruntsView()
        self.setCentralWidget(Emprunts)

    def jeux(self): # WIDGET JEUX
        if self.session == None:
            self.toolbar.close()
            self.toolbar = self.addToolBar('ToolBar')

            #On refixe la toolbar.
            self.toolbar.setMovable(False)

            # Ajout d'items (=> Actions)
            self.toolbar.addAction(QIcon('img/icon.png'),'Jeux',self.jeux)


            # Séparation pour avoir les widgets à droite
            spacer = QWidget()
            spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.toolbar.addWidget(spacer)

            # Deconnexion
            self.toolbar.addAction('Se connecter',self.connexion)
        Jeux=JeuxView(session=self.session)
        self.setCentralWidget(Jeux)

    def rechercheUser(self):
        self.Users.searchmydata(str(self.RechercheText.text()))
