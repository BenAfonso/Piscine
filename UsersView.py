#-*-coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import EnsUtilisateurs

import sys



 
class UsersView(QTableWidget):
    def __init__(self, *args):
        QTableWidget.__init__(self)


        # On défini le nombre de colonnes


        self.setSortingEnabled(True)
        self.setMinimumSize(800, 300)
        self.setColumnCount(5)
        self.setRowCount(EnsUtilisateurs.get_nombre_utilisateurs())
        self.setheaders()
        self.setmydata()

        # Selection de lignes activé
        self.setSelectionBehavior(self.SelectRows)
        # Pas de sélection de cellule
        self.setSelectionMode(self.NoSelection)  # Desactive la selection de lignes
        self.setEditTriggers(QAbstractItemView.NoEditTriggers) # Desactive l'edition de cellules
        self.setFocusPolicy(Qt.NoFocus)
        self.setAlternatingRowColors(True)
        self.verticalHeader().hide()
        # Affichage de la grille désactivé
        self.setShowGrid(False)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.horizontalHeader().setStretchLastSection(True)

        self.cellDoubleClicked.connect(self.selectedUser)
        

    def resizeEvent(self, event):
        selfsz = event.size().width()
        totalprops = sum(self.hedprops)
        newszs = [sz * selfsz / totalprops for sz in self.hedprops]
        for i, sz in enumerate(newszs):
            self.horizontalHeader().resizeSection(i, sz)
        self.updateGeometry()
        self.showMaximized()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        

        #self.resizeColumnsToContents()
        #self.resizeRowsToContents()
        

    # Fonction permettant de modifier le contenu de l'affichage en fonction d'une recherche   
    def searchmydata(self,keyword):
        ligne = 0
        randomChars="%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
        print keyword
        Users = EnsUtilisateurs.rechercher("%%%%%%%%%%%%%%%%"+keyword+"%%%%%%%%%%%%%%%%")
        self.setRowCount(len(Users))
        for User in Users:
            self.setItem(ligne, 0, QTableWidgetItem(str(User[0])))
            self.setItem(ligne, 1, QTableWidgetItem(User[1]))
            self.setItem(ligne, 2, QTableWidgetItem(str(User[3])))
            self.setItem(ligne, 3, QTableWidgetItem(str(User[4])))
            self.setItem(ligne, 4, QTableWidgetItem(str(User[6])))
            ligne=ligne+1

    # Fonction permettant d'initialiser le contenu de l'affichage (remplacer par searchmydata)
    def setmydata(self):
        ligne = 0
        Users = EnsUtilisateurs.printAll()
        for User in Users:
            self.setItem(ligne, 0, QTableWidgetItem(str(User[0])))
            self.setItem(ligne, 1, QTableWidgetItem(User[1]))
            self.setItem(ligne, 2, QTableWidgetItem(str(User[3])))
            self.setItem(ligne, 3, QTableWidgetItem(str(User[4])))
            self.setItem(ligne, 4, QTableWidgetItem(str(User[6])))
            ligne=ligne+1

    def setheaders(self):
        # On définit l'entête des colonnes
        hedlabels = ('ID', "Nom d'utilisateur", 'Abonnement', 'Emprunt', 'Retards')
        # Largeur initiale des colonnes
        self.hedprops = (100, 250, 200, 100, 130)
        # On ajoute les colonnes au tableau
        self.setHorizontalHeaderLabels(hedlabels)
        for i, taille in enumerate(self.hedprops):
            self.horizontalHeader().resizeSection(i, taille)

    def AddUser(self): # Popup pour ajouter un jeu 

        AddUser = QDialog()
        Username = QLabel("Nom d'Utilisateur: ")
        UsernameText = QLineEdit()

        Password = QLabel("Mot de passe: ")
        PasswordText = QLineEdit()
        PasswordText.setEchoMode(QLineEdit.Password)

        Password2 = QLabel(u"Ré-entrez le mot de passe: ")
        PasswordText2 = QLineEdit()
        PasswordText2.setEchoMode(QLineEdit.Password)

        # Test si PasswordText1 = PasswordText2
        SubmitButton = QPushButton(u"Créer")


        Layout = QVBoxLayout()
        Layout.addWidget(Username)
        Layout.addWidget(UsernameText)
        Layout.addWidget(Password)
        Layout.addWidget(PasswordText)
        Layout.addWidget(Password2)
        Layout.addWidget(PasswordText2)
        Layout.addWidget(SubmitButton)
        AddUser.setLayout(Layout)
        AddUser.exec_()
        #AddUser.SubmitButton.clicked.connect(creerJeu)
        

    def selectedUser(self):
        row = self.currentItem().row()
        print "row=",row
        col = self.currentItem().column()
        print "col=",col
        item = self.item(row,0).text()
        print "item=",item
        selected=EnsUtilisateurs.get_user(user_id=int(item))
        if selected.est_admin():
            statut = "Administrateur"
        else:
            statut = "Adhérent"
        selection = QMessageBox.information(self,  
        self.trUtf8("Selection"), 
        self.trUtf8("Vous avez séléctionné l'utilisateur: \nID: "+item+" \nNom d'utilisateur: "+self.item(row,1).text()+"\nStatut: "+statut))
        # Changer vue vers 1 Seul User et sa fiche !






