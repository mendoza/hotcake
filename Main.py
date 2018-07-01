# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

import sys
from Btree import BTree
from Node import Node
from dropdown import dropdown
from PyQt4 import QtCore, QtGui, uic
from functools import partial
from Numfields import Numfields
from Type import Type
from xlsxwriter import Workbook
from lxml import etree as et
from file import File
from crossFiles import Ui_Dialog

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


class Ui_MainWindow(QtGui.QMainWindow):
    actual = 0
    proximo = 0
    stack = []
    direccion = ""
    batch = 20
    file = None

    def mod_campos(self):
        if self.cantidad != 0:
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Information)
            msg.setText("Ya no puede editar sus campos")
            msg.setWindowTitle("Error")
            retval = msg.exec_()
        else:
            windo = dropdown(self.lista_nombres)
            windo.show()
            if windo.exec_():
                elegido = windo.reto()
                self.dialog2 = QtGui.QDialog()
                self.ui2 = Type()
                self.ui2.setupUi(self.dialog2)
                self.dialog2.show()
                if self.dialog2.exec_():
                    self.lista_tipos[self.lista_nombres.index(elegido)] = self.ui2.get_types()
                    self.lista_nombres[self.lista_nombres.index(elegido)] = self.ui2.get_name()
                with open(self.direccion,'w') as file:
                    file.write(str(self.lista_tipos))
                    file.write('\n')
                    file.write(str(self.lista_nombres))
                    file.write('\n')                    
                    par = '%' + str(10) + 'd'
                    new_size = (par % 0)
                    file.write(new_size)
                    file.write('\n')
                    self.tableWidget.setHorizontalHeaderLabels(self.lista_nombres)

    def del_campos(self):
        if self.cantidad != 0:
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Information)
            msg.setText("Ya no puede editar sus campos")
            msg.setWindowTitle("Error")
            retval = msg.exec_()
        else:
            windo = dropdown(self.lista_nombres)
            windo.show()
            if windo.exec_():
                elegido = windo.reto()
                self.lista_tipos.pop(self.lista_nombres.index(elegido))
                self.lista_nombres.pop(self.lista_nombres.index(elegido))
                print(self.lista_nombres)
                print(self.lista_tipos)
                with open(self.direccion,'w') as file:
                    file.write(str(self.lista_tipos))
                    file.write('\n')
                    file.write(str(self.lista_nombres))
                    file.write('\n')                    
                    par = '%' + str(10) + 'd'
                    new_size = (par % 0)
                    file.write(new_size)
                    file.write('\n')
                    self.tableWidget.setColumnCount(len(self.lista_nombres))
                    self.tableWidget.setHorizontalHeaderLabels(self.lista_nombres)

    def merge_files(self, window):
        Dialog = QtGui.QDialog()
        ui = Ui_Dialog()
        ui.show()
        ui.exec_()
