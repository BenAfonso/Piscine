import EnsReservation

class Reservation :

    def __init__(self,Reservation_id = None, user_id = None, Exemplaire_id = None,Reservation_date = None) :
    
        self.Reservation_id = Reservation_id
        self.user_id = user_id
        self.Exemplaire_id = Exemplaire_id
        self.Reservation_date = Reservation_date
    
    
  ### GETTERS###
  
    def get_Reservation_id(self):
        return self.Reservation_id
    def get_user_id(self):
        return self.user_id    
    def get_Exemplaire_id(self):
        return self.Exemplaire_id
    def get_Reservation_date(self):
        return self.Reservation_date
        
    ##### SETTERS #####
    
    def set_user_id(self, user_id):
        self.user_id = user_id
    def set_Exemplaire_id(self, Exemplaire_id):
        self.Exemplaire_id = Exemplaire_id
    def set_Reservation_date(self, Reservation_date):
        self.Reservation_date = Reservation_date
           
        
  ##### FONCTIONS ANNEXES #####
  
      def save(self):
        
        EnsReservation.insert(self)
