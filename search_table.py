from PyQt4 import QtCore, QtGui,uic

class search_table(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        uic.loadUi("search_table.ui",self)

    def remove_chars(self, lista, cadena):
        for char in lista:
            cadena = cadena.replace(char, "")
        return cadena

    def set_table(self,lista):
        self.tableWidget.setRowCount(0)
        self.tableWidget.setRowCount(len(lista))
        for i in range(len(lista)):
            temp = lista[i]
            temp = self.remove_chars(["\n", ""], temp)
            aux = temp.split("|")
            self.tableWidget.setColumnCount(len(aux))
            for j in range(self.tableWidget.columnCount()):
                self.tableWidget.setItem(i, j, QtGui.QTableWidgetItem(aux[j]))
        self.tableWidget.resizeColumnsToContents()



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dialog = search_table()
    dialog.show()
    sys.exit(app.exec_())
