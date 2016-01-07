#-*-coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import EnsUtilisateurs
import EnsEmprunt
import sys




class ProfileView(QWidget):
    def __init__(self,session="",*args):
        # ESPACEMENT
        super(ProfileView, self).__init__()
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.session = session
        self.Display = QWidget()
        self.Display.setMinimumSize(300, 300)
        self.selectedUser = self.session.get_session_User()
        QWidget.__init__(self)
        HBox1 = QHBoxLayout()

        Grid = QVBoxLayout()


        # Titre Principale
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(36)
        Username = QLabel("Mon profil")
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

        empruntEnCoursTxt = QLabel("\n-----------------------------\nEmprunt en cours:")
        if EnsEmprunt.a_un_emprunt_en_cours(self.selectedUser):
            empruntEnCours=QLabel("\n"+EnsEmprunt.get_emprunt_en_cours(self.selectedUser).display()+"\n-----------------------------")
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

        HBox3=QHBoxLayout()
        VBox3=QVBoxLayout()
        HBox3.addLayout(VBox3)
        VBox3.addWidget(empruntEnCoursTxt)
        VBox3.addWidget(empruntEnCours)



        # Ajouts à faire...

        # Verticale Droite
        VBoxBoutons = QVBoxLayout()

        HBoxCentre.addLayout(VBoxTextes)
        Blank = QVBoxLayout()
        Blank.addWidget(spacer)
        HBoxCentre.addLayout(Blank)
        HBoxCentre.addLayout(VBoxBoutons)

        ModifierMotDePasse = QPushButton("Changer mon mot de passe")


        # Ajout des widgets Boutons

        VBoxBoutons.addWidget(ModifierMotDePasse)



        Grid.addLayout(HBoxCentre)
        Grid.addLayout(HBox3)
        #ModifierMotDePasse.clicked.connect(self.modifierMotDePasse)


        # ESPACEMENT
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        Grid.addWidget(spacer)



        self.setLayout(Grid)

    def refresh(self):
        refresh = ProfileView(session=self.session)
        self.parent().setCentralWidget(refresh)


    def criticalError(self):
        QMessageBox.critical(self, "ERREUR !",
        "Oops ! Une erreur est survenue ",
        QMessageBox.Cancel, QMessageBox.NoButton,
        QMessageBox.NoButton)
