#-*-coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import EnsJeux
from JeuView import JeuView
import sys



 
class JeuxView(QTableWidget):
    def __init__(self, *args):
        QTableWidget.__init__(self)


        # On défini le nombre de colonnes


        self.setSortingEnabled(True)
        self.setMinimumSize(800, 300)
        self.setColumnCount(5)
        self.setRowCount(EnsJeux.get_nombre_jeux())
        self.setheaders()
        self.setmydata()

        # Selection de lignes activé
        self.setSelectionBehavior(self.SelectRows)
        # Pas de sélection de cellule
        self.setSelectionMode(self.NoSelection)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setFocusPolicy(Qt.NoFocus)
        self.setAlternatingRowColors(True)
        self.verticalHeader().hide()
        # Affichage de la grille désactivé
        self.setShowGrid(False)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.horizontalHeader().setStretchLastSection(True)

        self.cellDoubleClicked.connect(self.selectedgame)
        

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
        Jeux = EnsJeux.rechercher("%%%%%%%%%%%%%%%%"+keyword+"%%%%%%%%%%%%%%%%")
        self.setRowCount(len(Jeux))
        for Jeu in Jeux:
            self.setItem(ligne, 0, QTableWidgetItem(str(Jeu[0])))
            self.setItem(ligne, 1, QTableWidgetItem(Jeu[1]))
            self.setItem(ligne, 2, QTableWidgetItem(Jeu[3]))
            self.setItem(ligne, 3, QTableWidgetItem(str(Jeu[2])))
            self.setItem(ligne, 4, QTableWidgetItem(Jeu[4]))
            ligne=ligne+1

    # Fonction permettant d'initialiser le contenu de l'affichage (remplacer par searchmydata)
    def setmydata(self):
        ligne = 0
        Jeux = EnsJeux.printAll()
        for Jeu in Jeux:
            self.setItem(ligne, 0, QTableWidgetItem(str(Jeu[0])))
            self.setItem(ligne, 1, QTableWidgetItem(Jeu[1]))
            self.setItem(ligne, 2, QTableWidgetItem(Jeu[3]))
            self.setItem(ligne, 3, QTableWidgetItem(str(Jeu[2])))
            self.setItem(ligne, 4, QTableWidgetItem(Jeu[4]))
            ligne=ligne+1

    def setheaders(self):
        # On définit l'entête des colonnes
        hedlabels = ('ID', 'Nom du jeu', 'Editeur', 'Annee', 'Nb Joueurs')
        # Largeur initiale des colonnes
        self.hedprops = (100, 250, 200, 100, 130)
        # On ajoute les colonnes au tableau
        self.setHorizontalHeaderLabels(hedlabels)
        for i, taille in enumerate(self.hedprops):
            self.horizontalHeader().resizeSection(i, taille)

    def AddJeu(self): # Popup pour ajouter un jeu 

        AddJeu = QDialog()
        NomJeu = QLabel("Nom du jeu")
        NomJeuText = QLineEdit()

        Editeur = QLabel("Editeur")
        EditeurText = QLineEdit()

        
        Annee = QLabel(u"Année")
        AnneeText = QLineEdit()

        NombreJoueurs = QLabel("NombreJoueurs")
        NombreJoueursText = QLineEdit()

        SubmitButton = QPushButton(u"Créer")

        # CreerJeu à mapper


        Layout = QVBoxLayout()
        Layout.addWidget(NomJeu)
        Layout.addWidget(NomJeuText)
        Layout.addWidget(Editeur)
        Layout.addWidget(EditeurText)
        Layout.addWidget(Annee)
        Layout.addWidget(AnneeText)
        Layout.addWidget(NombreJoueurs)
        Layout.addWidget(NombreJoueursText)
        Layout.addWidget(SubmitButton)
        AddJeu.setLayout(Layout)
        AddJeu.exec_()
        #AddJeu.SubmitButton.clicked.connect(creerJeu)
        


        
        

    def selectedgame(self):
        row = self.currentItem().row()
        print "row=",row
        col = self.currentItem().column()
        print "col=",col
        item = self.item(row,0).text()
        print "item=",item
        JeuV = JeuView()
        selection = QMessageBox.information(self,  
        self.trUtf8("Selection"), 
        self.trUtf8("Vous avez séléctionné le jeu: \nID: "+item+" \nNom du jeu: "+self.item(row,1).text()))
        #self.parent().setCentralWidget(JeuV)
        # Changer vue vers 1 Seul jeu et sa fiche !






