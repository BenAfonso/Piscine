#-*-coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import EnsJeux
import EnsEmprunt
import EnsExemplaires
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

        if selectedGame.get_nombre_exemplaires_dispo() == 0 and selectedGame.get_nombre_exemplaires() > 0:
            RetourPrevuTxt=QLabel(u"\nRetour prévu: ")
            RetourPrevu=QLabel(str(EnsEmprunt.get_Emprunt_Exemplaire(EnsExemplaires.get_Exemplaire(jeu_id=selectedGame.get_Jeu_id())).get_date_echeance()))
            VBox1.addWidget(RetourPrevuTxt)
            VBox2.addWidget(RetourPrevu)

        # Verticale Droite
        VBoxBoutons = QVBoxLayout()

        HBoxCentre.addLayout(VBoxTextes)
        Blank = QVBoxLayout()
        Blank.addWidget(spacer)
        HBoxCentre.addLayout(Blank)
        HBoxCentre.addLayout(VBoxBoutons)



        Extensions = QPushButton("Afficher Extensions+")

        Emprunter = QPushButton("Emprunter")
        Reserver = QPushButton("Reserver (Non Disponible)")
        Modifier = QPushButton("Modifier")
        Supprimer = QPushButton("Supprimer")
        ajouterExemplaire = QPushButton("Ajouter un exemplaire")
        retirerExemplaire = QPushButton("Retirer un exemplaire")

        # Ajout des widgets Boutons
        VBoxBoutons.addWidget(Extensions)
        VBoxBoutons.addWidget(Emprunter)
        VBoxBoutons.addWidget(Reserver)
        if self.session != None and self.session.est_admin():
            VBoxBoutons.addWidget(Modifier)
            VBoxBoutons.addWidget(Supprimer)
            VBoxBoutons.addWidget(ajouterExemplaire)
            VBoxBoutons.addWidget(retirerExemplaire)

        Grid.addLayout(HBoxCentre)

        if self.session != None:
            self.User = self.session.get_session_User()

        Emprunter.clicked.connect(self.emprunter)
        ajouterExemplaire.clicked.connect(self.ajouterExemplaire)
        Supprimer.clicked.connect(self.supprimer)
        retirerExemplaire.clicked.connect(self.retirerExemplaire)
        Modifier.clicked.connect(self.modifier)

        # ESPACEMENT
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        Grid.addWidget(spacer)



        self.setLayout(Grid)

    def emprunter(self):
        if self.session == None:
            QMessageBox.warning(self, "Impossible d'emprunter",
            u"Oops ! il semblerait que vous ne soyez pas connecté.",
            QMessageBox.Ok, QMessageBox.NoButton,
            QMessageBox.NoButton)
        elif (self.session.get_session_User().peut_emprunter()):
            try:
                D=EnsEmprunt.Emprunt(User=self.User,Jeu=self.selectedGame)
                ###########################
                # AJOUTER LA CONFIRMATION #
                ###########################
                QMessageBox.information(self, "Emprunt !",
                u"Le jeu a bien ete emprunté.\n A rendre pour le "+str(D.calcul_Date_Echeance()),
                QMessageBox.Ok, QMessageBox.NoButton,
                QMessageBox.NoButton)

                ## AUTOREFREEEEEESH ##
                new = JeuView(item=self.item,session=self.session)
                self.parent().setCentralWidget(new)

            # Bug catch de l'espace
            except:
                QMessageBox.critical(self, "ERREUR !",
                "Oops ! Une erreur est survenue ",
                QMessageBox.Ok, QMessageBox.NoButton,
                QMessageBox.NoButton)

        elif (EnsEmprunt.a_un_emprunt_en_cours(self.User)):
            QMessageBox.warning(self, "Impossible d'emprunter",
            u"Oops ! il semblerait que vous ayez déjà un emprunt en cours.",
            QMessageBox.Ok, QMessageBox.NoButton,
            QMessageBox.NoButton)
        else:
            QMessageBox.warning(self, "Impossible d'emprunter",
            "Oops ! Il semblerait que votre abonnement n'est pas valide.",
            QMessageBox.Ok, QMessageBox.NoButton,
            QMessageBox.NoButton)

    def supprimer(self):
        reply = QMessageBox.question(self, 'Confirmation',
        u"Êtes vous sur de vouloir supprimer le jeu "+str(self.selectedGame.get_Nom_jeu()), QMessageBox.Yes |
        QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            EnsJeux.delete_Jeu(self.selectedGame)
            QMessageBox.information(self, "Fait !",
            u"Le jeu a bien ete supprimé !",
            QMessageBox.Ok, QMessageBox.NoButton,
            QMessageBox.NoButton)
            self.parent().jeux()


    def modifier(self):
        self.ModifierJeu = QDialog()

        Titre = QLabel("Modification jeu\n")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(20)
        Titre.setFont(font)


        NomJeu = QLabel("Nom du jeu")
        self.NomJeuText = QLineEdit()
        self.NomJeuText.setText(str(self.selectedGame.get_Nom_jeu()))

        Editeur = QLabel("Editeur")
        self.EditeurText = QLineEdit()
        self.EditeurText.setText(str(self.selectedGame.get_Editeur()))


        Annee = QLabel(u"Année")
        self.AnneeText = QLineEdit()
        self.AnneeText.setText(str(self.selectedGame.get_Annee()))

        NombreJoueurs = QLabel("Nombre de joueurs")
        self.NombreJoueursText = QLineEdit()
        self.NombreJoueursText.setText(str(self.selectedGame.get_NombreJoueurs()))

        AgeMini = QLabel("Age Minimum:")
        self.AgeMiniText = QLineEdit()
        self.AgeMiniText.setText(str(self.selectedGame.get_AgeMini()))

        self.SubmitButton = QPushButton(u"Modifier")

        # CreerJeu à mapper


        Layout = QVBoxLayout()
        Layout.addWidget(Titre)

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
        self.ModifierJeu.setLayout(Layout)
        self.SubmitButton.clicked.connect(self.modifierValider)
        self.ModifierJeu.exec_()
    def modifierValider(self):
        if len(str(self.NomJeuText.text())) > 3:
            self.selectedGame.set_Nom_jeu(str(self.NomJeuText.text()))
            self.selectedGame.set_Editeur(str(self.EditeurText.text()))
            self.selectedGame.set_Annee(str(self.AnneeText.text()))
            self.selectedGame.set_AgeMini(str(self.AgeMiniText.text()))
            QMessageBox.information(self, u"Voilà !",
            u"Le jeu a été modifié avec succès !",
            QMessageBox.Ok, QMessageBox.NoButton,
            QMessageBox.NoButton)
        else:
            QMessageBox.critical(self, "ERREUR !",
            "Erreur lors de la modification du jeu.",
            QMessageBox.Ok, QMessageBox.NoButton,
            QMessageBox.NoButton)



        self.refresh()
        self.ModifierJeu.close()
        #EnsJeux.set_Description(DescriptionText.text())

    def refresh(self):
        refresh = JeuView(item=self.item,session=self.session)
        self.parent().setCentralWidget(refresh)


    def ajouterExemplaire(self):
        NewExemplaire = EnsExemplaires.Exemplaire(Jeu=self.selectedGame)
        reply = QMessageBox.question(self, 'Confirmation',
        u"Êtes vous sur de vouloir ajouter un exemplaire pour le jeu "+str(self.selectedGame.get_Nom_jeu()), QMessageBox.Yes |
        QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            NewExemplaire.save()
            QMessageBox.information(self, "Fait !",
            u"Un exemplaire a bien été ajouté !",
            QMessageBox.Ok, QMessageBox.NoButton,
            QMessageBox.NoButton)
            self.refresh()

    def retirerExemplaire(self):
        # Confirmation
        reply = QMessageBox.question(self, 'Confirmation',
        u"Êtes vous sur de vouloir supprimer un exemplaire pour le jeu "+str(self.selectedGame.get_Nom_jeu()), QMessageBox.Yes |
        QMessageBox.No, QMessageBox.No)
        # Test de la réponse de l'utilisateur
        if reply == QMessageBox.Yes:
            try:
                self.selectedGame.supprimer_Exemplaire()
                QMessageBox.information(self, "Fait !",
                u"Un exemplaire a bien été supprimé !",
                QMessageBox.Ok, QMessageBox.NoButton,
                QMessageBox.NoButton)
                self.refresh()
            except:
                QMessageBox.critical(self, "ERREUR !",
                "Oops, il semblerait qu'il n'y ait pas d'exemplaire disponible ! ",
                QMessageBox.Cancel, QMessageBox.NoButton,
                QMessageBox.NoButton)
