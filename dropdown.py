from PyQt4 import QtCore, QtGui, uic

class dropdown(QtGui.QDialog):
    def reto(self):
        return self.comboBox.currentText()
        
    def __init__(self,lista):
        QtGui.QDialog.__init__(self)
        uic.loadUi("drop_down.ui",self)
        self.comboBox.addItems(lista)
        self.comboBox.activated.connect(self.reto)