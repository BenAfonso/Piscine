# -*- coding: utf-8 -*-
import os
#from Utilisateur import Utilisateur
import EnsUtilisateurs
#from Jeu import Jeu
import EnsJeux
#from Exemplaire import Exemplaire
import EnsExemplaires
from Session import Session
from Connexion import Connexion
import EnsEmprunt
import EnsAdmins
import sys
import getpass #Masquer saisie mot de passe
global user
global ActiveSession

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
        # Rajoute try
        con = Connexion(login,password)
        
        if con.est_valide():
            newSession(login)
            menu()
        else:
            cls()
            print "Erreur:: Merci de vous reconnecter"
            raw_input("Press Enter to try again")
            connexion()
   

def newSession(login):
    global user
    global ActiveSession
    user = EnsUtilisateurs.get_user(username=login)
    ActiveSession = Session(user)

def connecte():
    cls()
    print("================================================================================")
    print("===                         GESTION DE LA LUDOTHEQUE                         ===")
    print("================================================================================")
    if ActiveSession.est_admin():
        statut= "Administrateur\n\n"
    elif ActiveSession.get_session_User().get_abonnementValide():
        statut= "Adherent\n\n"
    else:
        statut= "Non Adherent\n\n"
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
    rows=EnsUtilisateurs.printAll()
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
    
    selectedUser = EnsUtilisateurs.get_user(user_id=user_id)
    connecte()
    print "===== Utilisateur selectionné ====="
    print "ID: "+str(selectedUser.get_user_id())
    print "Nom d'utilisateur: "+selectedUser.get_username()
    if EnsAdmins.est_admin(selectedUser):
        status="Admin"
    else:
        status="Adhérent"
    print "Statut: "+status

    if selectedUser.get_abonnementValide():
        print "[V] Abonnement valide"
    else:
        print "[X] Abonnement non valide"
    if EnsEmprunt.a_un_emprunt_en_cours(selectedUser):
        print "\nEmprunt en cours: \n"+EnsEmprunt.get_emprunt_en_cours(selectedUser).display()
    print "==================================="
    print "\n"
    print "1. Emprunt rendu"
    if not(selectedUser.get_abonnementValide()):
        print "2. Valider abonnement"
    print "8. Modifier"
    print "9. Supprimer"
    if (status!="Admin"):
        print "10. Promouvoir administrateur"
    print "0. Retour"
    choix = int(raw_input("Choix: "))
    if (choix == 1 and EnsEmprunt.a_un_emprunt_en_cours(selectedUser)):
        rendreEmprunt(selectedUser)
        selectionnerUtilisateur(selectedUser.get_user_id())
    if (choix==2 and not(selectedUser.get_abonnementValide())):
        selectedUser.set_abonnementValide(True)
        selectionnerUtilisateur(selectedUser.get_user_id())
    if (choix==8):
        print "En construction..."
    elif (choix==9):
        selectedUser.delete_user()
        raw_input("Utilisateur supprimé. Appuyez sur Entrer pour continuer.")
        listeUtilisateurs()
    elif (choix==10 and status != "admin"):
        selectedUser.make_admin()
        selectionnerUtilisateur(selectedUser.get_user_id())
    elif (choix==0):
        listeUtilisateurs()
    else:
        selectionnerUtilisateur(selectedUser.get_user_id())
        
def ajouterUtilisateur():
    connecte()
    # Verifier s'il n'existe pas déjà ???? Dans EnsUtilisiteurs sinon raise error
    print ".::# AJOUT D'UN UTILISATEUR #::.\n"
    username=str(raw_input("Nom de l'utilisateur: "))
    password=str(raw_input("Mot de passe: "))
    newUser=EnsUtilisateurs.Utilisateur(username=username,password=password)
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
    rows=EnsJeux.printAll()
    print("ID |      Nom du jeu           | Année |    Editeur    |")
    print("-----------------------------")
    for row in rows:
        print('{0} | {1} | {2} | {3} '.format(row[0], row[1], row[2], row[3]))
    print "============================"
    print "\n1. Selectionner un jeu"
    print "2. Rechercher un jeu"
    if ActiveSession.est_admin():
        print "3. Ajouter un jeu"
    print "0. Retour au menu"
    choixUtilisateur=int(raw_input("Choix: "))
    if choixUtilisateur==1:
        game_id=int(raw_input("\nID du jeu: "))
        selectionnerJeu(game_id)
    elif choixUtilisateur==2:
        key="%%%%%%%%%%%%%%%%%%%%%%%%"+str(raw_input("Rechercher un jeu (par nom): "))+"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
        FoundJeu = EnsJeux.rechercher(key)
        print("========================")
        print("Resultat: "+str(FoundJeu.get_Jeu_id())+" :: "+FoundJeu.get_Nom_jeu())
        
        raw_input("\nPress Enter to go back")
        cls()
        listeJeux()

        
    elif (choixUtilisateur==3 and ActiveSession.est_admin()):
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
    Annee=str(raw_input("Annee: "))
    Editeur=str(raw_input("Editeur: "))
    AgeMini=str(raw_input("Age Minimum: "))
    NombreJoueurs=str(raw_input("Nombre de joueurs: "))
    Description=str(raw_input("Description: "))

    newGame=EnsJeux.Jeu(Nom_jeu=Nom_jeu,Annee=Annee,Editeur=Editeur,AgeMini=AgeMini,NombreJoueurs=NombreJoueurs,Description=Description)
    print("==> AJOUT DE:")
    print("Nom: "+Nom_jeu)
    print("Annee: "+Annee)
    print("Editeur: "+Editeur)
    print("Age Minimum: "+AgeMini)
    print("Nombre de joueurs: "+NombreJoueurs)
    print("Description: "+Description)

    valider=raw_input("Appuyez sur Entrer pour valider (0 puis Entrer pour annuler)")
    if valider=="":
        newGame.save()
        cls()
        listeJeux()
    else:
        listeJeux()

