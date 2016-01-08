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
        CompteTitre = QLabel("# Compte\n")
        EmpruntTitre = QLabel("\n# Emprunt")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(20)
        CompteTitre.setFont(font)
        EmpruntTitre.setFont(font)

        usernametxt = QLabel("Nom d'utilisateur: ")
        username=QLabel(str(self.selectedUser.get_username()))

        statutTxt = QLabel("Statut: ")
        if self.selectedUser.get_abonnementValide() and self.selectedUser.est_admin():
            statut = QLabel("Administrateur - Adherent")
        elif not(self.selectedUser.get_abonnementValide()) and self.selectedUser.est_admin():
            statut = QLabel("Administrateur - Non adherent")
        elif self.selectedUser.get_abonnementValide():
            statut= QLabel(u"Adhérent")
        else:
            statut=QLabel("Utilisateur")

        retardTxt = QLabel("Retard: ")
        retard = QLabel(str(self.selectedUser.get_nbRetard())+" jours")

        abonnementValideTxt = QLabel("Abonnement: ")
        if (self.selectedUser.get_abonnementValide()):
            abonnementValide = QLabel("Valide")
        else:
            abonnementValide = QLabel("Non Valide")

        empruntEnCoursTxt = QLabel("\nEmprunt en cours:")
        if EnsEmprunt.a_un_emprunt_en_cours(self.selectedUser):
            empruntEnCours=EnsEmprunt.get_emprunt_en_cours(self.selectedUser)
        else:
            empruntEnCours=None


        ModifierMotDePasse = QPushButton("Changer mon mot de passe")


        # Grande Horizontale Milieu
        HBoxCentre = QHBoxLayout()

        # Vertical Gauche
        VBoxTextes = QVBoxLayout()

        # Layout titre Compte
        VBoxTextes.addWidget(CompteTitre)

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
        VBox4=QVBoxLayout()

        HBox3.addLayout(VBox3)
        HBox3.addLayout(VBox4)

        VBoxTextes.addWidget(ModifierMotDePasse)


        #### EMPRUUUUNT ####
        VBoxTextes.addWidget(EmpruntTitre)

        HBox31 = QHBoxLayout()
        VBox3.addLayout(HBox31)
        VBox31 = QVBoxLayout()
        VBox32 = QVBoxLayout()
        HBox31.addLayout(VBox31)
        HBox31.addLayout(VBox32)
        VBox4.addWidget(spacer)

        if empruntEnCours != None:
            #### INFORMATIONS EMPRUNT ####
            NomDuJeuTxt=QLabel("Nom du jeu:")
            NomDuJeu=QLabel(str(empruntEnCours.get_Exemplaire_Emprunt().get_Jeu_Exemplaire().get_Nom_jeu()))
            DateEmpruntTxt=QLabel("Nom d'emprunt:")
            DateEmprunt=QLabel(str(empruntEnCours.get_date_emprunt()))
            DateEcheanceTxt=QLabel(u"Date d'écheance:")
            DateEcheance=QLabel(str(empruntEnCours.get_date_echeance()))
            #### AJOUT EMPRUNT AU LAYOUT ####
            VBox31.addWidget(NomDuJeuTxt)
            VBox32.addWidget(NomDuJeu)
            VBox31.addWidget(DateEmpruntTxt)
            VBox32.addWidget(DateEmprunt)
            VBox31.addWidget(DateEcheanceTxt)
            VBox32.addWidget(DateEcheance)
        else:
            VBox31.addWidget(QLabel("Aucun"))
            VBox32.addWidget(QLabel("     "))






        # Verticale Droite
        VBoxBoutons = QVBoxLayout()

        HBoxCentre.addLayout(VBoxTextes)
        Blank = QVBoxLayout()
        Blank.addWidget(spacer)
        HBoxCentre.addLayout(Blank)
        HBoxCentre.addLayout(VBoxBoutons)




        # Ajout des widgets Boutons

        #VBoxBoutons.addWidget(ModifierMotDePasse)



        Grid.addLayout(HBoxCentre)
        Grid.addLayout(HBox3)
        ModifierMotDePasse.clicked.connect(self.modifierMotDePasse)


        # ESPACEMENT
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        Grid.addWidget(spacer)



        self.setLayout(Grid)

    def refresh(self):
        refresh = ProfileView(session=self.session)
        self.parent().setCentralWidget(refresh)


    def modifierMotDePasse(self):
        self.ModifierMdp = QDialog()

        Titre = QLabel("Modification Mot de passe\n")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(20)
        Titre.setFont(font)

        OldPassword = QLabel("Ancien mot de passe: ")
        self.OldPasswordText = QLineEdit()
        self.OldPasswordText.setEchoMode(QLineEdit.Password)

        Password = QLabel("Nouveau mot de passe: ")
        self.PasswordText = QLineEdit()
        self.PasswordText.setEchoMode(QLineEdit.Password)

        Password2 = QLabel(u"Ré-entrez le nouveau mot de passe: ")
        self.PasswordText2 = QLineEdit()
        self.PasswordText2.setEchoMode(QLineEdit.Password)

        # Test si PasswordText1 = PasswordText2
        self.SubmitButton = QPushButton(u"Changer")


        Layout = QVBoxLayout()
        Layout.addWidget(Titre)
        Layout.addWidget(OldPassword)
        Layout.addWidget(self.OldPasswordText)
        Layout.addWidget(Password)
        Layout.addWidget(self.PasswordText)
        Layout.addWidget(Password2)
        Layout.addWidget(self.PasswordText2)
        Layout.addWidget(self.SubmitButton)
        self.ModifierMdp.setLayout(Layout)
        self.SubmitButton.clicked.connect(self.modifierValider)
        self.ModifierMdp.exec_()

    def modifierValider(self):
        if str(self.OldPasswordText.text()) == str(self.selectedUser.get_password()):
            if (len(str(self.PasswordText.text())) > 3):
                if str(self.PasswordText.text()) == str(self.PasswordText2.text()):
                    self.selectedUser.set_password(str(self.PasswordText.text()))

                    QMessageBox.information(self, u"Voilà !",
                    u"Votre mot de passe a été changé avec succès !",
                    QMessageBox.Ok, QMessageBox.NoButton,
                    QMessageBox.NoButton)
                    self.refresh()
                    self.ModifierMdp.close()
                else:
                    QMessageBox.critical(self, "ERREUR !",
                    "Les deux mots de passe de sont pas identiques !",
                    QMessageBox.Ok, QMessageBox.NoButton,
                    QMessageBox.NoButton)
            else:
                QMessageBox.critical(self, "ERREUR !",
                "Le mot de passe doit contenir au moins 4 caractères",
                QMessageBox.Ok, QMessageBox.NoButton,
                QMessageBox.NoButton)
        else:
            QMessageBox.critical(self, "ERREUR !",
            "Votre mot de passe actuel est incorrect !",
            QMessageBox.Ok, QMessageBox.NoButton,
            QMessageBox.NoButton)

    def criticalError(self):
        QMessageBox.critical(self, "ERREUR !",
        "Oops ! Une erreur est survenue ",
        QMessageBox.Cancel, QMessageBox.NoButton,
        QMessageBox.NoButton)
