import sys
from Btree import BTree


class File(object):

    def __init__(self, ruta1=None, ruta2=None):
        self.ruta1 = ruta1
        self.ruta2 = ruta2
        self.buffer = []
    def remove_chars(self, lista, cadena):
        for char in lista:
            cadena = cadena.replace(char, "")
        return cadena

    def buffer_add(self, cos):
        self.buffer.append(cos)
        print(self.buffer)
        if len(self.buffer) >= 5:
            print("entre")
            self.write_entry()

    def write_tree(self, BTree):
        B_tree = BTree
        sys.stdout = open("Index_Tree.txt", "w+")
        print (B_tree)

    def imprimir(self):
        print "ASABER PERRO"

    def getTypeF1(self):
        file = open(self.ruta1, "r+")
        tipos = file.readline()
        tipos = self.remove_chars(["[", "]", "'", "\n"], tipos)
        tipos = tipos.split(",")
        file.close()
        return tipos
    
    def getTypeF2(self):
        file = open(self.ruta2, "r+")
        tipos = file.readline()
        tipos = self.remove_chars(["[", "]", "'", "\n"], tipos)
        tipos = tipos.split(",")
        file.close()
        return tipos

    def getCeldasF1(self):
        file = open(self.ruta1, "r+")
        campos = file.readline()
        campos = file.readline()
        campos = self.remove_chars(["[", "]", "'", "\n"], campos)
        campos = campos.split(",")
        file.close()
        return campos

    def getCeldasF2(self):
        file = open(self.ruta2, "r+")
        campos = file.readline()
        campos = file.readline()
        campos = self.remove_chars(["[", "]", "'", "\n"], campos)
        campos = campos.split(",")
        file.close()
        return campos

    def getCantFile1(self):
        file = open(self.ruta1, "r+")
        file.readline()
        file.readline()
        cant= file.readline()
        #print "FILE 1",cant
        return int(cant)

    def getCantFile2(self):
        file = open(self.ruta2, "r+")
        file.readline()
        file.readline()
        cant= file.readline()
        #print "FILE 2",cant
        file.close()
        return int(cant)

    def createNewFile(self,tipos, campos, cantidad):
        self.tipos= tipos
        self.campos= campos
        self.cant= cantidad

        file = open("mergeFile.qls", "w+")
        file.write(str(self.tipos)+"\n")
        file.write(str(self.campos)+"\n")
        par = '%' + str(10) + 'd'
        new_size = (par % self.cant)
        file.write(str(new_size)+"\n")
        file.close()

    def write_in_newFile(self, indexList1, indexList2):
        self.indexList1 = indexList1
        self.indexList2= indexList2

        print "-------"
        print self.indexList1
        print self.indexList2
    
        file = open("mergeFile.qls", "r+")
        file.readline()
        file.readline()
        file.readline()
        file1 = open(self.ruta1, "r+")
        file2 = open(self.ruta2, "r+")
        
        file1.readline()
        file1.readline()
        file1.readline()

        file2.readline()
        file2.readline()
        file2.readline()

        lista_temp = []
        temp=[]

            
        
        for i in range(len(self.indexList1)):
            
            cadena = file1.readline()
            cadena = cadena.split("|")
            temp.append(cadena[self.indexList1[i]]+"|")
    

        for i in range(len(self.indexList2)):
            
            cadena = file2.readline()
            cadena = cadena.split("|")
            temp.append(cadena[self.indexList2[i]]+"|")
            
        lista_temp.append(str(temp))
        print lista_temp
        

        file.close()
        file2.close()
        file.close() 

    
    def write_entry(self):
        print(self.buffer)
        for registro in self.buffer:
            with open(self.ruta1, "a+") as file:
                cadena = ""
                for i in range(len(registro)):
                    if i == len(registro)-1:
                        cadena += str(registro[i])+"\n"
                    else:
                        cadena += str(registro[i])+"|"
                file.write(cadena)
        with open(self.ruta1, "r+") as file:
            aux = ""
            for i in range(3):
                aux = file.readline()
            aux = int(aux)
            par = '%' + str(10) + 'd'
            total = int(aux)+len(self.buffer)
            new_size = (par % total)
            file.seek(-11, 1)
            file.write(new_size)
        self.buffer = []
