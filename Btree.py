from Node import Node
import bisect
import itertools
import operator

class BTree(object):
    BRANCH = LEAF = Node

    """
    Orden: como su palabra lo dice, el orden en el que basamos el arbol


    """
    def __init__(self, order):
        self.order = order
        self._root = self._bottom = self.LEAF(self)

    #Metodo que nos ayuda a llegar hasta un item en especifico , como la root con sus keys 
    def _path_to(self, item):
        current = self._root
        llaves = []

        #Este getattr nos consigue que es nuestro atributo si es leaf, children etc
        while getattr(current, "children", None):
            index = bisect.bisect_left(current.contents, item)
            #Realizamos un append a las llavez 
            llaves.append((current, index))
            #tomamos el length para comparar si cumple con la propiedad
            if index < len(current.contents) \
                    and current.contents[index] == item:
                return llaves
            current = current.children[index]

        index = bisect.bisect_left(current.contents, item)
        llaves.append((current, index))
        present = index < len(current.contents)
        present = present and current.contents[index] == item
        
        #Hacemos un return de las llavez una vez verificado que cumple las propiedad
        return llaves

    #recibe data , y una lista 
    def _present(self, item, ancestors):
        last, index = ancestors[-1]
        return index < len(last.contents) and last.contents[index] == item

    #Realizamos el insert a nuestro arbol
    def insert(self, item):
        # assignamos a current el root para revisar si podemos insertarlo ahi
        current = self._root
        #usamos la lista que trae y la mandamos a nuestro metodo a ordenarlo
        ancestors = self._path_to(item)
        node, index = ancestors[-1]
        #Revisamos si es un hijo
        while getattr(node, "children", None):
            #al nodo sub la lista de sus hijos , dependiendo su condicion le hacemos split
            node = node.children[index]
            #como lo muestra el metodo hay un bisect que biseca la lista
            index = bisect.bisect_left(node.contents, item)
            #a la lista que traemos la hacemos un apend en el nodo , del data 
            ancestors.append((node, index))
        node, index = ancestors.pop()
        #finalmente hacemos el incert , mandando como parametro, indice, el data a aguardar y la litsa
        node.insert(index, item, ancestors)

    #Aqui realizamos nuestra funcion remove que recibe un dato como es logico
    def remove(self, item):
        #le asignamos nuevamente a curret la root principal
        current = self._root
        #recorremos la lista haciendo la llamada del meto
        ancestors = self._path_to(item)

        #Revisamos si existe ene nuestra lista 
        if self._present(item, ancestors):
            #si es asi realizamos el pop de la lista ancestros
            node, index = ancestors.pop()
            #hace el remove correspondiente
            node.remove(index, ancestors)
        else:  
            #En caso de no esncontrarlo , de muestra un mensaje que dice que no encontro lo que deseaba eliminar
            raise ValueError("%r not in %s" % (item, self.__class__.__name__))

    #Nuestro metodo simplemente revisa si el item que recibe como parametro, esta contemplado en el arbol
    def __contains__(self, item):
        return self._present(item, self._path_to(item))

    #Esta funcion es la que itera entre nuestras llavez y es nuestra recursiva
    def __iter__(self): 
        #Recibe un nodo como parametro
        def _recurse(node):
            #Chequea si es hijo 
            if node.children:
                #En caso de serlo , llama al item encontrado
                for child, item in zip(node.children, node.contents):
                    for child_item in _recurse(child):
                        yield child_item
                    yield item
                for child_item in _recurse(node.children[-1]):
                    yield child_item
            else:
                #Si no lo encuentra :
                for item in node.contents:
                    yield item

        for item in _recurse(self._root):
            yield item

    #Nuestro metodo realiza las operaciones llamando si es necesario a la recursiva
    def __repr__(self):
        def recurse(node, accum, depth):
            accum.append(("  " * depth) + repr(node))
            for node in getattr(node, "children", []):
                recurse(node, accum, depth + 1)

        accum = []
        recurse(self._root, accum, 0)
        return "\n".join(accum)
        
    #Sobrecarga de metodos propios del lenguaje
    #Realiza la carga al arbol
    @classmethod
    def bulkload(cls, items, order):
        tree = object.__new__(cls)
        tree.order = order

        #llama al meotod paara las hojas que es diferente al de las hijas o branches
        leaves = tree._build_bulkloaded_leaves(items)
        tree._build_bulkloaded_branches(leaves)

        return tree

    #A diferencia del metodo anterior este es llamado solo si es en una hoja el trabajo
    def _build_bulkloaded_leaves(self, items):
        #Definimos cual es nuestro orden minimo 
        minimum = self.order // 2
        leaves, seps = [[]], []

        #hace la validacion para saber si es posible que pueda realizar el trabajo , debe ser menor al orden-1
        for item in items:
            if len(leaves[-1]) < self.order:
                leaves[-1].append(item)
            else:
                seps.append(item)
                leaves.append([])
        
        #Revisa la segunda condicion que le dice cual es el orden minimo, la propiedad 
        if len(leaves[-1]) < minimum and seps:
            last_two = leaves[-2] + [seps.pop()] + leaves[-1]
            leaves[-2] = last_two[:minimum]
            leaves[-1] = last_two[minimum + 1:]
            seps.append(last_two[minimum])

        #Una vez ya con las validaciones pertinentes realiza el return 
        return [self.LEAF(self, contents=node) for node in leaves], seps

    #Este metodo a diferencia del anterior es para nodos NO hojas y por lo tanto tendra contempladas llamadas recuersivas
    def _build_bulkloaded_branches(self, (leaves, seps)):
        #De igual manera definimos cual es el orden minimo
        minimum = self.order // 2
        #aqui guardamos cuantos niveles va sumando nuestro arbol
        levels = [leaves]

        while len(seps) > self.order + 1:
            items, nodes, seps = seps, [[]], []
            #Es el mismo proceso de las hojas , eso si identifica que son hojas 
            for item in items:
                if len(nodes[-1]) < self.order:
                    nodes[-1].append(item)
                else:
                    seps.append(item)
                    nodes.append([])
            #Tambien hace la validacion normal , las de las propiedades que debes estar siempre contempladas
            if len(nodes[-1]) < minimum and seps:
                last_two = nodes[-2] + [seps.pop()] + nodes[-1]
                nodes[-2] = last_two[:minimum]
                nodes[-1] = last_two[minimum + 1:]
                seps.append(last_two[minimum])

            """
            offset: es donde va siendo recorrido nuestro arbol, nos da una posicion dentro de el
            """
            offset = 0
            #Enumera los nodos y va recorriendo lo que es el arbol para darle un valor
            for i, node in enumerate(nodes):
                children = levels[-1][offset:offset + len(node) + 1]
                nodes[i] = self.BRANCH(self, contents=node, children=children)
                offset += len(node) + 1

            levels.append(nodes)
        #por ultimo revisa el nodo NO hoja y manda sus hijos y sus niveles contemplados como parametros
        self._root = self.BRANCH(self, contents=seps, children=levels[-1])
