# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crossFiles.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui,uic

import sys
from file import File

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(QtGui.QDialog):

    def openDialog(self):
        print "hola"
    
    def File1(self):
        self.ruta1=str(QtGui.QFileDialog.getOpenFileName(self, 'Open File1'))
        FILE = File(self.ruta1 ,None)
        self.tiposFile1= FILE.getTypeF1()
        #tiposF2= FILE.getTypeF2()
        self.camposFile1= FILE.getCeldasF1()
        #celdasF2= FILE.getCeldasF2()

        self.combo1.addItems(self.camposFile1)
        #self.combo2.addItems(celdasF2)
        
        self.select_file_1.setEnabled(False)

        self.combo1.activated.connect(self.fillList1)

    def File2(self):
        self.ruta2= str(QtGui.QFileDialog.getOpenFileName(self, 'Open File2'))
        FILE = File(None,self.ruta2)
        #tiposF1= FILE.getTypeF1()
        self.tiposFile2= FILE.getTypeF2()
        #celdasF1= FILE.getCeldasF1()
        self.camposFile2= FILE.getCeldasF2()

        #self.combo1.addItems(celdasF1)
        self.combo2.addItems(self.camposFile2)
        
        #self.select_file_1.setEnabled(False)
        self.select_file_2.setEnabled(False)

        self.combo2.activated.connect(self.fillList2)
        #self.combo1.activated.connect(self.fillList1)

    def fillList1(self):
        text = self.combo1.currentText()
        self.lista1.addItems([text])
        self.campos_lista1.append(str(text))
        print text


        indice = self.combo1.currentIndex()
        self.indices_lista1.append(indice)

    def fillList2(self):
        text = self.combo2.currentText()
        self.lista2.addItems([text])
        self.campos_lista2.append(str(text))
        print text


        indice = self.combo2.currentIndex()
        self.indices_lista2.append(indice)

    def make(self):
        self.NewFileCampos=self.campos_lista1
        self.NewFileCampos+=self.campos_lista2

        for i in range(len(self.indices_lista1)):
            self.NewFileTipos.append(self.tiposFile1[self.indices_lista1[i]])
    
        for i in range(len(self.indices_lista2)):
            self.NewFileTipos.append(self.tiposFile2[self.indices_lista2[i]])

        FILE = File(self.ruta1, self.ruta2)

        cantFile1 = int
        cantFile2 = int
        cantFile1= FILE.getCantFile1()
        cantFile2= FILE.getCantFile2()
        reg_totales = int
        reg_totales = cantFile1+cantFile2

    
        print reg_totales
        print self.NewFileTipos
        print self.NewFileCampos 
        
        FILE.createNewFile(self.NewFileTipos, self.NewFileCampos, reg_totales)
        FILE.write_in_newFile(self.indices_lista1, self.indices_lista2)

    def __init__ (self):
        self.ruta1 =""
        self.ruta2 =""
        self.NewFileCampos= []
        self.NewFileTipos=[]
        self.indices_lista1 = []
        self.campos_lista1 =[]
        self.indices_lista2 = []
        self.campos_lista2 =[]
        self.tiposFile1 =[]
        self.tiposFile2 =[]
        self.camposFile1=[]
        self.camposFile2=[]
        QtGui.QDialog.__init__(self)
        uic.loadUi("crossFiles.ui",self)
        self.select_file_1.clicked.connect(self.File1)
        self.select_file_2.clicked.connect(self.File2)
        self.fusion.clicked.connect(self.make)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dialog = Ui_Dialog()
    dialog.show()
    sys.exit(app.exec_())

