from typing import Optional, List
class Node:
    def __init__(self, key, value=None):
        self._parent = None 
        self._left = None   
        self._right = None   
        self.key = key      
        self.data = value   

    def get_left(self) -> 'Node':
        return self._left

    def set_left(self, node) -> None:
        self._left = node
        if node is not None:
            node.set_parent(self)

    def get_right(self) -> 'Node':
        return self._right

    def set_right(self, node) -> None:
        self._right = node
        if node is not None:
            node.set_parent(self)

    def get_parent(self) -> 'Node':
        return self._parent

    def set_parent(self, node) -> None:
        self._parent = node

    def __str__(self):
        return f"{self.key}"
    
    def insert(self, key, value)-> None:
        """Entrada: se le pasa desde la función Binary Tree una key y una value para insertar el nuevo Nodo. Esta función es recursiva.
        Mira si en el nodo en el que se encuentra, es mayor menor o igual que el su key y dependiendo de eso mira el hijo izquierdo o el derecho. Si no tiene el hijo correspondiente, se añade el Nodo ahí y sino se llama a la función de niuevo pero con ese hijo.
        No se devuelve nada"""
        key_usuario = self.key
        if key_usuario <= key:
            if self.get_right() is not None:
                self.get_right().insert(key,value)
            else:
                self.set_right(Node(key,value))
        else:
            if self.get_left() is not None:
                self.get_left().insert(key,value)
            else:
                self.set_left(Node(key,value))
    def show(self)-> None:
        """No tiene elementos de entrada y mira si tiene padre o no. Si tiene padre, guarda su key y sino guarda None. Si tiene nodo izquierdo o/y derecho, llama a la misma función con sus o su hijos.
         No devuelve nada """
        key = self.key
        value = self.data
        if self.get_parent() is not None:
            parent = self.get_parent().key
        else:
            parent = None
        print(f'Nodo: ({key} , {value}) | Padre: {parent}')
        if self.get_left() is not None:
            self.get_left().show()
        if self.get_right() is not None:
            self.get_right().show()
    def height(self) -> int:
        """No recibe nada.
        Mira si tiene hijo derecho e izquierdo y calcula sus alturas y sino su valor será -1 y coge el máximo de los dos y le suma 1. 
        Devuelve la altura del árbol."""
        if self.get_right() is not None:
            der = self.get_right().height()
        else:
            der = -1
        if self.get_left() is not None:
            izq = self.get_left().height()
        else:
            izq = -1
        return 1 + max(izq, der)
    def find_node(self, key)-> tuple[int,int]:
        """Recibe la función la clave que estamos buscando y la comparamos con la del self: si es igual returneamos una tupla, si es mayor vemos si tiene hijo derecha, si tiene llamamos a esta misma función con el hijo derecho y si no tiene returneamos None. Si es menor igual pero con el izqueirdo.
        Devolvemos una tupla con key y data"""
        if self.key == key:
            return (self.key, self.data)
        if self.key > key:
            if self.get_left() is not None:
                return self.get_left().find_node(key)
        else:
            if self.get_right() is not None:
                return self.get_right().find_node(key)
        return None
    def skew(self) -> bool:
        """
        Función recursiva que comprueba si el nodo actual o alguno de sus descendientes está desbalanceado (inclinado). 
        Calcula la altura de sus hijos asumiendo que un hijo vacío (None) tiene altura -1.  Si la diferencia absoluta de alturas es mayor que 1, devuelve True.  Si no, llama a la función skew() de sus hijos para comprobar el resto del subárbol.
        Devuelve un booleano: True si encuentra algún desbalanceo, False si todo está balanceado.
        """
        h_izq = self.get_left().height() if self.get_left() is not None else -1
        h_der = self.get_right().height() if self.get_right() is not None else -1
        
        diferencia = abs(h_izq - h_der)
        if diferencia > 1:
            return True
        if self.get_left() is not None:
            skew_izq = self.get_left().skew()
        else:
            skew_izq= False
        if self.get_right() is not None:
            skew_der = self.get_right().skew() 
        else:
            skew_der = False
        
        return skew_izq or skew_der
    def count_nodes_tree(self)-> int:
        """Función auxiliar que no recibe nada y ve si tiene el nodo actual hijos y si es así calcula el número de nodos de sus hijos y returnea 1 + n de nodos derecha + n de nodos izquierda."""
        if self.get_left() is not None:
            izq = self.get_left().count_nodes_tree()
        else:
            izq = 0
        if self.get_right() is not None:
            der = self.get_right().count_nodes_tree()
        else:
            der = 0
        return 1 + izq + der
    def count_leafs(self) ->int:
        """Función auxiliar devuelve el número de hojas que tiene el árbol. Mira si tiene hijo derecho e izquierdo. Si no tiene ninguno devuelve 1 y sino llama a está misma función pero del hijo derecho e izquierdo si existen y luego devuelve la suma de ellos."""
        if self.get_right() is None and self.get_left() is None:
            return 1
        if self.get_left() is not None:
            izq = self.get_left().count_leafs()
        else:
            izq = 0
        if self.get_right() is not None:
            der = self.get_right().count_leafs()
        else:
            der = 0
        return izq + der  
    def longest_path(self) ->list:
        """Función auxiliar que devuelve la lista de palabras del camino más largo desde el último hijo hasta la raíz."""
        if self.get_left() is None and self.get_right() is None:
            return [self.key]
        else:
            if self.get_left() is not None:
                izq = self.get_left().longest_path()
            else:
                izq = []
            if self.get_right() is not None:
                der = self.get_right().longest_path()
            else:
                der = []
            if len(der) > len(izq):
                der.append(self.key)
                return der
            else:
                izq.append(self.key)
                return izq
            
