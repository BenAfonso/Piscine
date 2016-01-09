#-*-coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import EnsJeux
from JeuView import JeuView
from JeuDialog import JeuDialog
from UsersView import UsersView

import sys


class JeuxView(QWidget):
    def __init__(self,session="", *args):
        QWidget.__init__(self)
        self.session = session
        self.Table = QTableWidget()
        # Conteneur Vertical
        VLayout = QVBoxLayout()
        # Element 1 du Conteneur Vertical : Label


        VLayout.addWidget(QLabel("Jeux"))

        # Layout de recherche
        RechercheLayout = QHBoxLayout()

        self.RechercheText = QLineEdit()

        RechercheButton = QPushButton("Rechercher")
        # Ajouter possibilité de rechercher par catégorie (Affichage)
        # Auto refresh recherche
        self.RechercheText.textEdited.connect(self.rechercheJeu)
        # Ajout des widgets au layout de recherche
        RechercheLayout.addWidget(self.RechercheText)
        RechercheLayout.addWidget(RechercheButton)




        # Ajout du layout de recherche au layout principal
        VLayout.addLayout(RechercheLayout)

        # Connexion:

        VLayout.addWidget(self.Table)
        # Conteneur Horizontal pour boutons
        Buttons = QHBoxLayout()
        # Ajout d'un bouton (2)

        AddJeu = QPushButton("Ajouter un jeu")
        if self.session!=None and self.session.est_admin():
            Buttons.addWidget(AddJeu)
        #  Ajout du conteneur horizontal au conteneur principal (vertical)
        VLayout.addLayout(Buttons)
        # On affecte le layout vertical au widget
        self.setLayout(VLayout)
        #  On change le widget central !
        AddJeu.clicked.connect(self.AddJeu)


        self.Table.setSortingEnabled(True)
        self.Table.setMinimumSize(800, 300)
        self.Table.setColumnCount(5)
        self.Table.setRowCount(EnsJeux.get_nombre_jeux())
        self.setheaders()
        self.setmydata()

        # Selection de lignes activé
        self.Table.setSelectionBehavior(self.Table.SelectRows)
        # Pas de sélection de cellule
        self.Table.setSelectionMode(self.Table.NoSelection)
        self.Table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Table.setFocusPolicy(Qt.NoFocus)
        self.Table.setAlternatingRowColors(True)
        self.Table.verticalHeader().hide()
        # Affichage de la grille désactivé
        self.Table.setShowGrid(False)
        self.Table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Table.horizontalHeader().setStretchLastSection(True)

        self.Table.cellDoubleClicked.connect(self.selectedgame)


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


    # Fonction permettant de modifier le contenu de l'affichage en fonction d'une recherche
    def searchmydata(self,keyword):
        ligne = 0
        randomChars="%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
        print keyword
        Jeux = EnsJeux.rechercher("%%%%%%%%%%%%%%%%"+keyword+"%%%%%%%%%%%%%%%%")
        self.Table.setRowCount(len(Jeux))
        for Jeu in Jeux:
            self.Table.setItem(ligne, 0, QTableWidgetItem(str(Jeu[0])))
            self.Table.setItem(ligne, 1, QTableWidgetItem(Jeu[1]))
            self.Table.setItem(ligne, 2, QTableWidgetItem(Jeu[3]))
            self.Table.setItem(ligne, 3, QTableWidgetItem(str(Jeu[2])))
            self.Table.setItem(ligne, 4, QTableWidgetItem(str(Jeu[4])))
            CurrentJeu=EnsJeux.get_Jeu(Jeu[0])
            if CurrentJeu.get_nombre_exemplaires_dispo() > 0:
                self.Table.item(ligne, 0).setBackground(QColor(178,255,102))
            else:
                self.Table.item(ligne, 0).setBackground(QColor(255,102,102))
            ligne=ligne+1

    # Fonction permettant d'initialiser le contenu de l'affichage (remplacer par searchmydata)
    def setmydata(self):
        ligne = 0
        Jeux = EnsJeux.printAll()
        for Jeu in Jeux:
            self.Table.setItem(ligne, 0, QTableWidgetItem(str(Jeu[0])))
            self.Table.setItem(ligne, 1, QTableWidgetItem(Jeu[1]))
            self.Table.setItem(ligne, 2, QTableWidgetItem(Jeu[3]))
            self.Table.setItem(ligne, 3, QTableWidgetItem(str(Jeu[2])))
            self.Table.setItem(ligne, 4, QTableWidgetItem(str(Jeu[5])))
            CurrentJeu=EnsJeux.get_Jeu(Jeu[0])
            if CurrentJeu.get_nombre_exemplaires_dispo() > 0:
                self.Table.item(ligne, 0).setBackground(QColor(178,255,102))
            else:
                self.Table.item(ligne, 0).setBackground(QColor(255,102,102))

            ligne=ligne+1

    def setheaders(self):
        # On définit l'entête des colonnes
        hedlabels = ('ID', 'Nom du jeu', 'Editeur', u'Annee', 'Nb Joueurs')
        # Largeur initiale des colonnes
        self.Table.hedprops = (5,50,30,10,15)
        # On ajoute les colonnes au tableau
        self.Table.setHorizontalHeaderLabels(hedlabels)
        for i, taille in enumerate(self.Table.hedprops):
            self.Table.horizontalHeader().resizeSection(i, taille)

    def AddJeu(self): # Popup pour ajouter un jeu

        self.AddJeuP = QDialog()
        NomJeu = QLabel("Nom du jeu")
        self.NomJeuText = QLineEdit()

        Editeur = QLabel("Editeur")
        self.EditeurText = QLineEdit()


        Annee = QLabel(u"Année")
        self.AnneeText = QLineEdit()

        NombreJoueurs = QLabel("NombreJoueurs")
        self.NombreJoueursText = QLineEdit()

        AgeMini = QLabel("Age Minimum:")
        self.AgeMiniText = QLineEdit()

        self.SubmitButton = QPushButton(u"Créer")

        # CreerJeu à mapper


        Layout = QVBoxLayout()
        Layout.addWidget(NomJeu)
        Layout.addWidget(self.NomJeuText)
        Layout.addWidget(Editeur)
        Layout.addWidget(self.EditeurText)
        Layout.addWidget(Annee)
        Layout.addWidget(self.AnneeText)
        Layout.addWidget(AgeMini)
        Layout.addWidget(self.AgeMiniText)
        Layout.addWidget(NombreJoueurs)
        Layout.addWidget(self.NombreJoueursText)
        Layout.addWidget(self.SubmitButton)
        self.AddJeuP.setLayout(Layout)
        self.SubmitButton.clicked.connect(self.creerJeu)
        self.AddJeuP.exec_()



    def creerJeu(self):
        Nom_jeu=str(self.NomJeuText.text())
        Editeur=str(self.EditeurText.text())
        Annee=str(self.AnneeText.text())
        NombreJoueurs=str(self.NombreJoueursText.text())
        AgeMini=str(self.AgeMiniText.text())
        if Nom_jeu != "":
            try:
                EnsJeux.Jeu(Nom_jeu=Nom_jeu,Editeur=Editeur,Annee=Annee,AgeMini=AgeMini,NombreJoueurs=NombreJoueurs).save()
                QMessageBox.information(self, u"Voilà !",
                u"Le jeu a été ajouté avec succès !",
                QMessageBox.Ok, QMessageBox.NoButton,
                QMessageBox.NoButton)
                self.AddJeuP.close()
                self.parent().parent().jeux()
            except:
                raise
                QMessageBox.critical(self, "ERREUR !",
                u"Erreur lors de l'ajout du jeu. Jeu déjà existant ?",
                QMessageBox.Ok, QMessageBox.NoButton,
                QMessageBox.NoButton)
        else:
            QMessageBox.critical(self, "ERREUR !",
            "Erreur lors de l'ajout du jeu. Rentrez un nom valide !",
            QMessageBox.Ok, QMessageBox.NoButton,
            QMessageBox.NoButton)
            self.AddJeuP.close()
        # AJOUTER Categorie


    def selectedgame(self):
        row = self.Table.currentItem().row()
        print "row=",row
        col = self.Table.currentItem().column()
        print "col=",col
        item = self.Table.item(row,0).text()
        print "item=",item

        # Affichage popup selection #
        #selection = QMessageBox.information(self,
        #self.trUtf8("Selection"),
        #self.trUtf8("Vous avez séléctionné le jeu: \nID: "+item+" \nNom du jeu: "+self.Table.item(row,1).text()))
        Jeu = JeuView(item=item,session=self.parent().session)
        # JEU VIEW ? OU POPUP.
        self.close()
        self.parent().setCentralWidget(Jeu)

        #self.parent().setCentralWidget(JeuV)
        # Changer vue vers 1 Seul jeu et sa fiche !

    def rechercheJeu(self):
        self.searchmydata(str(self.RechercheText.text()))
