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
from search_table import search_table

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
    archivo = None
    buffer = []

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
                    self.lista_tipos[self.lista_nombres.index(
                        elegido)] = self.ui2.get_types()
                    self.lista_nombres[self.lista_nombres.index(
                        elegido)] = self.ui2.get_name()
                with open(self.direccion, 'w') as file:
                    file.write(str(self.lista_tipos))
                    file.write('\n')
                    file.write(str(self.lista_nombres))
                    file.write('\n')
                    par = '%' + str(10) + 'd'
                    new_size = (par % 0)
                    file.write(new_size)
                    end = (par % -1)
                    file.write('&'+end)
                    file.write('\n')
                    self.tableWidget.setHorizontalHeaderLabels(
                        self.lista_nombres)

    def getAvailList(self):
        with open(self.direccion, "r+") as file:
            file.readline()
            file.readline()
            metadata = file.readline()
            metadata = metadata.split("&")
            metadata = metadata[1]
            if int(metadata) < 0:
                print "No hay HEAD"
            elif int(metadata) > 0:
                self.avail_list.append(int(metadata))
                self.agregar(metadata)

    def agregar(self, lastOne):
        file = open(self.direccion, "r+")
        file.seek(0)

        for i in range(3):
            file.readline()

        nextOne = ""
        for i in range(int(lastOne)):
            nextOne = file.readline()
            if nextOne[0] == '*':
                nextOne = nextOne.split("&")
                nextOne = nextOne[0]
                nextOne = nextOne.replace("*", "")
                nextOne = int(nextOne)
        self.avail_list.append(nextOne)
        if nextOne != -1:
            self.agregar(nextOne)

        file.close()

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
                with open(self.direccion, 'w') as file:
                    file.write(str(self.lista_tipos))
                    file.write('\n')
                    file.write(str(self.lista_nombres))
                    file.write('\n')
                    par = '%' + str(10) + 'd'
                    new_size = (par % 0)
                    file.write(new_size)
                    end = (par % -1)
                    file.write('&'+end)
                    file.write('\n')
                    self.tableWidget.setColumnCount(len(self.lista_nombres))
                    self.tableWidget.setHorizontalHeaderLabels(
                        self.lista_nombres)

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
            self.B_tree = BTree(6)
            # Abrimos el archivo seleccionado en forma de lectura
            #file = open(name, "r+")
            file = open(self.direccion, "r+")
            # Seek: nos ayuda a posicionarnos al incio del archivo
            file.seek(0)
            # Realizamos 2 readline() porque esos contienen metadata y asi posicionarnos en los registros
            file.readline()
            file.readline()
            # 3ra linea del archivo siempre es la cantidad de registros guardados
            aux = file.readline().split("&")
            totales, head = aux[0], aux[1]
            # realizamos n cantidad de repeticiones que dependen de la cantidad de registros guardados
            for i in range(int(totales)):
                # temp: Es la variable que toma cada registro
                temp = file.readline()
                # lista_temp: Hacemos una lista de los campos de los registros
                lista_temp = temp.split("|")
                # Es aqui donde insertamos al nuestro arbol b
                if '*' not in lista_temp[0]:
                    self.B_tree.insert(temp)
                # --------------QUITAR COMENTARIO , Solo en caso de querer ver dato por dato ingresado en nuestro arbol
                #print "Codigo---", lista_temp[0]
            # Creamos una instancia del objeto FILE
            FILE = File()
            # Mandamos a escribir el arbol en un archivo con la extension -> .qls
            FILE.write_tree(self.B_tree)

        except IOError:
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Information)
            msg.setText("NO SELECCIONO ARCHIVO ALGUNO")
            msg.setWindowTitle("Error")
            retval = msg.exec_()

    def save(self):
        if len(self.buffer) != 0:
            print("entre")
            for registro in self.buffer:
                if len(self.avail_list)-1 == 0:
                    self.archivo.write_entry([registro])
                else:
                    print("entre2")
                    with open(self.direccion, 'r+') as file:
                        for offset in self.avail_list:
                            if offset != -1:
                                for i in range(offset+3):
                                    aux = file.readline()
                                    cade = ""
                                    for j in range(len(registro)):
                                        if j == len(registro)-1:
                                            cade += registro[j]+"\n"
                                        else:
                                            cade += registro[j]+"|"
                                if len(cade) == len(aux):
                                    file.seek(-len(aux), 1)
                                    file.write(cade)
                                    indice = self.avail_list.index(offset)
                                    anterior = self.avail_list.pop(indice)
                                    print(indice, anterior)
                                    print(self.avail_list)
                                    if indice == 0:
                                        file.seek(0)
                                        file.readline()
                                        file.readline()
                                        era = file.readline()
                                        eral = era.split('&')
                                        par = '%' + str(10) + 'd'
                                        valueint = int(eral[0])
                                        valueint += 1
                                        new_size = (par % valueint)
                                        valueend = self.avail_list[indice+1]
                                        new_end = (par % valueend)
                                        file.seek(-22, 1)
                                        file.write(new_size+'&'+new_end+"\n")
                                        break
                                    else:
                                        file.seek(0)
                                        print(self.avail_list)
                                        for b in range(self.avail_list[indice-1]+3):
                                            line = file.readline()
                                        file.seek(-len(line), 1)
                                        file.write(
                                            "*"+str(self.avail_list[indice])+"&")
                                        file.seek(0)
                                        break

                                    break
                            else:
                                self.archivo.write_entry([registro])
                            file.seek(0)

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
        end = (par % -1)
        file.write(new_size+'&'+end+'\n')

    def new_entry(self):
        nuevo = []
        for _ in range(len(self.lista_nombres)):
            text, ok = QtGui.QInputDialog.getText(
                self, 'New Entry', 'Enter your new '+str(self.lista_nombres[_])+':')
            nuevo.append(str(text))
        self.cantidad += 1
        self.buffer.append(nuevo)

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
        n = 0
        lastn = 0
        for i in range(cant):
            temp = file.readline()
            temp = self.remove_chars(["\n", " "], temp)
            aux = temp.split("|")
            if '*' in aux[0]:
                n += 1
            for j in range(self.tableWidget.columnCount()):
                if '*' not in aux[0]:
                    self.tableWidget.setItem(
                        i-n, j, QtGui.QTableWidgetItem(aux[j]))
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
            print("first one")

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
        rows = f.readline().split()[0]
        rows = self.remove_chars(["\n"], rows)
        self.cantidad = int(rows)
        root = et.Element("Root")
        for i in range(self.cantidad):
            register = et.Element("Register")
            temp = f.readline()
            temp = self.remove_chars(["\n", " "], temp)
            aux = temp.split("|")
            for j in range(len(self.lista_nombres)):
                if '*' not in aux[0]:
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
        rows = f.readline().split()[0]
        rows = self.remove_chars(["\n"], rows)
        self.cantidad = int(rows)
        n = 0
        for i in range(self.cantidad):
            temp = f.readline()
            temp = self.remove_chars(["\n", " "], temp)
            aux = temp.split("|")
            if '*' in aux[0]:
                n += 1
            for j in range(len(self.lista_nombres)):
                if '*' not in aux[0]:
                    worksheet.write_string(i - n + 1, j, aux[j])
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

    def open_File(self, window, dire=None):
        try:
            self.avail_list = []
            self.actual = 0
            self.proximo = 0
            self.stack = []
            self.direccion = ""
            self.batch = 20
            self.archivo = None
            name = QtGui.QFileDialog.getOpenFileName(window, 'Open File')
            self.direccion = str(name)
            self.archivo = File(name)
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
            rows = f.readline().split()[0]
            self.actual += len(rows)
            rows = self.remove_chars(["\n"], rows)
            self.tableWidget.setColumnCount(len(self.lista_tipos))
            self.tableWidget.setHorizontalHeaderLabels(self.lista_nombres)
            self.cantidad = int(rows.split("&")[0])
            if self.batch >= self.cantidad:
                self.Previous_button.setVisible(False)
                self.Next_button.setVisible(False)
                self.batch = self.cantidad
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
        records, metadata = FILE.getRecords()
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

        with open(self.direccion, "w") as file:
            for meta in metadata:
                file.write(str(meta))
                file.write("\n")
            for i in btree:
                file.write(str(i))
        self.tableWidget.setHorizontalHeaderLabels(metadata[1])

    def search(self):
        text, ok = QtGui.QInputDialog.getText(
            self, 'Search', 'Enter the primary key of the entry you are searching:')
        temp = []
        for registro in self.B_tree:
            aux = registro.split("|")
            if aux[0] == text:
                temp.append(registro)
        windo = search_table()
        if len(temp) != 0:
            windo.set_table(temp)
            windo.show()
            windo.exec_()
        else:
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Information)
            msg.setText("Theres no entry with that key")
            msg.setWindowTitle("Exit")
            retval = msg.exec_()
    def mod_entry(self):
        text, ok = QtGui.QInputDialog.getText(
            self, 'Search', 'Enter the primary key of the entry you are searching:')
        temp = []
        for registro in self.B_tree:
            aux = registro.split("|")
            if aux[0] == text:
                temp.append(registro)
        windo = search_table()
        if len(temp) != 0:
            windo.set_table(temp)
            windo.show()
            if windo.exec_():
                selected = windo.selected(temp)
                
    def remove_entry(self):
        text, ok = QtGui.QInputDialog.getText(
            self, 'Search', 'Enter the primary key of the entry you are searching:')
        temp = []
        for registro in self.B_tree:
            aux = registro.split("|")
            if aux[0] == text:
                temp.append(registro)
        tabla = search_table()
        tabla.set_table(temp)
        tabla.show()
        text = ""
        if tabla.exec_():
            lista = tabla.selected(self.lista_tipos)
        for i in range(len(lista)):
            if i == len(lista)-1:
                text += lista[i]+"\n"
            else:
                text += lista[i]+"|"
        line = 1
        with open(self.direccion, "r+") as file:
            aux = ""
            file.readline()
            file.readline()
            file.readline()
            print(line)
            for value in self.B_tree:
                if file.readline() != text:
                    line += 1
                else:
                    break
            print(line)
            file.seek(0)
            for i in range(3):
                aux = file.readline()
            auxn, auxend = aux.split('&')[0], aux.split('&')[1]

            file.seek(0)
            for j in range(line+3):
                text = file.readline()
            file.seek(-len(text), 1)
            file.write("*"+str(int(auxend))+"&")

            file.seek(0)
            aux = ""
            for i in range(3):
                aux = file.readline()
            auxint = int(auxn)
            par = '%' + str(10) + 'd'
            total = int(auxint)-1
            new_size = (par % total)
            end = (par % line)
            file.seek(-22, 1)
            file.write(new_size+"&"+end)

    def __init__(self):
        self.avail_list = []
        QtGui.QMainWindow.__init__(self)
        uic.loadUi("Main.ui", self)
        self.bOpenFile.clicked.connect(partial(self.open_File, self))
        self.bOpenFile.clicked.connect(self.indexando)
        self.bNewEntry.clicked.connect(partial(self.new_entry))
        self.bExportXml.clicked.connect(partial(self.exportxml, self))
        self.bExportExcel.clicked.connect(partial(self.exportxlsx, self))
        self.bNewFile.clicked.connect(
            partial(self.new_file, self))
        self.Previous_button.clicked.connect(partial(self.previous_batch))
        self.Next_button.clicked.connect(partial(self.next_batch))
        self.bMergeFiles.clicked.connect(self.merge_files)
        self.bSave.clicked.connect(self.save)
        self.bModifyField.clicked.connect(partial(self.mod_campos))
        self.bRemoveField.clicked.connect(partial(self.del_campos))
        self.bExit.clicked.connect(self.esci)
        self.bReIndexBtree.clicked.connect(self.reindexar)
        self.bSearch.clicked.connect(self.search)
        self.bRemoveEntry.clicked.connect(self.remove_entry)
        self.bOpenFile.clicked.connect(self.getAvailList)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    windo = Ui_MainWindow()
    windo.show()
    sys.exit(app.exec_())
