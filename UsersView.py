#-*-coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import EnsUtilisateurs
import EnsEmprunt
from UserView import UserView
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
            currentUser = EnsUtilisateurs.get_user(int(User[0]))
            if (EnsEmprunt.a_un_emprunt_en_cours(currentUser)):
                emprunt = "Oui"
            else:
                emprunt = "Non"
            self.setItem(ligne, 3, QTableWidgetItem(emprunt))
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
            currentUser = EnsUtilisateurs.get_user(int(User[0]))
            if (EnsEmprunt.a_un_emprunt_en_cours(currentUser)):
                emprunt = "Oui"
            else:
                emprunt = "Non"
            self.setItem(ligne, 3, QTableWidgetItem(emprunt))
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



    def ReinitAll(self):
        try:
            reply = QMessageBox.question(self, 'Attention',
            u"Vous êtes sur le point de réinitialiser TOUS les abonnements.\nÊtes vous sûrs de vouloir continuer ?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                EnsUtilisateurs.reinitAbonnements()
                self.refresh()
        except:
            self.criticalError()


    def AddUser(self): # Popup pour ajouter un jeu

        self.AddUser = QDialog()
        Username = QLabel("Nom d'Utilisateur: ")
        self.UsernameText = QLineEdit()

        Password = QLabel("Mot de passe: ")
        self.PasswordText = QLineEdit()
        self.PasswordText.setEchoMode(QLineEdit.Password)

        Password2 = QLabel(u"Ré-entrez le mot de passe: ")
        self.PasswordText2 = QLineEdit()
        self.PasswordText2.setEchoMode(QLineEdit.Password)

        # Test si PasswordText1 = PasswordText2
        self.SubmitButton = QPushButton(u"Créer")


        Layout = QVBoxLayout()
        Layout.addWidget(Username)
        Layout.addWidget(self.UsernameText)
        Layout.addWidget(Password)
        Layout.addWidget(self.PasswordText)
        Layout.addWidget(Password2)
        Layout.addWidget(self.PasswordText2)
        Layout.addWidget(self.SubmitButton)
        self.AddUser.setLayout(Layout)
        self.SubmitButton.clicked.connect(self.newUser)
        self.AddUser.exec_()


    def newUser(self):
        if str(self.PasswordText.text()) == str(self.PasswordText2.text()) and len(str(self.PasswordText.text())) > 3 and len(str(self.UsernameText.text())) > 2:
            # CONFIRMATION ?
            newuser=EnsUtilisateurs.Utilisateur(username=str(self.UsernameText.text()),password=str(self.PasswordText.text()))
            newuser.save()

            QMessageBox.information(self, u"Voilà !",
            u"L'utilisateur a été ajouté !",
            QMessageBox.Ok, QMessageBox.NoButton,
            QMessageBox.NoButton)
            self.AddUser.close()
            self.parent().parent().user()

        else:
            QMessageBox.critical(self, "ERREUR !",
            "Erreur lors de la creation de l'utilisateur.",
            QMessageBox.Ok, QMessageBox.NoButton,
            QMessageBox.NoButton)

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
        #selection = QMessageBox.information(self,
        #self.trUtf8("Selection"),
        #self.trUtf8("Vous avez séléctionné l'utilisateur: \nID: "+item+" \nNom d'utilisateur: "+self.item(row,1).text()+"\nStatut: "+statut))
        # Changer vue vers 1 Seul User et sa fiche !
        User = UserView(item=item,session=self.parent().parent().session)
    	# JEU VIEW ? OU POPUP.
        self.close()
        self.parent().parent().setCentralWidget(User)

    def refresh(self):
        self.parent().parent().user()

    def criticalError(self):
        QMessageBox.critical(self, "ERREUR !",
        "Oops ! Une erreur est survenue ",
        QMessageBox.Cancel, QMessageBox.NoButton,
        QMessageBox.NoButton)
