import EnsReservation

class Reservation :

    def __init__(self,Reservation_id = None) :
    
        self.Reservation_id = Reservation_id
        
    
    
  ### GETTERS###
  
     def get_Reservation_id(self):
        return self.Reservation_id
        
        
        
        
  
      def save(self):
        
        EnsReservation.insert(self)
