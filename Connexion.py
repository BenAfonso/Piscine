# -*- coding: utf-8 -*-
from EnsUtilisateurs import EnsUtilisateurs
from Session import Session

class Connexion:
        def __init__(self,username,password):
                self.username = username
                self.password = password
                self.Userlist = EnsUtilisateurs()


        def est_valide(self):
                return self.Userlist.is_password(self.password,self.Userlist.has_username(self.username))

        def creer_session(self):
                global session
                if self.est_valide():
                        userid = self.Userlist.has_username(self.username) # ID Associe à username fourni
                        session=Session(userid)
                else:
                        print "Oops !"




