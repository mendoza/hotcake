# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton_selected = QtGui.QPushButton(self.centralwidget)
        self.pushButton_selected.setObjectName(_fromUtf8("pushButton_selected"))
        self.verticalLayout.addWidget(self.pushButton_selected)
        self.pushButton_add = QtGui.QPushButton(self.centralwidget)
        self.pushButton_add.setObjectName(_fromUtf8("pushButton_add"))
        self.verticalLayout.addWidget(self.pushButton_add)
        self.pushButton_remove = QtGui.QPushButton(self.centralwidget)
        self.pushButton_remove.setObjectName(_fromUtf8("pushButton_remove"))
        self.verticalLayout.addWidget(self.pushButton_remove)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 808, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuStructure = QtGui.QMenu(self.menubar)
        self.menuStructure.setObjectName(_fromUtf8("menuStructure"))
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
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuStructure.addAction(self.actionNew_Structure)
        self.menuStructure.addAction(self.actionEdit_Structure)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuStructure.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Entrance", None))
        self.pushButton_selected.setText(_translate("MainWindow", "remove selected", None))
        self.pushButton_add.setText(_translate("MainWindow", "Add Row", None))
        self.pushButton_remove.setText(_translate("MainWindow", "Remove last", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuStructure.setTitle(_translate("MainWindow", "Structure", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.actionNew_Structure.setText(_translate("MainWindow", "New Structure", None))
        self.actionNew_Structure.setShortcut(_translate("MainWindow", "Alt+S", None))
        self.actionEdit_Structure.setText(_translate("MainWindow", "Edit Structure", None))
        self.actionEdit_Structure.setShortcut(_translate("MainWindow", "Alt+E", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

