import sys
from Btree import BTree
from dropdown import dropdown


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
        print("inicie  :v")
        with open("Index_Tree.txt", "w+") as f:
            f.write(str(B_tree))
        #print (B_tree)
        print("termine")

    def getRecords(self):
        lista_records = []

        with open(self.ruta1, "r+")as file: 
            lista_tipos = file.readline()
            lista_tipos = self.remove_chars(["[","]","'","\n"," "],lista_tipos)
            lista_tipos = lista_tipos.split(",")
            lista_nombres = file.readline()
            lista_nombres = self.remove_chars(["[","]","'","\n"," "],lista_nombres)
            lista_nombres = lista_nombres.split(",")
            cant = int(file.readline())
            windo = dropdown(lista_nombres)
            windo.show()
            if windo.exec_():
                valor = windo.reto()
            
            indice = int(lista_nombres.index(valor))
            aux = lista_nombres[0]
            lista_nombres[0]= lista_nombres[indice]
            lista_nombres[indice]= aux

            aux = lista_tipos[0]
            lista_tipos[0]= lista_tipos[indice]
            lista_tipos[indice]= aux
            for i in range(cant):
                cadena = file.readline()
                cadena = cadena.replace("\n","")
                cadena = cadena.split("|")
                aux = cadena[0]
                cadena[0]= cadena[indice]
                cadena[indice]= aux
                lista_records.append(cadena)
        return lista_records , [lista_tipos,lista_nombres,cant]

            
        
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
        print "FILE 1",cant
        return int(cant)

    def getCantFile2(self):
        file = open(self.ruta2, "r+")
        file.readline()
        file.readline()
        cant= file.readline()
        print "FILE 2",cant
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

        for k in range((self.cant)/2):
            temp=[]
        
        
            for i in range(len(self.indexList1)):
                
                cadena = file1.readline()
                cadena = cadena.split("|")
                temp.append(cadena[self.indexList1[i]]+"|")
        

            for i in range(len(self.indexList2)):
                
                cadena = file2.readline()
                cadena = cadena.split("|")
                if i==len(self.indexList2)-1:
                    temp.append(cadena[self.indexList2[i]])
                else:
                    temp.append(cadena[self.indexList2[i]]+"|")

                        
                
            lista_temp.append(str(temp))
        

        for i in range(len(lista_temp)):
            print lista_temp[i]+"\n"
        
        self.write_Entrys(lista_temp)

        file.close()
        file2.close()
        file.close() 

    def write_Entrys(self, registros):

        file = open("mergeFile.qls", "r+")

        file.readline()
        file.readline()
        file.readline()
        
        
        for i in range(len(registros)):
            cadena =  registros[i]
            cadena = self.remove_chars(["[", "]", "'", ","], cadena)
            file.write(str(cadena)+"\n")
        
    
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
