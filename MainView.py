#! /usr/bin/python
#-*-coding: utf-8 -*-
from PyQt4 import QtGui
from ConnexionView import *
from PyQt4.QtGui import *
from MainWindow import MainWindow
from UsersView import UsersView
import sys


def connexion(args):
    app=QtGui.QApplication(args)
    # Création d'un widget qui servira de fenêtre
    connexionView=ConnexionView() # Affichage de la fenêtre de connexion
    connexionView.show()
    r=app.exec_()
    return connexionView.state


def main(args):
    mainApp=QtGui.QApplication(args)
    fenetre=QWidget()
    label1 = QLabel("Bienvenue")


    MainWindow2=MainWindow()
    MainWindow2.show()
    

    r=mainApp.exec_()
    return r


if __name__=="__main__":
    #main(sys.argv)
    valide=connexion(sys.argv)
    if valide: # Si la connexion est valide on affiche la suite
        main(sys.argv)
