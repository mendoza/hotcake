from PyQt4 import QtCore, QtGui
from Numfields import Numfields
class toolkit(object):
    @staticmethod
    def new_file(window):
        name = QtGui.QFileDialog.getSaveFileName(window, 'New File')
        if not name.endsWith('.qls'):
            name += '.qls'
        file = open(name, 'w')
        file.writelines(['[]\n'])
        Dialog = QtGui.QDialog()
        ui = Numfields()
        ui.setupUi(Dialog)
        Dialog.show()
        if Dialog.exec_():
            das = ui.getNum()
        print(das)
        file.close()
        