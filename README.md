# Piscine

A FAIRE 

Mehdi:
- EnsReservations (+Structure de données)
- Reservation

Jean:
- EnsEmprunts (+Structure de données)
- Emprunt

Rahim:
- EnsExtensions (+Structure de données)

Vincent:
- Extension (+Spécification fonctionnelle)

==>Extension
- On peut reserver une extension sans avoir reservé le jeu de base
- On peut reserver une extension et un jeu (SEULEMENT si l'extension lui appartient)
- On peut reserver une seule extension
- Recuperer le nombre d'extension d'un jeu
- Recuperer le nombre d'extensions disponibles
- Recuperer une Extension
- Ajouter une extension
- Supprimer une extension
- Modifier une extension





<h1>Projet Piscine IG3</h1>
<h2>Gestion d'une ludothèque</h2>

-----------------------------------------------------------------------
#Class Connexion

Structure de données:
- username: string
- password: string

Spécification fonctionnelle:
<br><b>est_valide</b>: Connexion  -> Bool
<br><b>creer_session</b>: Connexion -> Session
<br> (1) creer_session <=> est_valide(Connexion)


-----------------------------------------------------------------------
#Class Session

Structure de données:
- User: Utilisateur
- admin: Bool

Spécification fonctionnelle:
<br><b>est_admin</b>: Session  -> Bool
<br><b>set_admin</b>: Session x Bool -> Session
<br><b>get_id</b>: Session -> Int


-----------------------------------------------------------------------
#Class Utilisateur

Structure de données:
- user_id: Int
- username: STRING
- password: STRING
- abonnementValide: Bool
- empruntEnCours: Bool
- reservationEnCours: Bool
- nbRetard: Int

Spécification fonctionnelle:
<br><b>get_user_id</b>: Utilisateur  -> String
<br><b>get_username</b>: Utilisateur  -> String
<br><b>get_password</b>: Utilisateur  -> String
<br><b>get_abonnementValide</b>: Utilisateur  -> Bool
<br><b>get_empruntEnCours</b>: Utilisateur  -> Bool
<br><b>get_reservationEnCours</b>: Utilisateur  -> Bool
<br><b>get_nbRetard</b>: Utilisateur  -> Int
<br>
<br><b>set_username</b>: Utilisateur x String -> Utilisateur
<br><b>set_password</b>: Utilisateur x String -> Utilisateur
<br><b>set_abonnementValide</b>: Utilisateur x Bool -> Utilisateur
<br><b>set_empruntEnCours</b>: Utilisateur x Bool -> Utilisateur
<br><b>set_reservationEnCours</b>: Utilisateur x Bool -> Utilisateur
<br><b>set_nbRetard</b>: Utilisateur x Int -> Utilisateur
<br>
<br><b>est_admin</b>: Utilisateur -> Bool
<br><b>make_admin</b>: Utilisateur -> 
<br><b>delete_user</b>: Utilisateur -> 
<br><b>save</b>: Utilisateur -> 

-----------------------------------------------------------------------
#Class Jeu

Structure de données:
- Jeu_id: Int
- Nom_jeu: STRING
- Annee: STRING
- Editeur: STRING
- AgeMini: STRING
- NombreJoueur: STRING
- Description: TEXT

Spécification fonctionnelle:
<br><b>get_Nom_jeu</b>: Jeu  -> String
<br><b>get_AgeMini</b>: Jeu  -> String
<br><b>get_Description</b>: Jeu  -> String
<br><b>get_Jeu_id</b>: Jeu  -> Int
<br><b>get_nombre_exemplaires</b>: Jeu  -> Int
<br><b>get_nombre_exemplaires_dispo</b>: Jeu  -> Int
<br><b>get_NombreJoueurs</b>: Jeu  -> String
<br><b>get_Editeur</b>: Jeu  -> String
<br><b>get_Annee</b>: Jeu  -> String
<br>
<br><b>set_Nom_jeu</b>: Jeu x String -> Jeu
<br><b>set_AgeMini</b>: Jeu x String -> Jeu
<br><b>set_Description</b>: Jeu x Text -> Jeu
<br><b>set_NombreJoueurs</b>: Jeu x String -> Jeu
<br><b>set_Editeur</b>: Jeu x String -> Jeu
<br><b>set_Annee</b>: Jeu x String -> Jeu
<br>
<br><b>save</b>: Jeu -> 

-----------------------------------------------------------------------
#Class Exemplaire

Structure de données:
- Exemplaire_id: Int
- Jeu_id: Int
- Est_disponible: Bool

Spécification fonctionnelle:

<br><b>get_Jeu_id</b>: Exemplaire  -> Int
<br><b>get_Exemplaire_id</b>: Exemplaire  -> Int
<br><b>get_Est_disponible</b>: Exemplaire  -> Bool

<br>
<br><b>set_Jeu_id</b>: Exemplaire x Int -> Exemplaire
<br><b>set_Est_disponible</b>: Exemplaire x Bool -> Exemplaire

<br>
<br><b>save</b>: Exemplaire -> 

-----------------------------------------------------------------------
#Class Reservation

Structure de données:
- Reservation_id = int
- user_id = int
- Jeu_id = int
- Extension_id = int
- Exemplaire_id = int
- date_Reservation = date
- Terminer = bool

Spécification fonctionnelle:
 
<br><b>get_Reservation_id</b>: Reservation  -> Int
<br><b>get_user_id</b>: Utilisateur -> Int
<br><b>get_Jeu_id</b>: Jeu  -> Int
<br><b>get_Extension_id</b>: Extension -> Int
<br><b>get_Exemplaire_id</b>: Exemplaire  -> Bool
<br><b>get_date_Reservation</b>: Reservation-> date
<br><b>get_Terminer</b>: Reservation -> Bool

<br><b>set_Reservation_id</b>: Reservation x int-> Reservation
<br><b>set_user_id</b>: Utilisateur x int -> Utilisateur
<br><b>set_Jeu_id</b>: Jeu x int  -> Jeu
<br><b>set_Extension_id</b>: Extension x int -> Extension
<br><b>set_Exemplaire_id</b>: Exemplaire x int  -> Exemplaire
<br><b>set_date_Reservation</b>: Reservation x date -> Reservation
<br><b>set_Terminer</b>: Reservation x Bool -> Reservation

------------------------------------------------------------------------
<h3> Modules </h3>

<h4> EnsUtilisateurs </h4>

Fonctions: 
- <b>createTable()</b>: Crée la table EnsUtilisateurs
- <b>destroyTable()</b>: Detruit la table EnsUtilisateurs
- <b>has_username(username)</b>: Renvoie True si un utilisateur est enregistré au même nom
- <b>is_password(password,User)</b>: Renvoie True si c'est le mot de passe de User
- <b>get_nombre_utilisateurs()</b>: Renvoie le nombre d'utilisateurs
- <b>get_user(user_id=None,username=None)</b>: Renvoie un type Utilisateur à partir de l'id et/ou de l'username
- <b>delete_user(User)</b>: Supprime un utilisateur de la base de données <br>
 (1) Si un utilisateur est admin, le supprime aussi de EnsAdmins
- <b>user_to_table(User)</b>: Renvoie une liste avec les attributs d'un type Utilisateur
- <b>insert(User)</b>: Insert un type Utilisateur dans la base de données
- <b>printAll()</b>: Renvoie un tableau avec tous les utilisateurs

<h4> EnsAdmins </h4>

Fonctions: 
- <b>createTable()</b>: Crée la table EnsAdmins
- <b>destroyTable()</b>: Detruit la table EnsAdmins
- <b>est_admin(User)</b>: Renvoie True si l'Utilisateur est admin
- <b>delete_admin(User)</b>: Supprime un statut admin de la base de données <br>
(1) Ne supprime pas l'utilisateur associé
- <b>insert(User)</b>: Insert un type Admin dans la base de données
- <b>printAll()</b>: Renvoie un tableau avec tous les admins

<h4> EnsJeux </h4>

Fonctions: 
- <b>createTable()</b>: Crée la table EnsJeux
- <b>destroyTable()</b>: Detruit la table EnsJeux
- <b>jeu_to_table(Jeu)</b>: Renvoie les attributs d'un Jeu sous forme de liste
- <b>get_Jeu(Jeu_id=None,Nom_jeu=None)</b>: Renvoie un jeu associé au Jeu_id et/ou au Nom_jeu
- <b>delete_jeu(Jeu)</b>: Supprime un type Jeu de la base de données <br>
(1) Supprime les exemplaires associés
(2) Vérifie si un exemplaire est emprunté
- <b>insert(Jeu)</b>: Insert un type Jeu dans la base de données
- <b>rechercher(Nom_jeu)</b>: Recherche type Jeu dans la base de données
- <b>update(Jeu)</b>: Update un type Jeu dans la base de données
- <b>printAll()</b>: Renvoie un tableau avec tous les Jeux

<h4> EnsExemplaires </h4>

Fonctions: 
- <b>createTable()</b>: Crée la table EnsExemplaires
- <b>destroyTable()</b>: Detruit la table EnsExemplaires
- <b>exemplaire_to_table(Jeu)</b>: Renvoie les attributs d'un Exemplaire sous forme de liste
- <b>get_nombre_exemplaires(Jeu,disponible)</b>: Renvoie le nombre d'exemplaire<br>
 <i>Tous: disponible = 2, Disponibles: disponible=1, Indisponibles: disponible=0</i>
- <i><b>get_Exemplaire_dispo(Jeu)</b>: Renvoie un exemplaire disponible associé à un Type Jeu</i>
- <b>delete_Exemplaire(Exemplaire)</b>: Supprime un type Exemplaire de la base de données <br>
- <b>insert(Exemplaire)</b>: Insert un type Exemplaire dans la base de données
- <b>printAll()</b>: Renvoie un tableau avec tous les Exemplaires


<h4> EnsReservation </h4>
Fonctions: 
- <b>createTable()</b>: Crée la table EnsReservation
- <b>destroyTable()</b>: Detruit la table EnsReservation
- <b>Reservation_EnCours(User)<b> : Prend en paramètre un utilisateur et renvoie si il a une reservation en cours.
- <b>get_Reservation(User)<b> : Renvoie une reservation associé à un Type Utilisateur
- <b>Ajouter_Reservation(Reservation)<b> : Créer une reservation pour un utilisateur
- <b>supprimer_Reservation(Reservation)<b> : Supprime une réservation pour un utilisateur
- <b>Nombre_De_Reservation()<b> : renvoie le nombre de Reservation
- <b>rechercher_Reservation_User(User)<b> Trouver la reservation en cours de l'utilisateur entré en paramètre
- <b>Reservation_to_table(Reservation)<b> Renvoie une liste avec les attributs d'un type Reservation