class BinaryTree:
    def __init__(self, root: Node):
        self.root = root
    def insert(self, key, value=None) -> None:
        """Entrada: key y value del Nodo que debemos insertar nuevo.
        Función: Mira si existe o no el self.root. Si existe, manda a la función del nodo insert con entrada key y value y si no existe, añade este nuevo Nodo como self.root.
        No devuelve nada"""
        if self.root is None:
            self.root = Node(key,value)
        else:
            self.root.insert(key,value)

    def show(self)-> None:
        """Función que no recibe nada y ve si existe la raíz del árbol o no. Si no existe, printea que el árbol está vacio y sino llama a una función de la raíz."""
        if self.root is None:
            print("Árbol vacio")
        else:
            self.root.show()
    def height(self)-> int:
        """No recibe ningún elemento. Mira si tiene o no raiz y devuelve la altura del árbol(tipo int)."""
        if self.root is None:
            return -1
        else:
            return self.root.height()
    def find_node(self, key)->tuple[int,int]:
        """Recibe la clave a buscar y mira si tiene raiz o no el árbol. Si no tiene devuelve directamente None y sino llama a una función del nodo de la raíz."""
        if self.root is None:
            return None
        else:
            return self.root.find_node(key)
        
    def _find_node_obj(self, node: 'Node', key) -> 'Node':
        """Función auxiliar que recibe un Nodo y la clave que buscamos y que busca y devuelve el objeto Node exacto. """
        if node is None:
            return None
        if node.key == key:
            return node
        if node.key > key:
            return self._find_node_obj(node.get_left(), key)
        else:
            return self._find_node_obj(node.get_right(), key)

    def tree_minimum(self, v: 'Node') -> 'Node':
        """Busca el nodo más a la izquierda (el menor) a partir del nodo v."""
        current = v
        while current.get_left() is not None:
            current = current.get_left()
        return current
    def transplant(self, u: 'Node', v: 'Node') -> None:
        """Reemplaza el subárbol de 'u' por el subárbol de 'v'."""
        padre_u = u.get_parent()
        if padre_u is None:
            self.root = v
            if v is not None:
                v.set_parent(None)
        elif u == padre_u.get_left():
            padre_u.set_left(v)
        else:
            padre_u.set_right(v)

    def delete(self, key: int) -> bool:
        """Elimina un nodo por su clave. Retorna True si lo borra, False si no existe."""
        nodo_borrar = self._find_node_obj(self.root, key)
        
        if nodo_borrar is None:
            print("Nodo no encontrado")
            return False

        if nodo_borrar.get_left() is None:
            self.transplant(nodo_borrar, nodo_borrar.get_right())
            
        elif nodo_borrar.get_right() is None:
            self.transplant(nodo_borrar, nodo_borrar.get_left())

        else:
            y = self.tree_minimum(nodo_borrar.get_right())
            if y.get_parent() != nodo_borrar:
                self.transplant(y, y.get_right())
                y.set_right(nodo_borrar.get_right())
                
            self.transplant(nodo_borrar, y)
            y.set_left(nodo_borrar.get_left())
            
        return True


        
        
    def skew(self) ->bool:
        """Esta función va a mirar si tiene raiz o no el árbol. Si tiene va a llamar a la función skew del nodo y sino devolvera False."""
        if self.root is None:
            return False
        else:
            return self.root.skew()
    def count_nodes_tree(self) ->int:
        """Función que no recibe nada y va a contar el número de raices que hay en el árbol, para ello va a haber si hay o no raiz, si hay llama a una función auxiliar del nodo, y si no hay, devueve 0."""
        if self.root is None:
            return 0
        else:
            return self.root.count_nodes_tree()
    def count_leafs(self) ->int:
        """Función que comprueba si el árbol está vacio o no y si está devuelve 0 y sino devuelve llamando a una función auxiliar dentro de la clase de node."""
        if self.root is None:
            return 0
        else:
            return self.root.count_leafs()
    def longest_path(self) ->list:
        if self.root is None:
            return []
        else:
            return self.root.longest_path()
    def paths_to_leaf_with_length(self, node: Optional["Node"], remaining_edges: int, current_path: Optional[List[str]] = None, results: Optional[List[List[str]]] = None) -> List[List[str]]:
        """ Devuelve todos los caminos raiz->hoja con longitud exacta (en aristas) igual a remaining_edges al comienzo de la llamada. """
        if current_path is None:
            current_path = []
        if results is None:
            results = []
            

        if node is None:
            return results
        current_path.append(str(node.key))
        
        if node.get_left() is None and node.get_right() is None:
            if remaining_edges == 0:
                results.append(list(current_path))
        else:
            self.paths_to_leaf_with_length(node.get_left(), remaining_edges - 1, current_path, results)
            self.paths_to_leaf_with_length(node.get_right(), remaining_edges - 1, current_path, results)
        current_path.pop()
        
        return results
