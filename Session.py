import EnsAdmins
from Utilisateur import Utilisateur
class Session:
	def __init__(self,User,admin=0):
		self.User = User
		self.admin = admin

	def est_admin(self):
		
		return EnsAdmins.est_admin(self.User)

	def get_session_User(self):
		return self.User

	def set_admin(self,admin):
		self.admin = admin

	def get_id(self):
		return self.User.get_user_id()

	def __del__(self):
		self.User = None
		self.admin = 0

	


