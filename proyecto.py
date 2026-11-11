from binarytree import BinaryTree, Node
import sys
sys.setrecursionlimit(100000)
from binarytree import BinaryTree, Node
from RedBlackTree import RedBlackTree # Asegúrate de que el nombre del archivo coincida con el tuyo
import sys

# El límite de recursión es vital aquí: el diccionario RAE desbalanceará tanto 
# el árbol binario normal que la recursión se disparará.
sys.setrecursionlimit(100000)

def comparar_arboles(letra: str, bt: BinaryTree, rb: RedBlackTree):
    """Función auxiliar para imprimir las métricas de ambos árboles cara a cara."""
    print()
    print(f"==========================================================")
    print(f"=== COMPARACIÓN PARA LA LETRA '{letra.upper()}' ===")
    print(f"==========================================================")
    
    # 1. Total de Nodos (Deberían ser exactamente los mismos)
    nodos_bt = bt.count_nodes_tree()
    nodos_rb = rb.count_nodo_RB()
    print(f"Nodos totales    | BT: {nodos_bt:<6} | RBT: {nodos_rb}")
    
    # 2. Altura (Aquí verás la magia del Rojo-Negro)
    alt_bt = bt.height()
    alt_rb = rb.height_RB()
    print(f"Altura máxima    | BT: {alt_bt:<6} | RBT: {alt_rb}")
    
    # 3. Nodos Hoja
    hojas_bt = bt.count_leafs()
    hojas_rb = rb.count_leafs_RB()
    print(f"Nodos hoja       | BT: {hojas_bt:<6} | RBT: {hojas_rb}")
    
    # 4. Inclinación (Skew)
    skew_bt = bt.skew()
    skew_rb = rb.skew_RB()
    print(f"¿Está Inclinado? | BT: {str(skew_bt):<6} | RBT: {str(skew_rb)}")
    
    # 5. Longitud del camino más largo
    camino_bt = bt.longest_path()
    camino_rb = rb.longest_path_RB()
    print(f"Long. Camino Máx | BT: {len(camino_bt):<6} | RBT: {len(camino_rb)}")


if __name__ == "__main__":
    letra1 = input('Dime la primera letra: ').lower()
    letra2 = input('Dime la segunda letra: ').lower()
    letra3 = input('Dime la tercera letra: ').lower()
    
    arbol_bt_1 = BinaryTree(None)
    arbol_bt_2 = BinaryTree(None)
    arbol_bt_3 = BinaryTree(None)

    arbol_rb_1 = RedBlackTree()
    arbol_rb_2 = RedBlackTree()
    arbol_rb_3 = RedBlackTree()

    print("\nLeyendo palabras e insertando en los árboles... (Esto puede tardar unos segundos)")
    

    # Abrimos el fichero de la RAE
    with open('palabras_RAE_cleaned_noaccents.txt', 'r', encoding='utf-8') as fichero:
        for linea in fichero:
            palabra = linea.strip()
            if len(palabra) > 0:
                inicial = palabra[0].lower()
                
                # Insertamos en el par de árboles correspondiente
                if inicial == letra1:
                    arbol_bt_1.insert(palabra, palabra)
                    arbol_rb_1.insert_RB(palabra)
                elif inicial == letra2:
                    arbol_bt_2.insert(palabra, palabra)
                    arbol_rb_2.insert_RB(palabra)
                elif inicial == letra3:
                    arbol_bt_3.insert(palabra, palabra)
                    arbol_rb_3.insert_RB(palabra)
                    
    print("¡Todos los árboles han sido cargados con éxito!")
    
    # Mostramos las comparativas
    comparar_arboles(letra1, arbol_bt_1, arbol_rb_1)
    comparar_arboles(letra2, arbol_bt_2, arbol_rb_2)
    comparar_arboles(letra3, arbol_bt_3, arbol_rb_3)
    


