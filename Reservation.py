import EnsReservation

class Reservation :

    def __init__(self,Reservation_id = None, user_id = None,Jeu_id = None, Exemplaire_id = None,date_Reservation = None) :
    
        self.Reservation_id = Reservation_id
        self.user_id = user_id
        self.Jeu_id = Jeu_id
        self.Exemplaire_id = Exemplaire_id
        self.date_Reservation = date_Reservation
    
    
  ### GETTERS###
  
    def get_Reservation_id(self):
        return self.Reservation_id
    def get_user_id(self):
        return self.user_id   
    def get_Jeu_id(self):
        return self.Jeu_id
    def get_Exemplaire_id(self):
        return self.Exemplaire_id
    def get_date_Reservation(self):
        return self.date_Reservation
        
    ##### SETTERS #####
    
    def set_user_id(self, user_id):
        self.user_id = user_id
    def set_Jeu_id(self, Jeu_id):
        self.Jeu_id = Jeu_id
    def set_Exemplaire_id(self, Exemplaire_id):
        self.Exemplaire_id = Exemplaire_id
    def set_Reservation_date(self, date_Reservation):
        self.date_Reservation = date_Reservation
        
  ##### FONCTIONS ANNEXES #####
  
      def save(self):
        
        EnsReservation.insert(self)
