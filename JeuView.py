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
import getpass #Masquer saisie mot de passe
global user
global ActiveSession
UserList = EnsUtilisateurs()
GameList = EnsJeux()

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def firstmenu():
    cls()
    print("================================================================================")
    print("===                         GESTION DE LA LUDOTHEQUE                         ===")
    print("================================================================================\n")
    print("1. Se connecter")
    print("2. Quitter")
    Choix = int(raw_input("\nChoix: "))
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
        print("================================================================================")
        print("===                         GESTION DE LA LUDOTHEQUE                         ===")
        print("================================================================================\n")
        print("CONNEXION:\n")
        login = str(raw_input("Nom d'utilisateur: "))
        password = getpass.getpass("Mot de passe: ")
        try:
            con = Connexion(login,password)
            res=con.est_valide()
            if res:
                newSession(login)
                menu()
            else:
                cls()
                print "Erreur:: Merci de vous reconnecter"
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
    print("================================================================================")
    print("===                         GESTION DE LA LUDOTHEQUE                         ===")
    print("================================================================================")
    if ActiveSession.est_admin():
        statut= "Administrateur\n\n"
    else:
        statut= "Adherent\n\n"
    print "----- Connecte en tant que "+user.get_username()+" :: "+statut


def menu():
    connecte()
    print "=========== MENU ==========="
    
    print "1. Afficher liste des jeux"
    if ActiveSession.est_admin():
        print "2. Afficher utilisateurs"
    print "9. Se deconnecter"
    print "0. Quitter"
    print "============================"
    choix = int(raw_input("\nChoix: "))
    if (choix==2 and ActiveSession.est_admin()):
        listeUtilisateurs()
    elif (choix==1):
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
    print "====== LISTE UTILISATEURS ======"
    rows=UserList.printAll()
    for row in rows:
        print('{0} - {1} '.format(row[0], row[1]))
    print "================================"
    print "\n1. Selectionner un utilisateur"
    print "2. Ajouter un utilisateur"
    print "0. Retour au menu"
    choixUtilisateur=int(raw_input("Choix: "))
    if choixUtilisateur==1:
        user_id=int(raw_input("\nID de l'utilisateur: ")) # Verifier si existe !!!
        selectionnerUtilisateur(user_id)
    elif choixUtilisateur==2:
        ajouterUtilisateur()
    elif choixUtilisateur == 0:
        menu()
    else:
        listeUtilisateurs()

def selectionnerUtilisateur(user_id):
    EnsA=EnsAdmins()
    selectedUser = Utilisateur("","",user_id)
    connecte()
    print "===== Utilisateur selectionné ====="
    print "ID: "+str(selectedUser.get_user_id())
    print "Nom d'utilisateur: "+selectedUser.get_username()
    if EnsA.est_admin(selectedUser.get_user_id()):
        status="Admin"
    else:
        status="Adhérent"
    print "Statut: "+status
    print "==================================="
    print "\n"
    print "1. Modifier"
    print "2. Supprimer"
    if (status!="Admin"):
        print "3. Promouvoir administrateur"
    print "0. Retour"
    choix = int(raw_input("Choix: "))
    if (choix==1):
        print "En construction..."
    elif (choix==2):
        selectedUser.delete_user()
        raw_input("Utilisateur supprimé. Appuyez sur Entrer pour continuer.")
        listeUtilisateurs()
    elif (choix==3 and status != "admin"):
        selectedUser.make_admin()
        selectionnerUtilisateur(selectedUser.get_user_id())
    elif (choix==0):
        listeUtilisateurs()
    else:
        selectionnerUtilisateur(user_id)
        
def ajouterUtilisateur():
    connecte()
    # Verifier s'il n'existe pas déjà ???? Dans EnsUtilisiteurs sinon raise error
    print ".::# AJOUT D'UN UTILISATEUR #::.\n"
    username=str(raw_input("Nom de l'utilisateur: "))
    password=str(raw_input("Mot de passe: "))
    newUser=Utilisateur(username,password)
    print("==== NOUVEL UTILISATEUR")
    print("Nom d'utilisateur: "+username+"\nMot de passe: "+password)
    valider=raw_input("Appuyez sur Entrer pour valider")
    if valider=="":
        newUser.save()
        cls()
        listeUtilisateurs()

def listeJeux():
    connecte()
    print "====== LISTE DES JEUX ======"
    rows=GameList.printAll()
    print("ID |      Nom du jeu     ")
    print("-----------------------------")
    for row in rows:
        print('{0} | {1}'.format(row[0], row[1]))
    print "============================"
    print "\n1. Selectionner un jeu"
    if ActiveSession.est_admin():
        print "2. Ajouter un jeu"
    print "0. Retour au menu"
    choixUtilisateur=int(raw_input("Choix: "))
    if choixUtilisateur==1:
        game_id=int(raw_input("\nID du jeu: "))
        selectionnerJeu(game_id)
    elif (choixUtilisateur==2 and ActiveSession.est_admin()):
        ajouterJeu()
    elif choixUtilisateur==0:
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

    newGame=Jeu(0,Nom_jeu,AgeMini,Description)
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

def selectionnerJeu(game_id):
    
    selectedGame = Jeu(game_id)
    connecte()
    print "===== JEU ====="
    print "ID: "+str(selectedGame.get_Jeu_id())
    print "Nom du jeu: "+selectedGame.get_Nom_jeu()
    print "Age Minimum: "+str(selectedGame.get_AgeMini())
    print "Description: "+selectedGame.get_Description()
    print "Nombre d'exemplaires: "+str(selectedGame.get_nombre_exemplaires())
    print "Nombre d'exemplaires disponibles: "+str(selectedGame.get_nombre_exemplaires(1))
    print "==============="
    print "\n"
    print "1. Emprunter"
    print "2. Reserver"
    if ActiveSession.est_admin():
        print "3. Modifier"
        print "4. Supprimer"
        print "5. Ajouter un exemplaire"
    print "0. Retour"
    choix = int(raw_input("Choix: "))
    if (choix==1):
        emprunterJeu()
    if (choix==3 and ActiveSession.est_admin()):
        modifierJeu()
    if (choix==4 and ActiveSession.est_admin()):
        supprimerJeu()
    if (choix==5 and ActiveSession.est_admin()):
        ajouterExemplaire(selectedGame)
    if choix==0:
        listeJeux()
    else:
        listeJeux()

def emprunterJeu():
    listeJeux()

def modifierJeu():
    global ActiveSession
    print ActiveSession.get_id()
    raw_input("")
    menu()

def supprimerJeu():
    menu()

def ajouterExemplaire(selectedGame):
    NewExemplaire = Exemplaire(selectedGame.get_Jeu_id())
    valider = raw_input("Etes vous sur de vouloir ajouter un nouvel exemplaire pour "+selectedGame.get_Nom_jeu())
    if valider=="":
        NewExemplaire.save()
        selectionnerJeu(selectedGame.get_Jeu_id())