# FUNCION QUE REALIZA LA INDEXACION CUANDO SELECCIONA UN ARCHIVO

    def indexando(self, window):
        try:
            #ruta = QtGui.QFileDialog.getOpenFileName(window, 'Open File')
            # -------------------
            # B_tree: Es el arbol
            B_tree = BTree(6)
            # Abrimos el archivo seleccionado en forma de lectura

            """
            name=str(QtGui.QFileDialog.getOpenFileName(self, 'Index File'))
            #name = QtGui.QFileDialog.getOpenFileName(window, 'Open File')
            self.direccion = str(name)
            """

            #file = open(name, "r+")
            file = open(self.direccion, "r+")
            # Seek: nos ayuda a posicionarnos al incio del archivo
            file.seek(0)
            # Realizamos 2 readline() porque esos contienen metadata y asi posicionarnos en los registros
            file.readline()
            file.readline()
            # 3ra linea del archivo siempre es la cantidad de registros guardados
            totales = file.readline()
            # realizamos n cantidad de repeticiones que dependen de la cantidad de registros guardados
            for i in range(int(totales)):
                # temp: Es la variable que toma cada registro
                temp = file.readline()
                # lista_temp: Hacemos una lista de los campos de los registros
                lista_temp = temp.split("|")
                # Es aqui donde insertamos al nuestro arbol b
                B_tree.insert(lista_temp[0])
                # --------------QUITAR COMENTARIO , Solo en caso de querer ver dato por dato ingresado en nuestro arbol
                #print "Codigo---", lista_temp[0]
            print B_tree
            # Creamos una instancia del objeto FILE
            FILE = File()
            # Mandamos a escribir el arbol en un archivo con la extension -> .qls
            FILE.write_tree(B_tree)

        except IOError:
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Information)
            msg.setText("NO SELECCIONO ARCHIVO ALGUNO")
            msg.setWindowTitle("Error")
            retval = msg.exec_()

    def save(self):
        if len(file.buffer) != 0:   
            file.write_entry()
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Information)
            msg.setText("Saving Done")
            msg.setWindowTitle("Save")
            retval = msg.exec_()

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
        par = '%' + str(10) + 'd'
        new_size = (par % 0)
        file.write(new_size+'\n')

    def new_entry(self):
        nuevo = []
        for _ in range(len(self.lista_nombres)):
            text, ok = QtGui.QInputDialog.getText(
                self, 'Text Input Dialog', 'Enter your new '+str(self.lista_nombres[_])+':')
            nuevo.append(str(text))
        self.cantidad += 1
        self.file.buffer_add(nuevo)

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
        self.tableWidget.setRowCount(0)
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
            with open(self.direccion, "r+") as file:
                file.seek(self.actual)
                proximo = self.calculate_next_byte(
                    file, self.actual, self.batch)
                self.actual += proximo
                self.stack.append(proximo)
                self.set_entries(file, self.batch)
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
            temp = self.remove_chars(["\n", " "], temp)
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
        bold = workbook.add_format({'bold': True})
        worksheet.write_row(0, 0, self.lista_nombres, bold)
        rows = f.readline()
        rows = self.remove_chars(["\n"], rows)
        self.cantidad = int(rows)
        for i in range(self.cantidad):
            temp = f.readline()
            temp = self.remove_chars(["\n", " "], temp)
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

    def open_File(self, window,dire=None):
        try:
            self.actual = 0
            self.proximo = 0
            self.stack = []
            self.direccion = ""
            self.batch = 20
            self.file = None
            name = QtGui.QFileDialog.getOpenFileName(window, 'Open File')
            self.direccion = str(name)
            f = open(name, "r+")
            cadena = f.readline()
            self.actual += len(cadena)
            cadena = self.remove_chars(["[", "]", "\'", "\n"], cadena)
            self.lista_tipos = cadena.split(",")
            #######################
            #################
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
            self.file = File(self.direccion)
            f.close()
        except IOError:
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Information)
            msg.setText("NO SELECCIONO ARCHIVO ALGUNO")
            msg.setWindowTitle("Error")
            retval = msg.exec_()

    def esci(self):
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Information)
        msg.setText("Goodbye")
        msg.setWindowTitle("Exit")
        retval = msg.exec_()
        sys.exit()

    def reindexar(self):
        FILE = File(self.direccion)
        records,metadata = FILE.getRecords()
        btree = BTree(6)
        aux = []
        for record in records:
            cadena = ""
            for i in range(len(record)):
                if i == len(record)-1:
                    cadena += str(record[i])+"\n"
                else:
                    cadena += str(record[i])+"|"
            btree.insert(cadena)

        with open(self.direccion,"w") as file:
            for meta in metadata:
                file.write(str(meta))
                file.write("\n")
            for i in btree:
                file.write(str(i))
        self.tableWidget.setHorizontalHeaderLabels(metadata[1])        
        
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        uic.loadUi("Main.ui", self)
        self.actionOpen.triggered.connect(partial(self.open_File, self))
        self.actionOpen.triggered.connect(self.indexando)
        self.actionNew_Structure.triggered.connect(partial(self.new_entry))
        self.actionXML.triggered.connect(partial(self.exportxml, self))
        self.actionNew_File.triggered.connect(
            partial(self.new_file, self))
        self.Previous_button.clicked.connect(partial(self.previous_batch))
        self.Next_button.clicked.connect(partial(self.next_batch))
        self.actionMerge_Files.triggered.connect(self.merge_files)
        self.actionSave.triggered.connect(self.save)
        self.actionModify_fields.triggered.connect(partial(self.mod_campos))
        self.actionRemove_fields.triggered.connect(partial(self.del_campos))
        self.actionExit.triggered.connect(self.esci)
        self.actionRe_Index_Files.triggered.connect(self.reindexar)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    windo = Ui_MainWindow()
    windo.show()
    sys.exit(app.exec_())
