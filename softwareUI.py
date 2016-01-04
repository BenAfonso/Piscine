# -*- coding: utf-8 -*-
from Tkinter import *
# MEMO: pour qu'un widget apparaisse il faut qu'il prenne en parametre du constructeur la fenetre principale
# Les widgets: fenetre, label, boutons, champ de saisie,
#creation d'une fenetre de base
root_window = Tk()

#creation d'un label contenant du texte
label_field = Label(root_window, text="Welcome to LudoTech' :-)")
# On affiche le label dans la fenêtre, pack() positionne notre label dans la fenetre
label_field.pack()

#Label pseudo
label_pseudo=Label(root_window, text="Pseudo")
label_pseudo.pack()
#Champ de saisie
var_pseudo = StringVar()
text_line_pseudo = Entry(root_window,textvariable=var_pseudo, width=30)
text_line_pseudo.pack()
#Label mot de passe
label_password=Label(root_window, text="Mot de passe")
label_password.pack()
#Champ de saisie mot de passe
var_password = StringVar()
text_line_password = Entry(root_window,textvariable=var_password, width=30, show="*")
text_line_password.pack()
#Bouton de connexion
button_connexion=Button(root_window, text="Se connecter")
button_connexion.pack()
#Bouton quitter
button_quit=Button(root_window, text="Quitter", command=root_window.destroy)
button_quit.pack()

#Frame test
main_frame = Frame(root_window,width=640, height=480,borderwidth=1)
main_frame.pack(fill=BOTH)
#Label for main_frame
main_frame_label=Label(main_frame, text="Main Frame window")


# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
root_window.mainloop()


# TO DO: Classes d'interface nécessaire à la génération de chaque écran
