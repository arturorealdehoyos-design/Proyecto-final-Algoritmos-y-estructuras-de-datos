import sys
import random
import time
from enum import Enum
class Color(Enum):
    RED = 0
    BLACK = 1

class RBNode:
    def __init__(self, key, value=None, color=Color.RED):
        self._parent = None
        self._left = None
        self._right = None
        self.key = key
        self.data = value
        self.color = color

    def set_black(self):
        self.color = Color.BLACK

    def set_red(self):
        self.color = Color.RED
        
    def set_left(self, node):
        self._left = node
        
    def set_right(self, node):
        self._right = node

    def is_red ( self ) -> bool :
        if self.color == Color.RED:
            return True
        return False
    
    def is_black ( self ) -> bool :
        if self.color == Color.BLACK:
            return True
        return False
    
    def get_left ( self ) -> None :
        return self._left
    
    def get_right ( self ) -> None :
        return self._right
    
    def get_parent ( self ) -> None :
        return self._parent
    
class RedBlackTree:
    def __init__(self, root: RBNode = None):
        self.NIL = RBNode(0)
        self.NIL.set_black()
        self.NIL.set_left(None)
        self.NIL.set_right(None)
        self.root = self.NIL
        
        if root is not None:
            self.insert(root.key, root.data)
    
    def left_rotate(self, x: RBNode) -> None:
        """Rota el árbol hacia la izquierda sobre el nodo x."""
        y = x._right
        x._right = y._left
        
        if y._left != self.NIL:
            y._left._parent = x
            
        y._parent = x._parent
        
        if x._parent == self.NIL:
            self.root = y
        elif x == x._parent._left:
            x._parent._left = y
        else:
            x._parent._right = y
            
        y._left = x
        x._parent = y

    def right_rotate(self, y: RBNode) -> None:
        """Rota el árbol hacia la derecha sobre el nodo y."""
        x = y._left
        y._left = x._right
        
        if x._right != self.NIL:
            x._right._parent = y
            
        x._parent = y._parent
        
        if y._parent == self.NIL:
            self.root = x
        elif y == y._parent._right:
            y._parent._right = x
        else:
            y._parent._left = x
            
        x._right = y
        y._parent = x
    def insert_fix_up (self, z: RBNode)-> None:
        """Función que recibe el nodo desde el cual hay que arreglar el árbol y va arreglando el árbol hasta que el color del padre de z sea negro o llegar a la raíz. Pone finalmente la raíz en negroi ya que es una norma de los árboles negros y rojos. 
        No devuelve nada."""
        while z._parent != self.NIL and z._parent.color == Color.RED:
            y = z._parent
            if z._parent._parent._right == y:
                if z._parent._parent._left.color == Color.RED:
                    z._parent.color = Color.BLACK
                    z._parent._parent._left.color = Color.BLACK
                    z._parent._parent.color = Color.RED
                    z = z._parent._parent
                else:
                    if z._parent._left == z:
                        z = z._parent
                        self.right_rotate(z)
                    z._parent.color = Color.BLACK
                    z._parent._parent.color = Color.RED
                    self.left_rotate(z._parent._parent)
            else: 
                if z._parent._parent._right.color == Color.RED:
                    z._parent.color = Color.BLACK
                    z._parent._parent._right.color = Color.BLACK
                    z._parent._parent.color = Color.RED
                    z = z._parent._parent
                else:
                    if z._parent._right == z:
                        z = z._parent
                        self.left_rotate(z)
                    z._parent.color = Color.BLACK
                    z._parent._parent.color = Color.RED
                    self.right_rotate(z._parent._parent)
        self.root.color = Color.BLACK
    
    def insert_RB (self, key: int):
        """Recibe una clave que debe insertar. Si el árbol está vacio, nombra como raíz el nodo formado por la clave dada y sino va recorriendo el árbol para luego insertarlo en la correcta posición. 
        LLama finalmente a la función fixed up para que arregle el desajuste de los colores. No devuelve nada."""
        nodo = RBNode(key)
        nodo.color = Color.RED
        nodo._left = self.NIL
        nodo._right = self.NIL
        nodo._parent = self.NIL
        if self.root == self.NIL:
            self.root = nodo
            self.root.color = Color.BLACK
            return
        current = self.root
        y = self.NIL
        while current != self.NIL:
            y = current
            if current.key > key:
                current = current._left
            else:
                current = current._right
        if y.key > key:
            y._left = nodo
        else:
            y._right = nodo
        nodo._parent = y
        self.insert_fix_up(nodo)
    
    def _show_recursivo(self, nodo, nivel)->None:
        """Función auxiliar que comprueba que el nodo no este vacio y si es así llama a la misma función con el nodo de la derecha, luego imprime el nodo y luego llama a la misma función con el nodo de la izquierda.
        Así conseguimos que vaya imprimiendo de derecha a izzquierda."""
        if nodo != self.NIL:
            self._show_recursivo(nodo._right, nivel + 1)
            sangria = "    " * nivel
            if nodo.color == Color.RED:
                print(f"{sangria}-> {nodo.key} (ROJO)")
            else:
                print(f"{sangria}-> {nodo.key} (NEGRO)")
            self._show_recursivo(nodo._left, nivel + 1)
    def show_RB(self)-> None:
        """Va a imprimir el árbol. Mira si tiene raíz el árbol. Si no tiene, imprime árbol vacio y sino llema a una función auxilir, que va a ser la encargada dde ir imprimiendo el árbol."""
        if self.root == self.NIL:
            print("Árbol vacío.")
        else:
            print("- Árbol Rojo-Negro")
            self._show_recursivo(self.root, 0)
            print("------------------------")
    def count_nodo_auxiliar(self, nodo: RBNode)-> int:
        """Función auxiliar que reibe un nod y cuenta las hojas que hay a partir de ese nodo. Si ese nodo tiene hijo izquierdo llama de nbuevo a la función con el hijo izquierdo y sino izq = 0 y lo mismo con el derecho.
        Devuelve la cantidad de hojas (int)."""
        if nodo._left != self.NIL:
            izq = self.count_nodo_auxiliar(nodo._left)
        else:
            izq = 0
        if nodo._right != self.NIL:
            der = self.count_nodo_auxiliar(nodo._right)
        else:
            der = 0
        return 1 + izq + der
    def count_nodo_RB(self)-> int:
        """Función que devuelve en número de hojas que tiene el árbol. Si la raíz está vacia devuelve 0 y sino devolverá la cantidad de hpjas llamando a una función auxiliar."""
        if self.root == self.NIL:
            return 0
        else:
            return self.count_nodo_auxiliar(self.root)
        
    def height_auxiliar(self, nodo: RBNode)-> int:
        """Función auxiliar que reibe un nodo y cuenta la altura que hay a partir de ese nodo. Si ese nodo tiene hijo izquierdo llama de nuevo a la función con el hijo izquierdo y sino izq = -1 y lo mismo con el derecho.
        Devuelve la altura del árbol (int)."""
        if nodo._left != self.NIL:
            izq = self.height_auxiliar(nodo._left)
        else:
            izq = -1
        if nodo._right != self.NIL:
            der = self.height_auxiliar(nodo._right)
        else:
            der = -1
        return 1 + max(der, izq)
    def height_RB(self)-> int:
        """Función que devuelve la altura del árbol. Si la raíz está vacia devuelve -1 y sino devolverá la altura del árbol llamando a una función auxiliar."""
        if self.root == self.NIL:
            return -1
        else:
            return self.height_auxiliar(self.root)
    def find_node_auxiliar (self, node: RBNode, key: int)-> RBNode:
        """Función auxiliar que mira si el nodo recibido tiene la clave busacada. 
        Si es así devuelve ese nodo y sino si es mayor la clave del nodo, mira si tiene hijo izquierdo y si es así devolverá llamando a la misma función con el hijo izqueirdo y sino devolverá None. Lo mismo que con el derecho si el nodo.key es menor que key."""
        if node.key == key:
            return node
        else:
            if node.key > key:
                if node._left != self.NIL:
                    return self.find_node_auxiliar(node._left,key)
                else: 
                    return None
            else:
                if node._right != self.NIL:
                    return self.find_node_auxiliar(node._right,key)
                else:
                    return None

    def find_node_RB(self, key)->RBNode:
        """Función que deuvelve el nodo con la clave bsucada. Si el árbol está vacio, devuelve None y sino devuelve llamando a una función auxiliar."""
        if self.root == self.NIL:
            return None
        else:
            return self.find_node_auxiliar(self.root, key)
    def transplant(self, u:RBNode, v:RBNode):
        """Función auxiliar que elimina a u y pone en su posición v. No devuelve nada"""
        v._parent = u._parent
        if u._parent == self.NIL:
            self.root = v
        elif u._parent._right == u:
            u._parent._right = v
        else:
            u._parent._left = v
        v._parent = u._parent
    def tree_minimum(self, v):
        """Función auxiliar que devuelve el hijo izquierdo mas pequeño de un nodo que le pasan."""
        current = v
        while current._left != self.NIL:
            current = current._left
        return current
    def delete (self, key):
        """Función que le pasan una clave, busca si está el nodo con esa clave: Si no es así se acab la función, sino lo va a eliminar.
        Tres casos:
            -Sin hijo derecho.
            -Sin hijo izquierdo.
            -Con los dos hijos.
        Finalemnte, si el color_original es negro llama a la función auxiliar delete_fix_up. """
        nodo_borrar = self.find_node_RB(key)
        if nodo_borrar == self.NIL or nodo_borrar == None:
            print("nodo no encontrado")
            return
        y = nodo_borrar
        color_original_y = y.color
        if nodo_borrar._right == self.NIL:
            x = nodo_borrar._left
            self.transplant(nodo_borrar, nodo_borrar._left)
        elif nodo_borrar._left == self.NIL:
            x = nodo_borrar._right
            self.transplant(nodo_borrar, nodo_borrar._right)
        else:

            y = self.tree_minimum(nodo_borrar._right)
            color_original_y = y.color
            x = y._right
            if y != nodo_borrar._right:
                self.transplant(y, y._right)
                y._right = nodo_borrar._right
                y._right._parent = y
            else:
                x._parent = y
            self.transplant(nodo_borrar, y)
            y._left = nodo_borrar._left
            y._left._parent = y
            y.color = nodo_borrar.color
        if color_original_y == Color.BLACK:
            self.delete_fix_up(x)
    def delete_fix_up(self, x:RBNode)-> None:
        while x != self.root and x.color == Color.BLACK:
            if x == x._parent._right:
                w = x._parent._left
                if w.color == Color.RED:
                    w.color = Color.BLACK
                    x._parent.color = Color.RED
                    self.right_rotate(x._parent)
                    w = x._parent._left
                if w._left.color == Color.BLACK and w._right.color == Color.BLACK:
                    w.color = Color.RED
                    x = x._parent
                else:
                    if w._left.color == Color.BLACK:
                        w._right.color = Color.BLACK
                        w.color = Color.RED
                        self.left_rotate(w)
                        w = x._parent._left
                    w.color = x._parent.color
                    x._parent.color = Color.BLACK
                    w._left.color = Color.BLACK
                    self.right_rotate(x._parent)
                    x = self.root
            else:
                w = x._parent._right
                if w.color == Color.RED:
                    w.color = Color.BLACK
                    x._parent.color = Color.RED
                    self.left_rotate(x._parent)
                    w = x._parent._right
                if w._right.color == Color.BLACK and w._left.color == Color.BLACK:
                    w.color = Color.RED
                    x = x._parent
                else:
                    if w._right.color == Color.BLACK:
                        w._left.color = Color.BLACK
                        w.color = Color.RED
                        self.right_rotate(w)
                        w = x._parent._right
                    w.color = x._parent.color
                    x._parent.color = Color.BLACK
                    w._right.color = Color.BLACK
                    self.left_rotate(x._parent)
                    x = self.root
        x.color = Color.BLACK
    def min_height_auxiliar(self, nodo: RBNode) -> int:
        """Calcula el camino más corto desde el nodo hasta una hoja (NIL)."""
        if nodo == self.NIL:
            return -1
        
        izq = self.min_height_auxiliar(nodo._left)
        der = self.min_height_auxiliar(nodo._right)
        
        return 1 + min(izq, der)

    def skew_auxiliar(self, node: RBNode) -> bool:
        """
        En un Árbol Rojo-Negro, está desbalanceado (skewed) SÓLO si 
        la altura máxima es más del doble de la altura mínima.
        """
        if node == self.NIL:
            return False
        max_h = self.height_auxiliar(node)
        min_h = self.min_height_auxiliar(node)
        
        nodos_max = max_h + 1
        nodos_min = min_h + 1
        if nodos_max > (2 * nodos_min):
            return True 
            
        # Comprobamos recursivamente los hijos
        return self.skew_auxiliar(node._left) or self.skew_auxiliar(node._right)

    def skew_RB(self) -> bool:
        """Comprueba si el árbol rompe las reglas de balanceo Rojo-Negro."""
        if self.root == self.NIL:
            return False 
        else:
            return self.skew_auxiliar(self.root)
    def count_leafs_auxiliar(self, node: RBNode)-> int:
        """Función recursiva auxiliar para contar los nodos hoja. Recibe un nodo
        Recorre el subárbol a partir del nodo indicado. Si encuentra un nodo vacío (NIL), devuelve 0. Si encuentra un nodo hoja (sin hijos), devuelve 1. Si no, suma las hojas de sus ramas izquierda y derecha.
        Devuelve la cantidad de nodos hoja encontrados en este subárbol.
        """
        if node == self.NIL:
            return 0
        elif node._right == self.NIL and node._left == self.NIL:
            return 1
        else:
            der = self.count_leafs_auxiliar(node._right)
            izq = self.count_leafs_auxiliar(node._left)
        return der + izq
        
    def count_leafs_RB(self) ->int:
        """Cuenta el número total de nodos hoja que existen en el árbol. Devuelve el número total de hojas en todo el árbol. Devuelve 0 si el árbol está vacío"""
        if self.root == self.NIL:
            return 0
        else:
            return self.count_leafs_auxiliar(self.root)
    def longest_path_auxiliar(self, node: RBNode) -> list:
        """
        Función recursiva que busca el camino más largo desde las hojas. Devuelve una lista de palabras (keys).
        """
        if node == self.NIL:
            return []
        ruta_izq = self.longest_path_auxiliar(node._left)
        ruta_der = self.longest_path_auxiliar(node._right)
        if len(ruta_izq) > len(ruta_der):
            return ruta_izq + [node.key]
        else:
            return ruta_der + [node.key]
    def longest_path_RB(self) -> list:
        """
        Encuentra la ruta más larga desde una hoja hasta la raíz del árbol.Devuelve una lista con las palabras (keys) en orden desde la hoja hasta la raíz.
        Si el árbol está vacío, devuelve una lista vacía [].
        """
        if self.root == self.NIL:
            return []
        else:
            return self.longest_path_auxiliar(self.root)
    def paths_to_leaf_with_length_RB(self, node: RBNode, remaining_edges: int, current_path: list = None, results: list = None) -> list:
        """
        Devuelve todos los caminos raiz->hoja con longitud exacta (en aristas) igual
        a remaining_edges al comienzo de la llamada. Aplicando Backtracking.
        """
        if current_path is None:
            current_path = []
        if results is None:
            results = []
        if node == self.NIL:
            return results

        current_path.append(str(node.key))
        es_hoja = (node._left == self.NIL and node._right == self.NIL)

        if es_hoja:
            if remaining_edges == 0:
                results.append(list(current_path))
        else:
            if remaining_edges > 0:
                self.paths_to_leaf_with_length_RB(node._left, remaining_edges - 1, current_path, results)
                self.paths_to_leaf_with_length_RB(node._right, remaining_edges - 1, current_path, results)
        current_path.pop()
        return results
    
    def in_order_nodo(self, nodo: RBNode)-> None:
        """
        Realiza un recorrido in-order de forma recursiva a partir de un nodo dado.
        Visita primero el subárbol izquierdo, luego el nodo actual, y por último el subárbol derecho.
        Recibe el nodo desde el cual se inicia el recorrido, no devuelve nada.
        """
        if nodo != self.NIL:
            self.in_order_nodo(nodo.get_left())
            print(nodo.key)
            self.in_order_nodo(nodo.get_right())


    def in_order(self)-> None:
        """
        Inicia un recorrido in-order desde la raíz del árbol.
        Imprime "Árbol vacío." si el árbol no contiene elementos.
        """
        if self.root == self.NIL:
            print("Árbol vacío.")
        else:
            self.in_order_nodo(self.root)

    def pre_order_nodo(self, nodo: RBNode)-> None:
        """
        Realiza un recorrido pre-order de forma recursiva a partir de un nodo dado.
        Visita primero el nodo actual, luego el subárbol izquierdo, y por último el subárbol derecho.
        Recibe el nodo desde el cual se inicia el recorrido, no deuvelve nada
        """
        if nodo != self.NIL:
            print(nodo.key)
            self.pre_order_nodo(nodo.get_left())
            self.pre_order_nodo(nodo.get_right())

    def pre_order(self)-> None:
        """
        Inicia un recorrido pre-order desde la raíz del árbol.
        Imprime "Árbol vacío." si el árbol no contiene elementos.
        """
        if self.root == self.NIL:
            print("Árbol vacío.")
        else:
            self.pre_order_nodo(self.root)

    def post_order_nodo(self, nodo: RBNode)-> None:
        """
        Realiza un recorrido post-order de forma recursiva a partir de un nodo dado.
        Visita primero el subárbol izquierdo, luego el subárbol derecho, y por último el nodo actual.
        Recibe el nodo desde el cual se inicia el recorrido, no deuvelve nada
        """
        if nodo != self.NIL:
            self.post_order_nodo(nodo.get_left())
            self.post_order_nodo(nodo.get_right())
            print(nodo.key)

    def post_order(self)-> None:
        """
        Inicia un recorrido post-order desde la raíz del árbol.
        Imprime "Árbol vacío." si el árbol no contiene elementos.
        """
        if self.root == self.NIL:
            print("Árbol vacío.")
        else:
            self.post_order_nodo(self.root)

