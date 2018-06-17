from PyQt4 import QtCore, QtGui
from Numfields import Numfields
from Type import Type
from xlsxwriter import Workbook


class toolkit(object):
    @staticmethod
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
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)

    def exportxml(self, window):
        name = QtGui.QFileDialog.getOpenFileName(window, 'Open File')

        f = open(name, "r+")
        cadena = f.readline()
        cadena = cadena.replace("[", "")
        cadena = cadena.replace("]", "")
        cadena = cadena.replace("\'", "")
        cadena = cadena.replace("\n", "")
        self.lista_tipos = cadena.split(",")

        #######################
        cadena = f.readline()
        cadena = cadena.replace("[", "")
        cadena = cadena.replace("]", "")
        cadena = cadena.replace("\'", "")
        cadena = cadena.replace("\n", "")
        self.lista_nombres = cadena.split(",")
        #######################
        rows = f.readline()
        rows = rows.replace("\n", "")
        self.cantidad = int(rows)
        root = et.Element("root")
        for i in range(self.cantidad):
            temp = f.readline()
            temp = temp.replace("\n", "")
            temp = temp.replace(" ", "")
            aux = temp.split("|")
            for j in range(len(self.lista_nombres)):
                et.SubElement(root, str(self.lista_nombres[j])).text = aux[j]
            del aux
            del temp
        f.close()
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Information)
        msg.setText("The export is done!")
        msg.setWindowTitle("Export XML")
        retval = msg.exec_()
        del cadena
        del retval
        tree = et.ElementTree(root)
        tree.write(str(name).replace(".qls", ".XML"))

    def exportxlsx(self, window):
        name = QtGui.QFileDialog.getOpenFileName(window, 'Open File')

        f = open(name, "r+")
        workbook = Workbook(str(name).replace(".qls", ".xlsx"))
        worksheet = workbook.add_worksheet()
        cadena = f.readline()
        cadena = cadena.replace("[", "")
        cadena = cadena.replace("]", "")
        cadena = cadena.replace("\'", "")
        cadena = cadena.replace("\n", "")
        self.lista_tipos = cadena.split(",")

        #######################
        cadena = f.readline()
        cadena = cadena.replace("[", "")
        cadena = cadena.replace("]", "")
        cadena = cadena.replace("\'", "")
        cadena = cadena.replace("\n", "")
        self.lista_nombres = cadena.split(",")
        #######################
        worksheet.write_row(0, 0, self.lista_nombres)
        rows = f.readline()
        rows = rows.replace("\n", "")
        self.cantidad = int(rows)
        for i in range(self.cantidad):
            temp = f.readline()
            temp = temp.replace("\n", "")
            temp = temp.replace(" ", "")
            aux = temp.split("|")
            for j in range(len(self.lista_nombres)):
                worksheet.write_string(i+1, j, aux[j])
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
