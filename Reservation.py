import EnsReservation
from datetime import date

# Rajouter implementation de la date (date automatique lors de la creation) voir Classe Emprunt de Jean
# Faire en sorte qu'on rentre des Instances Utilisateurs et non des user_id (pareil pour exemplaire, ...)
# Jeu inutile parce qu'on a l'exemplaire qui est associé au jeu 

class Reservation :

    def __init__(self,Reservation_id = None, user_id = None, Extension_id = None ,Exemplaire_id = None,date_Reservation = None, Terminer = False) :
    
        self.Reservation_id = Reservation_id
        self.user_id = user_id
        self.Extension_id = Extension_id
        self.Exemplaire_id = Exemplaire_id
        self.Terminer = Terminer
        if date_Reservation == None:
            self.date_Reservation = date.today()
           
        else:
            self.date_Reservation = date_Reservation
            

        
    
  ### GETTERS###
  
    def get_Reservation_id(self):
        return self.Reservation_id
    def get_user_id(self):
        return self.user_id   
    def get_Exemplaire_id(self):
        return self.Exemplaire_id
    def get_date_Reservation(self):
        return self.date_Reservation
    def get_Extension_id(self):
        return self.Extension_id
    def get_Terminer(self):
        return self.Terminer
        
    ##### SETTERS #####
    
    def set_user_id(self, user_id):
        self.user_id = user_id
    def set_Exemplaire_id(self, Exemplaire_id):
        self.Exemplaire_id = Exemplaire_id
    def set_Terminer(self) :
        self.Terminer = True
    def set_Extension_id(self, Extension_id) :
        self.Extension_id = Extension_id

    def set_Reservation_date(self):
        self.date_Reservation = date.today()

        
  ##### FONCTIONS ANNEXES #####
  
      def save(self):
        
        EnsReservation.insert(self)

