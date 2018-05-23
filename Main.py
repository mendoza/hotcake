# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from functools import partial
import Toolkit
from Numfields import Numfields
from Type import Type
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(808, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Images/database.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 808, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuStructure = QtGui.QMenu(self.menubar)
        self.menuStructure.setObjectName(_fromUtf8("menuStructure"))
        self.menuOptions = QtGui.QMenu(self.menubar)
        self.menuOptions.setObjectName(_fromUtf8("menuOptions"))
        self.menuExport = QtGui.QMenu(self.menuOptions)
        self.menuExport.setObjectName(_fromUtf8("menuExport"))
        self.menuRegister = QtGui.QMenu(self.menuOptions)
        self.menuRegister.setObjectName(_fromUtf8("menuRegister"))
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionNew_Structure = QtGui.QAction(MainWindow)
        self.actionNew_Structure.setObjectName(_fromUtf8("actionNew_Structure"))
        self.actionEdit_Structure = QtGui.QAction(MainWindow)
        self.actionEdit_Structure.setObjectName(_fromUtf8("actionEdit_Structure"))
        self.actionExcel = QtGui.QAction(MainWindow)
        self.actionExcel.setObjectName(_fromUtf8("actionExcel"))
        self.actionXML = QtGui.QAction(MainWindow)
        self.actionXML.setObjectName(_fromUtf8("actionXML"))
        self.actionAdd = QtGui.QAction(MainWindow)
        self.actionAdd.setObjectName(_fromUtf8("actionAdd"))
        self.actionRemove = QtGui.QAction(MainWindow)
        self.actionRemove.setObjectName(_fromUtf8("actionRemove"))
        self.actionNew_File = QtGui.QAction(MainWindow)
        self.actionNew_File.setObjectName(_fromUtf8("actionNew_File"))
        self.actionNew_File.triggered.connect(partial(self.new_file,MainWindow));        
        self.menuFile.addAction(self.actionNew_File)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuStructure.addAction(self.actionNew_Structure)
        self.menuStructure.addAction(self.actionEdit_Structure)
        self.menuExport.addAction(self.actionExcel)
        self.menuExport.addAction(self.actionXML)
        self.menuRegister.addAction(self.actionAdd)
        self.menuRegister.addAction(self.actionRemove)
        self.menuOptions.addAction(self.menuExport.menuAction())
        self.menuOptions.addAction(self.menuRegister.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuStructure.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Entrance", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuStructure.setTitle(_translate("MainWindow", "Entry", None))
        self.menuOptions.setTitle(_translate("MainWindow", "Options", None))
        self.menuExport.setTitle(_translate("MainWindow", "Export ", None))
        self.menuRegister.setTitle(_translate("MainWindow", "Register", None))
        self.actionOpen.setText(_translate("MainWindow", "Open File", None))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionSave.setText(_translate("MainWindow", "Save File", None))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.actionNew_Structure.setText(_translate("MainWindow", "New Entry", None))
        self.actionNew_Structure.setShortcut(_translate("MainWindow", "Alt+S", None))
        self.actionEdit_Structure.setText(_translate("MainWindow", "Remove Entry", None))
        self.actionEdit_Structure.setShortcut(_translate("MainWindow", "Alt+E", None))
        self.actionNew_File.setShortcut(_translate("MainWindow","Ctrl+N",None))
        self.actionExcel.setText(_translate("MainWindow", "Excel", None))
        self.actionXML.setText(_translate("MainWindow", "XML", None))
        self.actionAdd.setText(_translate("MainWindow", "Add", None))
        self.actionRemove.setText(_translate("MainWindow", "Remove", None))
        self.actionNew_File.setText(_translate("MainWindow", "New File", None))

    def new_file(self, window):
        name = QtGui.QFileDialog.getSaveFileName(window, 'New File')
        if not name.endsWith('.qls'):
            name += '.qls'
        file = open(name, 'w')
        self.Dialog = QtGui.QDialog()
        self.ui = Numfields()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()
        if self.Dialog.exec_():
            cant = self.ui.getNum()
        tipos = []
        nombres = []
        for i in range(cant):
            self.dialog2 =QtGui.QDialog()
            self.ui2 = Type()
            self.ui2.setupUi(self.dialog2)
            self.dialog2.show()
            if self.dialog2.exec_():
                tipos.append(self.ui2.get_types())
                nombres.append(self.ui2.get_name())
        file.write(str(tipos))
        file.write('\n')
        file.write(str(nombres))
        file.write('\n')
        file.write('0\n')
        file.close()
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

