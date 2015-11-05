# Piscine

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
