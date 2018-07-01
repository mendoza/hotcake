# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crossFiles.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import sys
from file import File
from PyQt4.QtGui import *

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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(537, 412)
        self.select_file_1 = QtGui.QPushButton(Dialog)
        self.select_file_1.setGeometry(QtCore.QRect(20, 30, 181, 21))
        self.select_file_1.setObjectName(_fromUtf8("select_file_1"))
        ###############
        #self.select_file_1.clicked.connect(self.openDialog)
        self.select_file_1.clicked.connect(self.File1)
        self.select_file_2 = QtGui.QPushButton(Dialog)
        self.select_file_2.setGeometry(QtCore.QRect(320, 30, 181, 21))
        self.select_file_2.setObjectName(_fromUtf8("select_file_2"))
        self.combo1 = QtGui.QComboBox(Dialog)
        self.combo1.setGeometry(QtCore.QRect(20, 80, 181, 27))
        self.combo1.setObjectName(_fromUtf8("combo1"))

        self.combo2 = QtGui.QComboBox(Dialog)
        self.combo2.setGeometry(QtCore.QRect(320, 80, 181, 27))
        self.combo2.setObjectName(_fromUtf8("combo2"))
        self.lista1 = QtGui.QListView(Dialog)
        self.lista1.setGeometry(QtCore.QRect(20, 130, 181, 161))
        self.lista1.setObjectName(_fromUtf8("lista1"))
        self.lista2 = QtGui.QListView(Dialog)
        self.lista2.setGeometry(QtCore.QRect(320, 130, 181, 161))
        self.lista2.setObjectName(_fromUtf8("lista2"))
        self.fusion = QtGui.QPushButton(Dialog)
        self.fusion.setGeometry(QtCore.QRect(130, 330, 271, 27))
        self.fusion.setObjectName(_fromUtf8("fusion"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def openDialog(self):
        print "hola"
    
    def File1(self):
        ruta1= "Nuevo.qls"
        ruta2= "Nuevo.qls"
        FILE = File(ruta1,ruta2)
        tiposF1= FILE.getTypeF1()
        #tiposF2= FILE.getTypeF2()
        celdasF1= FILE.getCeldasF1()
        #celdasF2= FILE.getCeldasF2()

        self.combo1.addItems(celdasF1)
        #self.combo2.addItems(celdasF2)
        
        self.select_file_1.setEnabled(False)

        self.combo1.activated.connect(self.fillList)

    def fillList(self):
        text = self.combo1.currentText()
        print text

        
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.select_file_1.setText(_translate("Dialog", "Select File", None))
        self.select_file_2.setText(_translate("Dialog", "Select File", None))
        self.fusion.setText(_translate("Dialog", "MAKE ", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