def in_order_nodo (node: Node)-> None:
    """Función auxiliar recursiva que recoge un nodo, llama a su misma función para el nodo izquierda, imprime la clave del nodo actual y vuelve a llamar a la función para el nodo derecho. No devuelve nada"""
    if node is not None:
        in_order_nodo(node.get_left())
        print(node.key)
        in_order_nodo(node.get_right())

def in_order(tree: BinaryTree) ->None:
    """Función que recibe un árbol, saca su raíz guaradandolo en current y llama a una función auxiliar con current. No devuelve nada"""
    current = tree.root
    in_order_nodo(current)
    
def pre_order_nodo (node: Node)-> None:
    """Función auxiliar recursiva que recoge un nodo, imprime la clave del nodo actual, llama a su misma función para el nodo izquierda y vuelve a llamar a la función para el nodo derecho. No devuelve nada"""
    if node is not None:
        print(node.key)
        pre_order_nodo(node.get_left())
        pre_order_nodo(node.get_right())

def pre_order(tree: BinaryTree) ->None:
    """Función que recibe un árbol, saca su raíz guaradandolo en current y llama a una función auxiliar con current. No devuelve nada"""
    current = tree.root
    pre_order_nodo(current)

def post_order_nodo (node: Node)-> None:
    """Función auxiliar recursiva que recoge un nodo, llama a su misma función para el nodo izquierda, vuelve a llamar a la función para el nodo derecho y imprime la clave del nodo actual. No devuelve nada"""
    if node is not None:
        post_order_nodo(node.get_left())
        post_order_nodo(node.get_right())
        print(node.key)
def post_order(tree: BinaryTree) ->None:
    """Función que recibe un árbol, saca su raíz guaradandolo en current y llama a una función auxiliar con current. No devuelve nada"""
    current = tree.root
    post_order_nodo(current)

