#-*-coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import EnsJeux
import EnsEmprunt
import sys




class JeuView(QWidget):
    def __init__(self,item="",session="",*args):
        # ESPACEMENT
        super(JeuView, self).__init__()
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.session = session
        self.Display = QWidget()
        self.Display.setMinimumSize(300, 300)
        self.item = int(item)
        self.selectedGame = EnsJeux.get_Jeu(self.item)
        QWidget.__init__(self)
        HBox1 = QHBoxLayout()

        Grid = QVBoxLayout()


        # Titre Principale
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(36)
        selectedGame=EnsJeux.get_Jeu(self.item)
        Titre = QLabel(str(selectedGame.get_Nom_jeu()))
        Titre.setFont(font)

        HBox1.addWidget(spacer)
        if (selectedGame.get_nombre_exemplaires_dispo() > 0):
            Icon = QLabel("<html><img src='./img/green.png' height='35' width='35'></html>")
        else:
            Icon = QLabel("<html><img src='./img/red.png' height='35' width='35'></html>")
        HBox1.addWidget(Icon)
        HBox1.addWidget(Titre)


        HBox1.addWidget(spacer)

        Grid.addLayout(HBox1)
        Grid.addWidget(spacer)


        # TOUS LES CHAMPS
        NomJeuTxt = QLabel("Nom du jeu: ")
        NomJeu=QLabel(str(selectedGame.get_Nom_jeu()))
        EditeurTxt = QLabel("Editeur: ")
        Editeur=QLabel(str(selectedGame.get_Editeur()))
        AnneeTxt=QLabel("Annee: ")
        Annee=QLabel(str(selectedGame.get_Annee()))
        AgeMinTxt=QLabel("Age minimum: ")
        AgeMin=QLabel(str(selectedGame.get_AgeMini()))
        NbJoueursTxt=QLabel("Nombre de joueurs: ")
        NbJoueurs=QLabel(str(selectedGame.get_NombreJoueurs()))
        NbExTxt=QLabel("Nombre d'exemplaires: ")
        NbEx=QLabel(str(selectedGame.get_nombre_exemplaires()))
        NbExDispoTxt=QLabel("Nombre d'exemplaires disponibles: ")
        NbExDispo=QLabel(str(selectedGame.get_nombre_exemplaires_dispo()))


        # Grande Horizontale Milieu
        HBoxCentre = QHBoxLayout()

        # Vertical Gauche
        VBoxTextes = QVBoxLayout()

        # Horizontale Gauches
        HBoxGauche = QHBoxLayout()
        VBoxTextes.addLayout(HBoxGauche)

        VBox1 = QVBoxLayout()
        VBox2 = QVBoxLayout()
        HBoxGauche.addLayout(VBox1)
        HBoxGauche.addLayout(VBox2)

        # Ajout des Widgets de texte
        VBox1.addWidget(NomJeuTxt)
        VBox2.addWidget(NomJeu)
        VBox1.addWidget(EditeurTxt)
        VBox2.addWidget(Editeur)
        VBox1.addWidget(AnneeTxt)
        VBox2.addWidget(Annee)
        VBox1.addWidget(AgeMinTxt)
        VBox2.addWidget(AgeMin)
        VBox1.addWidget(NbJoueursTxt)
        VBox2.addWidget(NbJoueurs)
        VBox1.addWidget(NbExTxt)
        VBox2.addWidget(NbEx)
        VBox1.addWidget(NbExDispoTxt)
        VBox2.addWidget(NbExDispo)

        # Verticale Droite
        VBoxBoutons = QVBoxLayout()

        HBoxCentre.addLayout(VBoxTextes)
        Blank = QVBoxLayout()
        Blank.addWidget(spacer)
        HBoxCentre.addLayout(Blank)
        HBoxCentre.addLayout(VBoxBoutons)



        Extensions = QPushButton("Afficher Extensions")
        Emprunter = QPushButton("Emprunter")
        Reserver = QPushButton("Reserver (Non Disponible)")
        Modifier = QPushButton("Modifier")
        Supprimer = QPushButton("Supprimer")
        ajouterExemplaire = QPushButton("Ajouter Exemplaire")

        # Ajout des widgets Boutons
        VBoxBoutons.addWidget(Extensions)
        VBoxBoutons.addWidget(Emprunter)
        VBoxBoutons.addWidget(Reserver)
        VBoxBoutons.addWidget(Modifier)
        VBoxBoutons.addWidget(Supprimer)
        VBoxBoutons.addWidget(ajouterExemplaire)

        Grid.addLayout(HBoxCentre)


        self.User = self.session.get_session_User()
        Emprunter.clicked.connect(self.emprunter)

        # ESPACEMENT
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        Grid.addWidget(spacer)



        self.setLayout(Grid)

    def emprunter(self):
        if (self.session.get_session_User().peut_emprunter()):
            try:
                D=EnsEmprunt.Emprunt(User=self.User,Jeu=self.selectedGame)
                ###########################
                # AJOUTER LA CONFIRMATION #
                ###########################
                QMessageBox.information(self, "Emprunt !",
                "Le jeu a bien ete emprunte.\n A rendre pour le "+str(D.calcul_Date_Echeance()),
                QMessageBox.Ok, QMessageBox.NoButton,
                QMessageBox.NoButton)

                ## AUTOREFREEEEEESH ##
                new = JeuView(item=self.item,session=self.session)
                self.parent().setCentralWidget(new)

            # Bug catch de l'espace
            except:
                QMessageBox.critical(self, "ERREUR !",
                "Oops ! Une erreur est survenue ",
                QMessageBox.Cancel, QMessageBox.NoButton,
                QMessageBox.NoButton)

        elif (EnsEmprunt.a_un_emprunt_en_cours(self.User)):
            QMessageBox.warning(self, "Impossible d'emprunter",
            "Oops ! il semblerait que vous avez déjà un emprunt en cours.",
            QMessageBox.Cancel, QMessageBox.NoButton,
            QMessageBox.NoButton)
        else:
            QMessageBox.warning(self, "Impossible d'emprunter",
            "Oops ! Il semblerait que votre abonnement n'est pas valide.",
            QMessageBox.Cancel, QMessageBox.NoButton,
            QMessageBox.NoButton)