def selectionnerJeu(game_id):
    
    selectedGame = EnsJeux.get_Jeu(Jeu_id=game_id)
    connecte()
    print "===== JEU ====="
    print "ID: "+str(selectedGame.get_Jeu_id())
    print "Nom du jeu: "+str(selectedGame.get_Nom_jeu())
    print "Annee: "+str(selectedGame.get_Annee())
    print "Editeur: "+str(selectedGame.get_Editeur())
    print "Age Minimum: "+str(selectedGame.get_AgeMini())
    print "Nombre de joueurs: "+str(selectedGame.get_NombreJoueurs())
    print "Description: "+str(selectedGame.get_Description())
    print "Nombre d'exemplaires: "+str(selectedGame.get_nombre_exemplaires())
    print "Nombre d'exemplaires disponibles: "+str(selectedGame.get_nombre_exemplaires_dispo())
    print "==============="
    print "\n"
    if (ActiveSession.get_session_User().peut_emprunter()):
        print "1. Emprunter"
    else:
        print "1. Emprunter (Non disponible)"
    print "2. Reserver"
    if ActiveSession.est_admin():
        print "3. Modifier"
        print "4. Supprimer"
        print "5. Ajouter un exemplaire"
    print "0. Retour"
    choix = int(raw_input("Choix: "))

    # L'utilisateur n'a pas d'emprunt en cours 
    if (choix==1 and ActiveSession.get_session_User().peut_emprunter()):
        d=ActiveSession.get_session_User()
        print d.get_username()
        try:
            D=EnsEmprunt.Emprunt(User=d,Jeu=selectedGame)
            raw_input("Le jeu a bien été emprunté. A rendre pour le "+str(D.calcul_date_echeance()))
        except:
            raw_input("Oops, une erreur est survenue.")
        finally:
            selectionnerJeu(selectedGame.get_Jeu_id())

    # L'Utilisateur a déjà un emprunt en cours 
    elif(choix==1 and EnsEmprunt.a_un_emprunt_en_cours(ActiveSession.get_session_User())):
        print "[ERREUR] Vous ne pouvez pas emprunter. Vous avez déjà un emprunt en cours."
        raw_input("Continuer.")
        selectionnerJeu(selectedGame.get_Jeu_id())
    # L'Utilisateur n'est pas adhérent
    elif(choix==1 and not(ActiveSession.get_session_User().get_abonnementValide())):
        print "[ERREUR] Vous ne pouvez pas emprunter. Votre abonnement n'est pas valide."
        raw_input("Continuer.")
        selectionnerJeu(selectedGame.get_Jeu_id())

    if (choix==3 and ActiveSession.est_admin()):
        modifierJeu(selectedGame)
    if (choix==4 and ActiveSession.est_admin()):
        supprimerJeu(selectedGame)
    if (choix==5 and ActiveSession.est_admin()):
        ajouterExemplaire(selectedGame)
    if (choix == 6):
        rendreEmprunt(selectedGame)

    if choix==0:
        listeJeux()
    else:
        listeJeux()


def rendreEmprunt(selectedUser):
    EnsEmprunt.get_emprunt_en_cours(selectedUser).rendre_Emprunt()
 

def modifierJeu(selectedGame):
    connecte()
    newNom=raw_input("Nom du jeu ("+str(selectedGame.get_Nom_jeu())+"): ")
    if newNom != "":
        selectedGame.set_Nom_jeu(newNom)

    newAnnee=raw_input("Année ("+str(selectedGame.get_Annee())+"): ")
    if newAnnee != "":
        selectedGame.set_Annee(newAnnee)

    newEditeur=raw_input("Editeur ("+str(selectedGame.get_Editeur())+"): ")
    if newEditeur != "":
        selectedGame.set_Editeur(newEditeur)

    newAgeMin=raw_input("Age Minimum ("+str(selectedGame.get_AgeMini())+"): ")
    if newAgeMin != "":
        selectedGame.set_AgeMini(newAgeMin)

    newNbJoueurs=raw_input("Nombre de joueurs ("+str(selectedGame.get_NombreJoueurs())+"): ")
    if newNbJoueurs != "":
        selectedGame.set_NombreJoueurs(newNbJoueurs)

    newDescription=raw_input("Description ("+str(selectedGame.get_Description())+"): ")
    if newDescription != "":
        selectedGame.set_Description(newDescription)
        
    selectionnerJeu(selectedGame.get_Jeu_id())

def supprimerJeu(selectedGame):
    EnsJeux.delete_Jeu(selectedGame)
    listeJeux()

def ajouterExemplaire(selectedGame):
    NewExemplaire = EnsExemplaires.Exemplaire(Jeu=selectedGame)
    raw_input("Etes vous sur de vouloir ajouter un nouvel exemplaire pour "+selectedGame.get_Nom_jeu())
    NewExemplaire.save()
    selectionnerJeu(selectedGame.get_Jeu_id())