def level_order(tree: BinaryTree) ->None:
    cola = []
    if tree.root is not None:
        cola.append(tree.root)
    while len(cola)> 0:
        nodo_actual = cola.pop(0)
        print(nodo_actual.key)
        if nodo_actual.get_left() is not None:
            cola.append(nodo_actual.get_left())
        if nodo_actual.get_right() is not None:
            cola.append(nodo_actual.get_right())

if __name__ == "__main__":
    # --- CONSTRUCCIÓN DEL ÁRBOL DE PRUEBA ---
    root_example = Node(10)
    lc = Node(5)
    rc = Node(12)
    lc.set_parent(root_example)
    rc.set_parent(root_example)
    root_example.set_left(lc)
    root_example.set_right(rc)

    llc = Node(3)
    lrc = Node(6)
    lc.set_left(llc)
    lc.set_right(lrc)

    rrc = Node(16)
    rc.set_right(rrc)

    tree = BinaryTree(root_example)
    
    print("\n==================================================")
    print("        PRUEBAS DE ÁRBOLES BINARIOS")
    print("==================================================")

    print("\n--- TEST 1: Inserción y Borrado ---")
    print("Operación: Insertar 25 y eliminar 5.")
    tree.insert(25)
    tree.delete(5)
    
    print("\n[SALIDA ESPERADA - Estructura tras borrar 5 e insertar 25]")
    print("Nodo: (10 , None) | Padre: None")
    print("Nodo: (6 , None) | Padre: 10")
    print("Nodo: (3 , None) | Padre: 6")
    print("Nodo: (12 , None) | Padre: 10")
    print("Nodo: (16 , None) | Padre: 12")
    print("Nodo: (25 , None) | Padre: 16")
    
    print("\n[SALIDA OBTENIDA]")
    tree.show()


    print("\n--- TEST 2: Conteo de Nodos ---")
    print(f"[SALIDA ESPERADA] Hojas totales: 2 | Nodos totales: 6")
    print(f"[SALIDA OBTENIDA] Hojas totales: {tree.count_leafs()} | Nodos totales: {tree.count_nodes_tree()}")


    print("\n--- TEST 3: Altura y Búsqueda ---")
    print(f"[SALIDA ESPERADA] Altura: 3 | Buscar 16: (16, None) | Buscar 99: None")
    print(f"[SALIDA OBTENIDA] Altura: {tree.height()} | Buscar 16: {tree.find_node(16)} | Buscar 99: {tree.find_node(99)}")


    print("\n--- TEST 4: Skew (Inclinación) y Paths ---")
    print("[SALIDA ESPERADA] Skew: True (ya que la rama derecha es mucho más profunda)")
    print(f"[SALIDA OBTENIDA] Skew: {tree.skew()}")
    
    print("\n[SALIDA ESPERADA] Camino más largo: ['25', '16', '12', '10'] o similar (desde hoja a raíz)")
    print(f"[SALIDA OBTENIDA] Camino más largo: {tree.longest_path()}")
    
    print("\n[SALIDA ESPERADA] Caminos con 3 aristas (longitud 3): [['10', '12', '16', '25']]")
    caminos_exactos = tree.paths_to_leaf_with_length(tree.root, 3)
    print(f"[SALIDA OBTENIDA] Caminos con 3 aristas: {caminos_exactos}")


    print("\n--- TEST 5: Recorridos del Árbol ---")
    
    print("\n[In-Order]")
    print("Salida Esperada: 3 -> 6 -> 10 -> 12 -> 16 -> 25")
    print("Salida Obtendida:")
    in_order(tree)
    
    print("\n[Pre-Order]")
    print("Salida Esperada: 10 -> 6 -> 3 -> 12 -> 16 -> 25")
    print("Salida Obtendida:")
    pre_order(tree)
    
    print("\n[Post-Order]")
    print("Salida Esperada: 3 -> 6 -> 25 -> 16 -> 12 -> 10")
    print("Salida Obtendida:")
    post_order(tree)
    
    print("\n[Level-Order]")
    print("Salida Esperada: 10 -> 6 -> 12 -> 3 -> 16 -> 25")
    print("Salida Obtendida:")
    level_order(tree)
    print("\n==================================================")


