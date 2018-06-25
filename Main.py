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
from xlsxwriter import Workbook
from lxml import etree as et

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
    actual = 0
    proximo = 0
    stack = []
    direccion = ""
    batch = 10

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(808, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Images/database.png")),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.Previous_button = QtGui.QPushButton(self.centralwidget)
        self.Previous_button.clicked.connect(partial(self.previous_batch))
        self.Previous_button.setObjectName(_fromUtf8("Previous_button"))
        self.horizontalLayout.addWidget(self.Previous_button)
        spacerItem = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Next_button = QtGui.QPushButton(self.centralwidget)
        self.Next_button.clicked.connect(partial(self.next_batch))
        self.Next_button.setObjectName(_fromUtf8("Next_button"))
        self.horizontalLayout.addWidget(self.Next_button)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
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
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionOpen.triggered.connect(partial(self.open_File, MainWindow))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionNew_Structure = QtGui.QAction(MainWindow)
        self.actionNew_Structure.setObjectName(
            _fromUtf8("actionNew_Structure"))
        self.actionNew_Structure.triggered.connect(partial(self.new_entry))
        self.actionEdit_Structure = QtGui.QAction(MainWindow)
        self.actionEdit_Structure.setObjectName(
            _fromUtf8("actionEdit_Structure"))
        self.actionExcel = QtGui.QAction(MainWindow)
        self.actionExcel.setObjectName(_fromUtf8("actionExcel"))
        self.actionExcel.triggered.connect(
            partial(self.exportxlsx, MainWindow))
        self.actionXML = QtGui.QAction(MainWindow)
        self.actionXML.setObjectName(_fromUtf8("actionXML"))
        self.actionXML.triggered.connect(partial(self.exportxml, MainWindow))
        self.actionAdd = QtGui.QAction(MainWindow)
        self.actionAdd.setObjectName(_fromUtf8("actionAdd"))
        self.actionRemove = QtGui.QAction(MainWindow)
        self.actionRemove.setObjectName(_fromUtf8("actionRemove"))
        self.actionNew_File = QtGui.QAction(MainWindow)
        self.actionNew_File.setObjectName(_fromUtf8("actionNew_File"))
        self.actionNew_File.triggered.connect(
            partial(self.new_file, MainWindow))
        self.menuFile.addAction(self.actionNew_File)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuStructure.addAction(self.actionNew_Structure)
        self.menuStructure.addAction(self.actionEdit_Structure)
        self.menuExport.addAction(self.actionExcel)
        self.menuExport.addAction(self.actionXML)
        self.menuOptions.addAction(self.menuExport.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuStructure.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Entrance", None))
        self.Previous_button.setText(
            _translate("MainWindow", "Previous", None))
        self.Next_button.setText(_translate("MainWindow", "Next", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuStructure.setTitle(_translate("MainWindow", "Entry", None))
        self.menuOptions.setTitle(_translate("MainWindow", "Options", None))
        self.menuExport.setTitle(_translate("MainWindow", "Export ", None))
        self.actionOpen.setText(_translate("MainWindow", "Open File", None))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionSave.setText(_translate("MainWindow", "Save File", None))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.actionNew_Structure.setText(
            _translate("MainWindow", "New Entry", None))
        self.actionNew_Structure.setShortcut(
            _translate("MainWindow", "Alt+S", None))
        self.actionEdit_Structure.setText(
            _translate("MainWindow", "Remove Entry", None))
        self.actionEdit_Structure.setShortcut(
            _translate("MainWindow", "Alt+E", None))
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
            self.dialog2 = QtGui.QDialog()
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

    def new_entry(self):
        if (self.cantidad/self.batch) - 1 == len(self.stack):
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)

    def calculate_next_byte(self, file, lastbyte, batch):
        total = ""
        file.seek(0)
        file.seek(lastbyte)
        for i in range(batch):
            linea = file.readline()
            total += linea
        ret = len(total)
        return ret
    """ asigna a la tabla la cantidad dada usandola desde el byte predeterminado en el file """

    def set_entries(self, file, cant):
        self.tableWidget.setRowCount(cant)
        for i in range(cant):
            temp = file.readline()
            temp = self.remove_chars(["\n", " "], temp)
            aux = temp.split("|")
            for j in range(self.tableWidget.columnCount()):
                self.tableWidget.setItem(i, j, QtGui.QTableWidgetItem(aux[j]))
        self.tableWidget.resizeColumnsToContents()
    """calcula la siguiente ronda de registros, junto con el byte que se agrega al stack"""

    def next_batch(self):
        try:
            if (self.cantidad/self.batch) - 1 != len(self.stack):
                with open(self.direccion, "r+") as file:
                    file.seek(self.actual)
                    proximo = self.calculate_next_byte(
                        file, self.actual, self.batch)
                    self.actual += proximo
                    self.set_entries(file, self.batch)
                    self.stack.append(proximo)
        except:
            print("Last One")
    """calcula la anterior ronda de registros, consiguiendo el byte anterior del stack"""

    def previous_batch(self):
        try:
            with open(self.direccion, "r+") as file:
                val = self.stack.pop()
                self.actual -= val
                file.seek(0)
                file.seek(self.actual)
                self.set_entries(file, self.batch)
        except:
            print("First One")

    def exportxml(self, window):
        f = open(self.direccion, "r+")
        cadena = f.readline()
        cadena = self.remove_chars(["[", "]", "\'", "\n"], cadena)
        self.lista_tipos = cadena.split(",")
        #######################
        cadena = f.readline()
        cadena = self.remove_chars(["[", "]", "\'", "\n"], cadena)
        self.lista_nombres = cadena.split(",")
        #######################
        rows = f.readline()
        rows = self.remove_chars(["\n"], rows)
        self.cantidad = int(rows)
        root = et.Element("Root")
        for i in range(self.cantidad):
            register = et.Element("Register")
            temp = f.readline()
            temp = temp.replace("\n", "")
            temp = temp.replace(" ", "")
            aux = temp.split("|")
            for j in range(len(self.lista_nombres)):
                et.SubElement(register, str(
                    self.lista_nombres[j]).replace(" ", "")).text = aux[j]
            del aux
            del temp
            root.append(register)
        f.close()
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Information)
        msg.setText("The export is done!")
        msg.setWindowTitle("Export XML")
        retval = msg.exec_()
        del cadena
        del retval
        tree = et.ElementTree(root)
        tree.write(str(self.direccion).replace(".qls", ".XML"),
                   pretty_print=True, xml_declaration=True,   encoding="utf-8")

    def exportxlsx(self, window):
        f = open(self.direccion, "r+")
        workbook = Workbook(str(self.direccion).replace(".qls", ".xlsx"))
        worksheet = workbook.add_worksheet()
        cadena = f.readline()
        cadena = self.remove_chars(["[", "]", "\'", "\n"], cadena)
        self.lista_tipos = cadena.split(",")

        #######################
        cadena = f.readline()
        cadena = self.remove_chars(["[", "]", "\'", "\n"], cadena)
        self.lista_nombres = cadena.split(",")
        #######################
        worksheet.write_row(0, 0, self.lista_nombres)
        rows = f.readline()
        rows = self.remove_chars(["\n"], rows)
        self.cantidad = int(rows)
        for i in range(self.cantidad):
            temp = f.readline()
            temp = temp.replace("\n", "")
            temp = temp.replace(" ", "")
            aux = temp.split("|")
            for j in range(len(self.lista_nombres)):
                worksheet.write_string(i + 1, j, aux[j])
            del aux
            del temp
        f.close()
        workbook.close()
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Information)
        msg.setText("The export is done!")
        msg.setWindowTitle("Export Excel")
        retval = msg.exec_()
        del cadena
        del retval

    def remove_chars(self, lista, cadena):
        for char in lista:
            cadena = cadena.replace(char, "")
        return cadena

    def open_File(self, window):
        self.actual = 0
        self.proximo = 0
        name = QtGui.QFileDialog.getOpenFileName(window, 'Open File')
        self.direccion = str(name)
        f = open(name, "r+")
        cadena = f.readline()
        self.actual += len(cadena)
        cadena = self.remove_chars(["[", "]", "\'", "\n"], cadena)
        self.lista_tipos = cadena.split(",")
        #######################
        cadena = f.readline()
        self.actual += len(cadena)
        cadena = self.remove_chars(["[", "]", "\'", "\n"], cadena)
        self.lista_nombres = cadena.split(",")
        #######################
        rows = f.readline()
        self.actual += len(rows)
        rows = self.remove_chars(["\n"], rows)
        self.tableWidget.setColumnCount(len(self.lista_tipos))
        self.tableWidget.setHorizontalHeaderLabels(self.lista_nombres)
        self.cantidad = int(rows)
        if self.batch >= self.cantidad:
            self.Previous_button.setVisible(False)
            self.Next_button.setVisible(False)
        else:
            self.Previous_button.setVisible(True)
            self.Next_button.setVisible(True)
        self.set_entries(f, self.batch)
        f.close()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
