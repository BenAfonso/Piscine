# -*- coding: utf-8 -*-
# Classe d'interface de connexion
from Tkinter import *
class ConnexionFrame(Frame):
    def __init__(self, main_frame):
        Frame.__init__(self, main_frame)
        self.pack(fill=BOTH) #fill=BOTH => fusionne la fenetre tk et ce frame.
        LARGE_FONT=("Verdana",12)
        #Label principal de la fenetre de connexion
        connexionFrame_label_title=Label(self,text="LudoTech'",font=LARGE_FONT)
        connexionFrame_label_title.pack()

        #Label du champ Pseudo
        connexionFrame_label_pseudo=Label(self,text="Pseudo")
        connexionFrame_label_pseudo.pack()
        #Champ de saisie Pseudo
        var_pseudo=StringVar()
        pseudo_field=Entry(self,textvariable=var_pseudo, width=30)
        pseudo_field.pack()

        #Label du champ mot de passe
        connexionFrame_label_password=Label(self,text="Mot de passe")
        connexionFrame_label_password.pack()
        #Champ de saisie Mot de passe
        var_password=StringVar()
        password_field=Entry(self,textvariable=var_password, width=30, show="*")
        password_field.pack()

        #Bouton de connexion faisant appel à une méthode connexion() ou creation de session, ici quit pour l'instant
        connexion_button=Button(self,text="Se connecter",command=main_frame.destroy)
        connexion_button.pack()

        #Bouton quitter
        quit_button=Button(self, text="Quitter", command=main_frame.destroy)
        quit_button.pack()
