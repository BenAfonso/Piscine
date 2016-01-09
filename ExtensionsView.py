#-*-coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import EnsExtensions
import EnsJeux

import sys




class ExtensionsView(QTableWidget):
    def __init__(self, selectedGame=None,session=None,*args):
        QWidget.__init__(self)
        self.session = session
        self.Table = QTableWidget()
        self.selectedGame=selectedGame
        # On défini le nombre de colonnes

        self.Table.setSortingEnabled(True)
        self.Table.setMinimumSize(800, 300)
        self.Table.setColumnCount(2)
        self.Table.setRowCount(EnsExtensions.nombre_Extensions())
        self.setheaders()
        self.setmydata()
        self.selectedGame=selectedGame
        # Selection de lignes activé
        self.Table.setSelectionBehavior(self.SelectRows)
        # Pas de sélection de cellule
        self.Table.setSelectionMode(self.NoSelection)  # Desactive la selection de lignes
        self.Table.setEditTriggers(QAbstractItemView.NoEditTriggers) # Desactive l'edition de cellules
        self.Table.setFocusPolicy(Qt.NoFocus)
        self.Table.setAlternatingRowColors(True)
        self.Table.verticalHeader().hide()
        # Affichage de la grille désactivé
        self.Table.setShowGrid(False)
        self.Table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Table.horizontalHeader().setStretchLastSection(True)


        AddExtension=QPushButton("Ajouter extension")
        VLayout = QVBoxLayout()
        VLayout.addWidget(self.Table)
        if self.session!=None and self.session.est_admin():
            VLayout.addWidget(AddExtension)
        self.setLayout(VLayout)

        AddExtension.clicked.connect(self.AddExtension)
        self.Table.cellDoubleClicked.connect(self.selectedExtension)


    def resizeEvent(self, event):
        selfsz = event.size().width()
        totalprops = sum(self.Table.hedprops)
        newszs = [sz * selfsz / totalprops for sz in self.Table.hedprops]
        for i, sz in enumerate(newszs):
            self.Table.horizontalHeader().resizeSection(i, sz)
        self.Table.updateGeometry()
        self.Table.showMaximized()
        self.Table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)


        #self.resizeColumnsToContents()
        #self.resizeRowsToContents()


    # Fonction permettant d'initialiser le contenu de l'affichage (remplacer par searchmydata)
    def setmydata(self):
        ligne = 0
        Extensions =EnsExtensions.rechercher_Extensions_Jeu(self.selectedGame)
        for Extension in Extensions:
            currentExtension = EnsExtensions.get_Extension(int(Extension[0]))


            self.Table.setItem(ligne, 0, QTableWidgetItem(str(currentExtension.get_Extension_id())))
            if currentExtension.get_Disponible():
                self.Table.item(ligne, 0).setBackground(QColor(178,255,102))
            else:
                self.Table.item(ligne, 0).setBackground(QColor(255,102,102))
            self.Table.setItem(ligne, 1, QTableWidgetItem(str(currentExtension.get_Nom_Extension())))


            ligne=ligne+1

    def setheaders(self):
        # On définit l'entête des colonnes
        hedlabels = ('ID', "Nom extension")
        # Largeur initiale des colonnes
        self.Table.hedprops = (5,50)
        # On ajoute les colonnes au tableau
        self.Table.setHorizontalHeaderLabels(hedlabels)
        for i, taille in enumerate(self.Table.hedprops):
            self.Table.horizontalHeader().resizeSection(i, taille)



    def AddExtension(self): # Popup pour ajouter un jeu

        self.AddExtension = QDialog()
        NomExtension = QLabel("Nom extension: ")
        self.NomExtensionText = QLineEdit()

        # Checkbox disponible ?

        self.SubmitButton = QPushButton(u"Créer")


        Layout = QVBoxLayout()
        Layout.addWidget(NomExtension)
        Layout.addWidget(self.NomExtensionText)

        Layout.addWidget(self.SubmitButton)
        self.AddExtension.setLayout(Layout)
        self.SubmitButton.clicked.connect(self.newExtension)
        self.AddExtension.exec_()


    def newExtension(self):
        if len(str(self.NomExtensionText.text())) > 3:
            # CONFIRMATION ?
            newextension=EnsExtensions.Extension(Jeu_id=str(self.selectedGame.get_Jeu_id()),Nom_Extension=str(self.NomExtensionText.text()))
            newextension.save_Extension()

            QMessageBox.information(self, u"Voilà !",
            u"L'extension a bien été ajouté !",
            QMessageBox.Ok, QMessageBox.NoButton,
            QMessageBox.NoButton)
            self.AddExtension.close()
            self.refresh()

        else:
            QMessageBox.critical(self, "ERREUR !",
            u"Erreur lors de la création de l'extension.",
            QMessageBox.Ok, QMessageBox.NoButton,
            QMessageBox.NoButton)

    def selectedExtension(self):
        row = self.Table.currentItem().row()
        print "row=",row
        col = self.Table.currentItem().column()
        print "col=",col
        item = self.Table.item(row,0).text()
        print "item=",item

        self.Extension = QDialog()
        Layout = QVBoxLayout()

        self.currentExtension=EnsExtensions.get_Extension(str(item))
        NomExtension=QLabel(str(self.currentExtension.get_Nom_Extension()))
        Layout.addWidget(NomExtension)


        Emprunter=QPushButton("Emprunter")
        Reserver=QPushButton("Reserver")
        Modifier=QPushButton("Modifier")
        Supprimer=QPushButton("Supprimer")

        Layout.addWidget(Emprunter)
        Layout.addWidget(Reserver)
        if self.session != None and self.session.est_admin():
            Layout.addWidget(Modifier)
            Layout.addWidget(Supprimer)


        ### Edition des liens
        Emprunter.clicked.connect(self.emprunter)
        Reserver.clicked.connect(self.reserver)
        Modifier.clicked.connect(self.modifier)
        Supprimer.clicked.connect(self.supprimer)

        self.Extension.setLayout(Layout)
        self.Extension.exec_()


        self.close()
        self.refresh()

    def refresh(self):
        Ext=ExtensionsView(self.selectedGame,self.session)
        self.parent().setCentralWidget(Ext)

    def criticalError(self):
        QMessageBox.critical(self, "ERREUR !",
        "Oops ! Une erreur est survenue ",
        QMessageBox.Cancel, QMessageBox.NoButton,
        QMessageBox.NoButton)

    #### A FAIRE ####:

    #Fonction modifier:
    def modifier(self):
        self.Extension.close()
        self.ModifierExtension = QDialog()
        NomExtension = QLabel("Nom extension: ")
        self.NomExtensionText = QLineEdit()
        self.NomExtensionText.setText(str(self.currentExtension.get_Nom_Extension()))
        self.SubmitButton = QPushButton(u"Modifier")


        Layout = QVBoxLayout()
        Layout.addWidget(NomExtension)
        Layout.addWidget(self.NomExtensionText)

        Layout.addWidget(self.SubmitButton)
        self.ModifierExtension.setLayout(Layout)
        self.SubmitButton.clicked.connect(self.updateExt)
        self.ModifierExtension.exec_()

    #Fonction effectuant les modification nécessaires lors de la modification d'une extension
    def updateExt(self):
        self.currentExtension.set_Nom(str(self.NomExtensionText.text()))
        self.ModifierExtension.close()

    #Fonction Supprimer:
    def supprimer(self):
        reply = QMessageBox.question(self, 'Confirmation',
        u"Êtes vous sur de vouloir supprimer l'extension "+str(self.currentExtension.get_Nom_Extension()), QMessageBox.Yes |
        QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            try:
                EnsExtensions.supprimer_Extension(self.currentExtension)
                QMessageBox.information(self, "Fait !",
                u"L'extension a bien été supprimé !",
                QMessageBox.Ok, QMessageBox.NoButton,
                QMessageBox.NoButton)
                self.refresh()
                self.Extension.close()
            except:
                QMessageBox.critical(self, "ERREUR !",
                "Erreur lors de la suppression de l'extension !",
                QMessageBox.Ok, QMessageBox.NoButton,
                QMessageBox.NoButton)


    #### A FAIRE ####

    def emprunter(self):
        # Si l'extension est disponible
        # Si l'extension appartient au jeu de l'emprunt en cours
        # Si l'user n'a pas d'emprunt en cours
        QMessageBox.critical(self, "ERREUR !",
        u"Fonctionnalité pas encore disponible !",
        QMessageBox.Ok, QMessageBox.NoButton,
        QMessageBox.NoButton)

    def reserver(self):
        QMessageBox.critical(self, "ERREUR !",
        u"Fonctionnalité pas encore disponible !",
        QMessageBox.Ok, QMessageBox.NoButton,
        QMessageBox.NoButton)



    #Fonction Emprunter:

    #Fonction Reserver:
