#-*-coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import EnsUtilisateurs
import EnsEmprunt
import sys




class UserView(QWidget):
    def __init__(self,item="",session="",*args):
        # ESPACEMENT
        super(UserView, self).__init__()
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.session = session
        self.Display = QWidget()
        self.Display.setMinimumSize(300, 300)
        self.item = int(item)
        self.selectedUser = EnsUtilisateurs.get_user(self.item)
        QWidget.__init__(self)
        HBox1 = QHBoxLayout()

        Grid = QVBoxLayout()


        # Titre Principale
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(36)
        Username = QLabel(str(self.selectedUser.get_username()))
        Username.setFont(font)

        HBox1.addWidget(spacer)
        if (self.selectedUser.get_abonnementValide()):
            Icon = QLabel("<html><img src='./img/green.png' height='35' width='35'></html>")
        else:
            Icon = QLabel("<html><img src='./img/red.png' height='35' width='35'></html>")
        HBox1.addWidget(Icon)
        HBox1.addWidget(Username)


        HBox1.addWidget(spacer)

        Grid.addLayout(HBox1)
        Grid.addWidget(spacer)


        # TOUS LES CHAMPS
        usernametxt = QLabel("Nom d'utilisateur: ")
        username=QLabel(str(self.selectedUser.get_username()))

        statutTxt = QLabel("Statut: ")
        if self.selectedUser.get_abonnementValide() and self.selectedUser.est_admin():
            statut = QLabel("Administrateur - Adherent")
        elif not(self.selectedUser.get_abonnementValide()) and self.selectedUser.est_admin():
            statut = QLabel("Administrateur - Non adherent")
        elif self.selectedUser.get_abonnementValide():
            statut= QLabel("Adherent")
        else:
            statut=QLabel("Utilisateur")

        retardTxt = QLabel("Retard: ")
        retard = QLabel(str(self.selectedUser.get_nbRetard())+" jours")

        abonnementValideTxt = QLabel("Abonnement: ")
        if (self.selectedUser.get_abonnementValide()):
            abonnementValide = QLabel("Valide")
        else:
            abonnementValide = QLabel("Non Valide")

        empruntEnCoursTxt = QLabel("Emprunt en cours:")
        if EnsEmprunt.a_un_emprunt_en_cours(self.selectedUser):
            empruntEnCours=QLabel("\n"+EnsEmprunt.get_emprunt_en_cours(self.selectedUser).display())
        else:
            empruntEnCours=QLabel("Aucun")




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
        VBox1.addWidget(usernametxt)
        VBox2.addWidget(username)

        VBox1.addWidget(statutTxt)
        VBox2.addWidget(statut)

        VBox1.addWidget(retardTxt)
        VBox2.addWidget(retard)

        VBox1.addWidget(abonnementValideTxt)
        VBox2.addWidget(abonnementValide)

        EmpruntRendu = QPushButton("Emprunt Rendu")

        VBox1.addWidget(empruntEnCoursTxt)
        VBox2.addWidget(QLabel("    "))
        VBox1.addWidget(empruntEnCours)
        VBox2.addWidget(QLabel("    "))
        # Blank
        if EnsEmprunt.a_un_emprunt_en_cours(self.selectedUser):
            VBox1.addWidget(EmpruntRendu)
            VBox2.addWidget(QLabel("     "))



        # Ajouts à faire...

        # Verticale Droite
        VBoxBoutons = QVBoxLayout()

        HBoxCentre.addLayout(VBoxTextes)
        Blank = QVBoxLayout()
        Blank.addWidget(spacer)
        HBoxCentre.addLayout(Blank)
        HBoxCentre.addLayout(VBoxBoutons)




        Modifier = QPushButton("Modifier")
        if self.selectedUser.get_abonnementValide():
            Abonnement = QPushButton("Desactiver Abonnement")
        else:
            Abonnement = QPushButton("Activer Abonnement")

        ReinitRetard = QPushButton("Reinitialiser retard")

        if self.selectedUser.est_admin():
            Promote = QPushButton("Retrograder Utilisateur")
        else:
            Promote = QPushButton("Promouvoir Administrateur")

        Supprimer = QPushButton("Supprimer")


        # Ajout des widgets Boutons

        VBoxBoutons.addWidget(Modifier)
        VBoxBoutons.addWidget(ReinitRetard)
        VBoxBoutons.addWidget(Abonnement)
        VBoxBoutons.addWidget(Supprimer)
        VBoxBoutons.addWidget(Promote)


        Grid.addLayout(HBoxCentre)

        EmpruntRendu.clicked.connect(self.rendreEmprunt)
        ReinitRetard.clicked.connect(self.reinitRetard)
        Abonnement.clicked.connect(self.abonnement)
        Supprimer.clicked.connect(self.supprimer)
        Promote.clicked.connect(self.promote)

        # ESPACEMENT
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        Grid.addWidget(spacer)



        self.setLayout(Grid)

    def rendreEmprunt(self):
        try:
            empruntEnCours=EnsEmprunt.get_emprunt_en_cours(self.selectedUser)
            empruntEnCours.rendre_Emprunt()

            QMessageBox.information(self, "Emprunt rendu:",
            "Emprunte le: "+str(empruntEnCours.get_date_emprunt())+"\nRendu le:  "+str(empruntEnCours.get_date_rendu())+"\nRetard: "+str(empruntEnCours.calcul_retard()),

            QMessageBox.Ok, QMessageBox.NoButton,
            QMessageBox.NoButton)
            self.refresh()
        except:
            raise
            self.criticalError()

    def reinitRetard(self):
            try:
                self.selectedUser.set_nbRetard(0)
                QMessageBox.information(self, "Retard Reinitialise:",
                "Le retard a bien ete reinitialise pour "+str(self.selectedUser.get_username()),
                QMessageBox.Ok, QMessageBox.NoButton,
                QMessageBox.NoButton)
                self.refresh()
            except:
                self.criticalError()

    def abonnement(self):
        try:


            ### Fonction bouton pour changer abonnement

            if self.selectedUser.get_abonnementValide():
                self.selectedUser.set_abonnementValide(False)
                QMessageBox.information(self, "Abonnement:",
                "L'abonnement n'est plus actif pour "+str(self.selectedUser.get_username()),
                QMessageBox.Ok, QMessageBox.NoButton,
                QMessageBox.NoButton)
            else:
                self.selectedUser.set_abonnementValide(True)
                QMessageBox.information(self, "Abonnement:",
                "L'abonnement est desormais actif pour "+str(self.selectedUser.get_username()),
                QMessageBox.Ok, QMessageBox.NoButton,
                QMessageBox.NoButton)
            self.refresh()

        except:

            self.criticalError()

    def refresh(self):
        refresh = UserView(item=self.item,session=self.session)
        self.parent().setCentralWidget(refresh)

    def supprimer(self):
        reply = QMessageBox.question(self, 'Confirmation',
        "Etes vous sur de vouloir supprimer l'utilisateur "+str(self.selectedUser.get_username()), QMessageBox.Yes |
        QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.selectedUser.delete_user()
            QMessageBox.information(self, "Fait !",
            "L'utilisateur a bien ete supprime !",
            QMessageBox.Ok, QMessageBox.NoButton,
            QMessageBox.NoButton)
            self.parent().user()

    def promote(self):
        # L'utilisateur est admin ? Retrograder !
        if self.selectedUser.est_admin():
            reply = QMessageBox.question(self, 'Confirmation',
            "Etes vous sur de vouloir retirer "+str(self.selectedUser.get_username())+" des administrateurs ?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.selectedUser.remove_admin()
                QMessageBox.information(self, "Voila !",
                "L'utilisateur n'est plus dans la liste des administrateurs !",
                QMessageBox.Ok, QMessageBox.NoButton,
                QMessageBox.NoButton)
                self.refresh()
        # L'utilisateur n'est pas admin ? Le Promote !
        else:
            reply = QMessageBox.question(self, 'Confirmation',
            u"Êtes vous sur de vouloir ajouter "+str(self.selectedUser.get_username())+" aux administrateurs de la ludothèque ?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.selectedUser.make_admin()
                QMessageBox.information(self, u"Voilà !",
                u"L'utilisateur est maintenant dans la liste des administrateurs !",
                QMessageBox.Ok, QMessageBox.NoButton,
                QMessageBox.NoButton)
                self.refresh()

    def criticalError(self):
        QMessageBox.critical(self, "ERREUR !",
        "Oops ! Une erreur est survenue ",
        QMessageBox.Cancel, QMessageBox.NoButton,
        QMessageBox.NoButton)
