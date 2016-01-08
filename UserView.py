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

        empruntEnCoursTxt = QLabel("\nEmprunt en cours:")
        if EnsEmprunt.a_un_emprunt_en_cours(self.selectedUser):
            empruntEnCours=EnsEmprunt.get_emprunt_en_cours(self.selectedUser)
        else:
            empruntEnCours=None




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

        EmpruntRendu = QPushButton("Emprunt Rendu")

        HBox3=QHBoxLayout()

        # En dessous gauche et droite
        VBox3=QVBoxLayout()
        VBox4=QVBoxLayout()

        HBox3.addLayout(VBox3)
        HBox3.addLayout(VBox4)

        VBoxTextes.addWidget(EmpruntTitre)
        #VBox3.addWidget(empruntEnCoursTxt)
        #VBox3.addWidget(empruntEnCours)
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

        # Blank
        if EnsEmprunt.a_un_emprunt_en_cours(self.selectedUser):
            VBox3.addWidget(EmpruntRendu)



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
        Grid.addLayout(HBox3)

        EmpruntRendu.clicked.connect(self.rendreEmprunt)
        ReinitRetard.clicked.connect(self.reinitRetard)
        Abonnement.clicked.connect(self.abonnement)
        Supprimer.clicked.connect(self.supprimer)
        Promote.clicked.connect(self.promote)
        Modifier.clicked.connect(self.modifier)

        # ESPACEMENT
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        Grid.addWidget(spacer)



        self.setLayout(Grid)


    def modifier(self):
        self.ModifierUser = QDialog()

        Titre = QLabel("Modification Utilisateur\n")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(20)
        Titre.setFont(font)

        Username = QLabel("Nom d'Utilisateur: ")
        self.UsernameText = QLineEdit()
        self.UsernameText.setText(str(self.selectedUser.get_username()))

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
        self.ModifierUser.setLayout(Layout)
        self.SubmitButton.clicked.connect(self.modifierValider)
        self.ModifierUser.exec_()

    def modifierValider(self):
        if str(self.PasswordText.text()) == str(self.PasswordText2.text()) and len(str(self.PasswordText.text())) > 3:
            self.selectedUser.set_username(str(self.UsernameText.text()))
            self.selectedUser.set_password(str(self.PasswordText.text()))

            QMessageBox.information(self, u"Voilà !",
            u"L'Utilisateur a été modifié avec succès !",
            QMessageBox.Ok, QMessageBox.NoButton,
            QMessageBox.NoButton)
            self.refresh()
            self.ModifierUser.close()
        else:
            QMessageBox.critical(self, "ERREUR !",
            "Erreur lors de la modification de l'utilisateur.",
            QMessageBox.Ok, QMessageBox.NoButton,
            QMessageBox.NoButton)




        #EnsJeux.set_Description(DescriptionText.text())

    def rendreEmprunt(self):
        try:
            empruntEnCours=EnsEmprunt.get_emprunt_en_cours(self.selectedUser)
            empruntEnCours.rendre_Emprunt()

            #QMessageBox.information(self, "Emprunt rendu:",
            #u"Emprunté le: "+str(empruntEnCours.get_date_emprunt())+"\nRendu le:  "+str(empruntEnCours.get_date_rendu())+"\nRetard: "+str(empruntEnCours.calcul_retard()),
            #QMessageBox.Ok, QMessageBox.NoButton,
            #QMessageBox.NoButton)

            QMessageBox.information(self, "Emprunt rendu !",
            u"L'emprunt a bien été rendu !",
            QMessageBox.Ok, QMessageBox.NoButton,
            QMessageBox.NoButton)
            self.refresh()
        except:
            raise
            self.criticalError()

    def reinitRetard(self):
            try:
                self.selectedUser.set_nbRetard(0)
                QMessageBox.information(self, u"Retard Reinitialisé !",
                u"Le retard a bien été réinitialisé pour "+str(self.selectedUser.get_username()),
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
                u"L'abonnement est désormais actif pour "+str(self.selectedUser.get_username()),
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
        u"Êtes vous sur de vouloir supprimer l'utilisateur "+str(self.selectedUser.get_username()), QMessageBox.Yes |
        QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.selectedUser.delete_user()
            QMessageBox.information(self, "Fait !",
            u"L'utilisateur a bien été supprimé !",
            QMessageBox.Ok, QMessageBox.NoButton,
            QMessageBox.NoButton)
            self.parent().user()


    def promote(self):
        # L'utilisateur est admin ? Retrograder !
        if self.selectedUser.est_admin():
            reply = QMessageBox.question(self, 'Confirmation',
            u"Êtes vous sûr de vouloir retirer "+str(self.selectedUser.get_username())+" des administrateurs ?", QMessageBox.Yes |
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
            u"Êtes vous sur de vouloir ajouter "+str(self.selectedUser.get_username())+u" aux administrateurs de la ludothèque ?", QMessageBox.Yes |
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
