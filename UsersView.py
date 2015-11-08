from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
 
data = {'ID':['1','2','3'], "Nom d'utilisateur":['Darkyler','Blasfm','Zetsubo']}
 
class UsersView(QTableWidget):
    def __init__(self, data=data, *args):
        QTableWidget.__init__(self, *args)
        self.data = data
        self.setmydata()
        #self.resizeColumnsToContents()
        #self.resizeRowsToContents()
        
    def setmydata(self):
 
        horHeaders = []
        for n, key in enumerate(sorted(self.data.keys())):
            horHeaders.append(key)
            for m, item in enumerate(self.data[key]):
                newitem = QTableWidgetItem(item)
                #newitem.setFlags(Qt.ItemIsEnabled) # Bloque les cells
                self.setEditTriggers(QAbstractItemView.NoEditTriggers) # Cells selectionnables seulement
                #newitem.lineEdit.setEchoMode(QLineEdit.Password)
                self.setItem(m, n, newitem)
        self.setHorizontalHeaderLabels(horHeaders)