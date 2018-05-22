from PyQt4 import QtCore, QtGui

def new_file(window):
    name = QtGui.QFileDialog.getSaveFileName(window, 'New File')
    if not name.endsWith('.qls'):
        name += '.qls'
    file = open(name, 'w')
    file.writelines(['[]\n'])
    
    file.close()


        