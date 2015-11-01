from EnsAdmins import EnsAdmins
class Session:
	def __init__(self,user_id,admin=0):
		self.user_id = user_id
		self.admin = admin

	def est_admin(self):
		AdminList=EnsAdmins()
		return AdminList.est_admin(self.user_id)

	def set_admin(self,admin):
		self.admin = admin

	def get_id(self):
		return self.user_id

	def __del__(self):
		self.user_id = 0
		self.admin = 0

	


