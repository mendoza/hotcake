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
        print ""
    
    #Metodo File1 consigue , tipos de datos y campos que contiene el primer archivo seleccionado
    def File1(self):
        #ruta1: Es nuestra variable que nos ayuda a capturar la ruta del primer archivo
        self.ruta1=str(QtGui.QFileDialog.getOpenFileName(self, 'Open File1'))
        #creamos una instancia de file
        FILE = File(self.ruta1 ,None)
        #tiposFile1: como su nombre lo dice nos consigue los tipos de dato que contiene el archivo seleccionado
        self.tiposFile1= FILE.getTypeF1()
        #campos.File1: guarda los campos que contiene el archivo seleccionado
        self.camposFile1= FILE.getCeldasF1()
        #agregamos al combobox los campos disponibles de nuestro file1
        self.combo1.addItems(self.camposFile1)
        #desactivamos el boton para seleccionar archivo para evitar colisiones
        self.select_file_1.setEnabled(False)
        #Esta accion nos ayuda a capturar el valor selecionado despues de activar el combobox mediante presionar el mismo
        self.combo1.activated.connect(self.fillList1)

    #Este metodo al igual que el File1 , nos ayuda a capturar datos , pero del segundo archivo seleccionado
    def File2(self):
        #ruta2: nos guarda la ruta del archvio
        self.ruta2= str(QtGui.QFileDialog.getOpenFileName(self, 'Open File2'))
        #Nuevamente creamos una instancia de FILE 
        FILE = File(None,self.ruta2)
        #capturamos los tipos que contiene el file2 y los guardamos en tiposFile2
        self.tiposFile2= FILE.getTypeF2()
        #capturamos los campos que contiene el file2 y los guardamos camposFile2
        self.camposFile2= FILE.getCeldasF2()
        #En el segundo combo box le agregamos los campos encontrados en el File2
        self.combo2.addItems(self.camposFile2)
        #En este caso desactivamos el otro boton para seleccionar archivo y asi evitamos colisiones
        self.select_file_2.setEnabled(False)
        #Esta accion nos ayuda a capturar el valor selecionado despues de activar el combobox mediante presionar el mismo
        self.combo2.activated.connect(self.fillList2)

    #Este metodo nos ayuda a tomar el valor seleccionado del combo box que contiene los datos del file1
    def fillList1(self):
        #text: contiene el valor capturado despues de hacer click
        text = self.combo1.currentText()
        #le agregamos a nuestra lista que corresponde al metadata del nuevo archivo a crear ,el valor seleccionado
        self.lista1.addItems([text])
        #le agregamos a nuestra lista que corresponde al metadata del nuevo archivo a crear ,el campo seleccionado
        self.campos_lista1.append(str(text))
        #indice : contiene el numero de indice del tipo de dato que selecciono
        indice = self.combo1.currentIndex()
        #agregamos los indices seleccionados a nuestra lista de indices para el tercer archivo
        self.indices_lista1.append(indice)

    #Este metodo nos ayuda a tomar el valor seleccionado del combo box que contiene los datos del file2
    def fillList2(self):
        #text: contiene el valor capturado despues de hacer click
        text = self.combo2.currentText()
        #le agregamos a nuestra lista que corresponde al metadata del nuevo archivo a crear ,el valor seleccionado
        self.lista2.addItems([text])
        #le agregamos a nuestra lista que corresponde al metadata del nuevo archivo a crear ,el campo seleccionado
        self.campos_lista2.append(str(text))
        #indice : contiene el numero de indice del tipo de dato que selecciono
        indice = self.combo2.currentIndex()
        #agregamos los indices seleccionados a nuestra lista de indices para el tercer archivo
        self.indices_lista2.append(indice)

    #Nuestro metodo make es quien realiza el proceso para hacer las llamadas y escribir el tercer archivo
    def make(self):
        #Desactivamos el boton de MAKE para evitar colisiones
        self.fusion.setEnabled(False)
        #NewFileCampos:  contiene los campos que seran usados en el tercer archivo
        self.NewFileCampos=self.campos_lista1
        #Se le agregan los datos del segundo archivo seleccionado
        self.NewFileCampos+=self.campos_lista2
        #Este for recorre la lista de tipos que contiene el file1 , y por medio de una comparacion encuentra los proximos a usar
        #en el tercer archivo 
        for i in range(len(self.indices_lista1)):
            self.NewFileTipos.append(self.tiposFile1[self.indices_lista1[i]])
        #Este for recorre la lista de tipos que contiene el file2 , y por medio de una comparacion encuentra los proximos a usar
        #en el tercer archivo
        for i in range(len(self.indices_lista2)):
            self.NewFileTipos.append(self.tiposFile2[self.indices_lista2[i]])

        #creamos una instancia de FILe donde le mandamos las dos rutas para trabajar con sus registros
        FILE = File(self.ruta1, self.ruta2)
        #cantFile1: la cantidad de datos del file1
        cantFile1 = int
        #cantFile2: la cantidad de datos del file2
        cantFile2 = int
        #arriba fueron declarados como int
        #a continuacion se les asigna los datos capturados de file1 y file2
        cantFile1= FILE.getCantFile1()
        cantFile2= FILE.getCantFile2()

        #Si la cantidad de datos que contiene es la misma :
        if cantFile1 == cantFile2:
            #por medio de la instancia file, llamamos a crearNewFile, este escribe en el tercer archivo la metadata
            FILE.createNewFile(self.NewFileTipos, self.NewFileCampos, cantFile1)
            #esta siguiente llamada escribe los campos seleccionados de los dos archivos
            FILE.write_in_newFile(self.indices_lista1, self.indices_lista2)
            #Este codigo es usado para mostrar un aviso a nuestro usuario
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Information)
            msg.setText("MERGE REALIZADO CON EXITO!")
            msg.setWindowTitle("Merge Files")
            retval = msg.exec_()
        else:
            #Si nuestros archivos no comparten la misma cantidad de datos le decimos al usuario que no puede realizarse la accion
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Information)
            msg.setText("NO PUEDE FUSIONAR ARCHIVOS DE TAMANOS DIFERENTES!")
            msg.setWindowTitle("Merge Files")
            retval = msg.exec_()            
            
    def __init__ (self):
        """--------------------------------------------------
        ruta1: contiene la ruta del primer archivo
        ruta2: contiene la ruta del segundo archivo
        NewFileCampos: contiene los campos que van en el tercer archivo
        NewFileTipos: contiene los tipos que van en el tercer archivo
        indices_lista1: contiene los indices de los tipos seleccionados del file1
        indices_lista2: contiene los indices de los tipos seleccionados del file2
        campos_lista1: contiene los campos seleccionados del file1
        campòs:lista2: contiene los campos seleccionados del file2
        tiposFile1: contiene los tipos pertinentes seleccionados del file1
        tiposFile2: contiene los tipos pertinentes seleccionados del file2
        -------------------------------------------------------"""
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
        #Llamadas de los botones
        self.select_file_1.clicked.connect(self.File1)
        self.select_file_2.clicked.connect(self.File2)
        self.fusion.clicked.connect(self.make)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dialog = Ui_Dialog()
    dialog.show()
    sys.exit(app.exec_())