def level_order(tree: 'RedBlackTree') -> None:
    """
    Realiza un recorrido por niveles (anchura) de todo el árbol.
    Utiliza una lista a modo de cola para visitar los nodos nivel por nivel, 
    de izquierda a derecha.
    Recibe el árbol que se va a recorrer, sin devolver nada
    """
    cola = []
    if tree.root != tree.NIL:
        cola.append(tree.root)
    while len(cola) > 0:
        nodo_actual = cola.pop(0)
        print(nodo_actual.key)
        if nodo_actual.get_left() != tree.NIL:
            cola.append(nodo_actual.get_left())
        if nodo_actual.get_right() != tree.NIL:
            cola.append(nodo_actual.get_right())
if __name__ == "__main__":
    print("\n==================================================")
    print("        PRUEBAS DE ÁRBOL ROJO-NEGRO")
    print("==================================================")

    rb_tree = RedBlackTree()

    print("\n--- TEST 1: Insertar Nodos ---")
    valores = [10, 18, 7, 15, 16, 30, 25, 40, 60, 2, 1, 70]
    print(f"Insertando valores: {valores}")
    for val in valores:
        rb_tree.insert_RB(val)

    # Nota: He calculado a mano cómo queda tu árbol tras insertar esos 12 valores.
    print("\n[SALIDA ESPERADA - Estructura tras inserciones]")
    print("La raíz debería ser el 16. Los nodos balanceados por colores.")
    
    print("\n[SALIDA OBTENIDA]")
    rb_tree.show_RB()


    print("\n--- TEST 2: Conteo de Nodos y Hojas ---")
    print("[SALIDA ESPERADA] Nodos totales: 12 | Hojas: 6 (Nodos 1, 7, 16, 25, 40, 70)")
    print(f"[SALIDA OBTENIDA] Nodos totales: {rb_tree.count_nodo_RB()} | Hojas: {rb_tree.count_leafs_RB()}")


    print("\n--- TEST 3: Altura y Búsqueda ---")
    print("[SALIDA ESPERADA] Altura: 4 | Buscar 15: Encontrado (NEGRO) | Buscar 99: No encontrado")
    
    # Obtención de datos reales
    nodo_15 = rb_tree.find_node_RB(15)
    color_15 = "ROJO" if nodo_15 and nodo_15.color == Color.RED else "NEGRO"
    busqueda_15 = f"Encontrado ({color_15})" if nodo_15 else "No encontrado"
    nodo_99 = rb_tree.find_node_RB(99)
    busqueda_99 = "Encontrado" if nodo_99 else "No encontrado"
    
    print(f"[SALIDA OBTENIDA] Altura: {rb_tree.height_RB()} | Buscar 15: {busqueda_15} | Buscar 99: {busqueda_99}")


    print("\n--- TEST 4: Inclinación (Skew) ---")
    print("[SALIDA ESPERADA] ¿Hay alguna rama desbalanceada por más de 1 nivel?: False (Es un árbol Rojo-Negro balanceado)")
    print(f"[SALIDA OBTENIDA] ¿Hay alguna rama desbalanceada?: {rb_tree.skew_RB()}")


    print("\n--- TEST 5: Eliminar Nodos (Delete) ---")
    print("Eliminando el nodo 70 (hoja)...")
    rb_tree.delete(70)
    print("Eliminando el nodo 16 (fuerza rebalanceo)...")
    rb_tree.delete(16)
    
    print("\n[SALIDA ESPERADA - Tras borrar 70 y 16]")
    print("Nodos totales esperados: 10")
    print("\n[SALIDA OBTENIDA]")
    print(f"Nodos totales tras borrar: {rb_tree.count_nodo_RB()}")


    print("\n--- TEST 6: Caminos (Longest Path y Backtracking) ---")
    longitud_objetivo = 3
    print(f"\n[SALIDA ESPERADA] Caminos con longitud {longitud_objetivo} aristas: Lista que contiene ramas válidas desde la raíz 18")
    caminos_exactos = rb_tree.paths_to_leaf_with_length_RB(rb_tree.root, longitud_objetivo)
    
    print(f"[SALIDA OBTENIDA] Caminos con longitud {longitud_objetivo}:")
    for camino in caminos_exactos:
        print(" -> ".join(camino))


    print("\n--- TEST 7: Recorridos del Árbol (Requerido por PDF) ---")
    
    print("\n[In-Order]")
    print("Salida Esperada: 1 -> 2 -> 7 -> 10 -> 15 -> 18 -> 25 -> 30 -> 40 -> 60")
    print("Salida Obtenida:")
    rb_tree.in_order()
    
    print("\n[Pre-Order]")
    print("Salida Esperada: 18 -> 10 -> 2 -> 1 -> 7 -> 15 -> 40 -> 25 -> 30 -> 60")
    print("Salida Obtenida:")
    rb_tree.pre_order()
    
    print("\n[Post-Order]")
    print("Salida Esperada: 1 -> 7 -> 2 -> 15 -> 10 -> 30 -> 25 -> 60 -> 40 -> 18")
    print("Salida Obtenida:")
    rb_tree.post_order()
    
    print("\n[Level-Order]")
    print("Salida Esperada: 18 -> 10 -> 40 -> 2 -> 15 -> 25 -> 60 -> 1 -> 7 -> 30")
    print("Salida Obtenida:")
    level_order(rb_tree)

    print("\n==================================================")