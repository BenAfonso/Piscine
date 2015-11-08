#! /usr/bin/python
#-*-coding: utf-8 -*-
from PyQt4.QtGui import *
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Definition de la zone centrale de la fenetre
        zoneCentrale = QWidget()

        # Création d'une toolbar de menu
        self.toolbar = self.addToolBar('ToolBar')
            # Ajout d'items (=> Actions)
        self.toolbar.addAction(QIcon('img/user.png'),'Users',self.user)
        self.toolbar.addAction(QIcon('img/icon.png'),'Jeux',self.jeux)
        

      

        # Paramètres de la fenêtre
        self.resize(500,350)    # Taille
        self.setWindowTitle("Gestion Ludotheque") # Titre
        self.setWindowIcon(QIcon('img/game.png')) # Icône



    def user(self): # WIDGET USERS
        # Création du widget
        widget = QWidget()
        # Conteneur Vertical
        VLayout = QVBoxLayout() 
        # Element 1 du Conteneur Vertical : Label
        VLayout.addWidget(QLabel("Utilisateurs")) 
        ## Element 2 du Conteneur Vertical: Debut d'implementation de table
        Table = QTableWidget()
        data = {'ID':['1','2','3'], "Nom d'utilisateur":['Darkyler','Blasfm','Zetsubo']}
        Table1=self.setmydata(Table,data)
        # Ajout de la table au Layout
        VLayout.addWidget(Table1)
        # Conteneur Horizontal pour boutons
        Buttons = QHBoxLayout() 
        # Ajout d'un bouton (2)
        Buttons.addWidget(QPushButton("Ajouter Utilisateur")) 
        #  Ajout du conteneur horizontal au conteneur principal (vertical)
        VLayout.addLayout(Buttons) 
        # On affecte le layout vertical au widget
        widget.setLayout(VLayout) 

        #  On change le widget central !
        self.setCentralWidget(widget) 

        # Fonction pour remplir le Widget Table
    def setmydata(self,Table,data):
 
        horHeaders = []
        for n, key in enumerate(sorted(data.keys())):
            horHeaders.append(key)
            for m, item in enumerate(data[key]):
                newitem = QTableWidgetItem(item)
                #newitem.setFlags(Qt.ItemIsEnabled) # Bloque les cells
                Table.setEditTriggers(QAbstractItemView.NoEditTriggers) # Cells selectionnables seulement
                #newitem.lineEdit.setEchoMode(QLineEdit.Password)
                Table.setItem(m, n, newitem)
        Table.setHorizontalHeaderLabels(horHeaders)
        return Table
        
    def jeux(self): # WIDGET JEUX
        widget = QWidget()
        VLayout = QVBoxLayout() # Conteneur Vertical
        VLayout.addWidget(QLabel("Jeux")) # Ajout d'un Label sur la ligne (1)
        ## Debut d'implementation de table
        Table = QTableWidget()
        VLayout.addWidget(Table)
        Buttons = QHBoxLayout() # Conteneur Horizontal pour boutons
        Buttons.addWidget(QPushButton("Ajouter un Jeu")) # Ajout d'un bouton (2)
        VLayout.addLayout(Buttons) # On réuni les layouts
        widget.setLayout(VLayout) # Layout défini


        self.setCentralWidget(widget) # On change le widget central !
