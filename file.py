import sys
from Btree import BTree


class File(object):
    

    def __init__(self, ruta1=None, ruta2=None):
        self.ruta1= ruta1
        self.ruta2=ruta2

    def write_tree(self, BTree):
        B_tree = BTree
        sys.stdout=open("Index_Tree.txt","w+")
        print (B_tree)

    def imprimir(self):
        print "ASABER PERRO"

    def getTypeF1(self):
        #print self.ruta1
        #print self.ruta2

        file = open(self.ruta1, "r+")
        tipos= file.readline()
        tipos = tipos.replace("[","")
        tipos = tipos.replace("]","")
        tipos = tipos.replace("'","")
        tipos = tipos.split(",")

        return tipos
        file.close()

    def getTypeF2(self):
        #print self.ruta1
        #print self.ruta2

        file = open(self.ruta2, "r+")
        tipos= file.readline()
        tipos = tipos.replace("[","")
        tipos = tipos.replace("]","")
        tipos = tipos.replace("'","")
        tipos = tipos.split(",")

        return tipos
        file.close()

    def getCeldasF1(self):
        #print self.ruta1
        #print self.ruta2

        file = open(self.ruta1, "r+")
        campos = file.readline()
        campos= file.readline()
        campos = campos.replace("[","")
        campos = campos.replace("]","")
        campos = campos.replace("'","")
        campos = campos.replace("\n","")
        campos = campos.split(",")

        return campos
        file.close()

    def getCeldasF2(self):
        #print self.ruta1
        #print self.ruta2

        file = open(self.ruta1, "r+")
        campos= file.readline()
        campos = file.readline()
        campos = campos.replace("[","")
        campos = campos.replace("]","")
        campos = campos.replace("'","")
        campos = campos.split(",")

        return campos
        file.close()

        
