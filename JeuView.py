# -*- coding: utf-8 -*-
import os
from Utilisateur import Utilisateur
from EnsUtilisateurs import EnsUtilisateurs
from Jeu import Jeu
from EnsJeux import EnsJeux
from Exemplaire import Exemplaire
from EnsExemplaires import EnsExemplaires
from Session import Session
from Connexion import Connexion
from EnsAdmins import EnsAdmins
import sys
global user
global ActiveSession
UserList = EnsUtilisateurs()
GameList = EnsJeux()

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def firstmenu():
    cls()
    print("============== GESTION DE LA LUDOTHEQUE ===============\n")
    print("1. Se connecter")
    print("2. Quitter")
    Choix = int(raw_input("Choix: "))
    if Choix==1:
        connexion()
    elif Choix==2:
        exit()
    else:
        firstmenu()

def connexion():
    res=False

    while(res==False):
        cls()
        print("============== GESTION DE LA LUDOTHEQUE ===============")
        print("CONNEXION:")
        login = str(raw_input("Nom d'utilisateur: "))
        password = str(raw_input("Mot de passe: "))
        try:
            con = Connexion(login,password)
            res=con.est_valide()
            if res:
                newSession(login)
                menu()
            else:
                cls()
                print "Nom d'utilisateur et/ou mot de passe incorrect"
                raw_input("Press Enter to try again")
                connexion()
        except: 
            cls()
            print "Nom d'utilisateur et/ou mot de passe incorrect"
            raw_input("Press Enter to try again")
            connexion()

def newSession(login):
    global user
    global ActiveSession
    userid=UserList.has_username(login)
    user = Utilisateur("","",userid)
    ActiveSession = Session(userid)

def connecte():
    cls()
    print("============== GESTION DE LA LUDOTHEQUE ===============")
    print "----- Connecte en tant que "+user.get_username()
    if ActiveSession.est_admin():
        print "-- ADMIN\n\n"
    else:
        print"-- Adherent\n\n"


def menu():
    connecte()
    print "==== MENU ===="
    print "1. Afficher utilisateurs"
    print "2. Afficher liste des jeux"
    print "9. Se deconnecter"
    print "0. Quitter"
    choix = int(raw_input("Choix: "))
    if (choix==1):
        listeUtilisateurs()
    elif (choix==2):
        listeJeux()
    elif (choix==0):
        exit() 
    elif (choix==9):
        logoff()
    else:
        menu()

def logoff():
    global ActiveSession
    del ActiveSession
    firstmenu()

def listeUtilisateurs():
    connecte()
    print "==== LISTE UTILISATEURS ===="
    rows=UserList.printAll()
    for row in rows:
        print('{0} - {1} '.format(row[0], row[1]))
    print "============================"
    print "\n1. Selectionner un utilisateur"
    print "2. Ajouter un utilisateur"
    print "3. Retour au menu"
    choixUtilisateur=int(raw_input("Choix: "))
    if choixUtilisateur==2:
        ajouterUtilisateur()
    if choixUtilisateur == 3:
        menu()


def ajouterUtilisateur():
    connecte()
    print "AJOUT D'UN UTILISATEUR:\n"
    username=str(raw_input("Nom de l'utilisateur à ajouter: "))
    password=str(raw_input("Mot de passe de l'utilisateur à ajouter: "))
    newUser=Utilisateur(username,password)
    print("Vous êtes sur le point de créer l'utilisateur "+username+" avec comme mot de passe "+password)
    valider=raw_input("Appuyez sur Entrer pour valider")
    if valider=="":
        newUser.save()
        cls()
        listeUtilisateurs()

def listeJeux():
    connecte()
    print "==== LISTE DES JEUX ===="
    rows=GameList.printAll()
    print("ID |      Nom du jeu     | Age Mini | Description")
    for row in rows:
        print('{0} | {1}  {2}  {3}'.format(row[0], row[1], row[2], row[3]))
    print "============================"
    print "\n1. Selectionner un jeu"
    print "2. Ajouter un jeu"
    print "3. Retour au menu"
    choixUtilisateur=int(raw_input("Choix: "))
    if choixUtilisateur==1:
        selectionnerJeu()
    elif choixUtilisateur==2:
        ajouterJeu()
    elif choixUtilisateur==3:
        menu()
    else: 
        listeJeux()

def ajouterJeu():
    connecte()
    print "AJOUT D'UN JEU: "
    # Verifier s'il n'existe pas déjà ???? dans EnsJeu sinon raise error
    Nom_jeu=str(raw_input("Nom du jeu: "))
    AgeMini=str(raw_input("Age Minimum: "))
    Description=str(raw_input("Description: "))

    newGame=Jeu(Nom_jeu,AgeMini,Description)
    print("==> AJOUT DE:")
    print("Nom: "+Nom_jeu)
    print("Age Minimum: "+AgeMini)
    print("Description: "+Description)

    valider=raw_input("Appuyez sur Entrer pour valider (0 puis Entrer pour annuler)")
    if valider=="":
        newGame.save()
        cls()
        listeJeux()
    else:
        listeJeux()

def selectionnerJeu():
    game_id=int(raw_input("\nID du jeu: "))
    selectedGame = Jeu(game_id)
    connecte()
    print "===== JEU ====="
    print "ID: "+str(selectedGame.get_Jeu_id())
    print "Nom du jeu: "+selectedGame.get_Nom_jeu()
    print "Age Minimum: "+str(selectedGame.get_AgeMini())
    print "Description: "+selectedGame.get_Description()
    print "==============="
    print "\n"
    print "1. Modifier"
    print "2. Supprimer"
    print "0. Retour"
    choix = int(raw_input("Choix: "))
    if choix==1:
        modifierJeu()
    if choix==2:
        supprimerJeu()
    if choix==0:
        listeJeux()
    else:
        listeJeux()

def modifierJeu():
    global ActiveSession
    print ActiveSession.get_id()
    raw_input("")
    menu()

def supprimerJeu():
    menu()

