import sys
from Btree import BTree


class File(object):
    
    def __init__(self):
        self.data = "No data"

    def write_tree(self, BTree):
        B_tree = BTree
        sys.stdout=open("Index_Tree.txt","w+")
        print (B_tree)

    def imprimir(self):
        print "ASABER PERRO"