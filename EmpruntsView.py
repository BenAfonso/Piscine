#-*-coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import EnsJeux
import EnsEmprunt
import EnsExemplaires
import EnsUtilisateurs

import sys


class EmpruntsView(QWidget):
    def __init__(self, *args):
        QWidget.__init__(self)

        self.Table = QTableWidget()
        # Conteneur Vertical
        VLayout = QVBoxLayout()
        # Element 1 du Conteneur Vertical : Label


        VLayout.addWidget(QLabel("Emprunts"))

        # Layout de recherche
        RechercheLayout = QHBoxLayout()


        # Ajout du layout de recherche au layout principal
        VLayout.addLayout(RechercheLayout)

        # Connexion:

        VLayout.addWidget(self.Table)
        # Conteneur Horizontal pour boutons

        # On affecte le layout vertical au widget
        self.setLayout(VLayout)
        #  On change le widget central !


        self.Table.setSortingEnabled(True)
        self.Table.setMinimumSize(800, 300)
        self.Table.setColumnCount(4)
        self.Table.setRowCount(EnsEmprunt.get_nombre_emprunts())

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
        Emprunts = EnsEmprunt.printAll()
        for Emprunt in Emprunts:
            self.Table.setItem(ligne, 0, QTableWidgetItem(str(EnsUtilisateurs.get_user(Emprunt[1]).get_username())))
            self.Table.setItem(ligne, 1, QTableWidgetItem(str(EnsExemplaires.get_Exemplaire(Emprunt[2]).get_Jeu_Exemplaire().get_Nom_jeu())))
            self.Table.setItem(ligne, 2, QTableWidgetItem(str(Emprunt[3])))
            self.Table.setItem(ligne, 3, QTableWidgetItem(str(Emprunt[4])))

            ligne=ligne+1

    def setheaders(self):
        # On définit l'entête des colonnes
        hedlabels = ('Utilisateur', 'Nom du jeu', 'Date Emprunt', 'Date Echeance')
        # Largeur initiale des colonnes
        self.Table.hedprops = (100, 250, 200, 100)
        # On ajoute les colonnes au tableau
        self.Table.setHorizontalHeaderLabels(hedlabels)
        for i, taille in enumerate(self.Table.hedprops):
            self.Table.horizontalHeader().resizeSection(i, taille)
