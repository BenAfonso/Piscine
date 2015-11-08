# Piscine

A FAIRE =

MEHDI EnsReservations (structure de données)
MEHDI Reservation
JEAN EnsEmprunts (structure de données)
JEAN Emprunt
RAHIM EnsExtensions (sstructure de données)
VINCENT Extension (spé fonctionnelles)
- On peut reserver une extension sans avoir reservé le jeu de base
- On peut reserver une extension et un jeu (SEULEMENT si l'extension lui appartient)
- On peut reserver une seule extension
- Recuperer le nombre d'extension d'un jeu
- Recuperer le nombre d'extensions disponibles
- Recuperer une Extension
- Ajouter une extension
- Supprimer une extension
- Modifier une extension





Projet Piscine IG3
Gestion d'une ludothèque

-----------------------------------------------------------------------
Class Connexion

# username : string
# password : string
est_valide() => Return true if password/username matches
-----------------------------------------------------------------------
Class EnsUtilisateurs

createTable()
destroyTable()
has_username(username) => Return user_id for username or FALSE
is_password(password,user_id) => Return true if password is user_id's
insert(username,password) => Insert into database
# Préconditions : username dont already exists
printAll() => Print all users
-----------------------------------------------------------------------
Class Utilisateur

#username : String
#password : String
#user_id : Int

get_user() => Return self
get_username() => Return self's username
get_password() => Return self's password
set_username(username) => Change self's username
set_password(password) => Change self's password
save() => Save into Database
-----------------------------------------------------------------------
Class Session

session GLOBAL
#user_id : Int
#admin : Boolean
-----------------------------------------------------------------------
Class Jeu
