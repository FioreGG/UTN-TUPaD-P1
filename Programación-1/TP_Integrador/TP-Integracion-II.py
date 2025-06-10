# TP INTEGRADOR - CASO PRÁCTICO DE ÁRBOLES
# Árbol binario de películas - implementado con listas

# Función para crear un nuevo árbol (nodo raíz)
def crear_arbol(valor):
    # Cada nodo es una lista con tres elementos: [valor, subárbol izquierdo, subárbol derecho]
    return [valor, [], []]

# Función para insertar un nodo a la izquierda
def insertar_izquierda(nodo, valor):
    # Si ya existe un subárbol izquierdo, lo anida como hijo del nuevo nodo
    if nodo[1]:
        nodo[1] = [valor, nodo[1], []]
    else:
        # Si no hay subárbol izquierdo, simplemente lo inserta
        nodo[1] = [valor, [], []]

# Función para insertar un nodo a la derecha
def insertar_derecha(nodo, valor):
    # Si ya existe un subárbol derecho, lo anida como hijo del nuevo nodo
    if nodo[2]:
        nodo[2] = [valor, [], nodo[2]]
    else:
        # Si no hay subárbol derecho, simplemente lo inserta
        nodo[2] = [valor, [], []]

# Función para recorrer el árbol en preorden: raíz → izquierda → derecha
def recorrido_preorden(nodo):
    if nodo:
        print(nodo[0], end=' ')          # Imprime el valor del nodo actual
        recorrido_preorden(nodo[1])      # Recorre subárbol izquierdo
        recorrido_preorden(nodo[2])      # Recorre subárbol derecho

# Función para recorrer el árbol en inorden: izquierda → raíz → derecha
def recorrido_inorden(nodo):
    if nodo:
        recorrido_inorden(nodo[1])       # Recorre subárbol izquierdo
        print(nodo[0], end=' ')          # Imprime el valor del nodo actual
        recorrido_inorden(nodo[2])       # Recorre subárbol derecho

# Función para recorrer el árbol en postorden: izquierda → derecha → raíz
def recorrido_postorden(nodo):
    if nodo:
        recorrido_postorden(nodo[1])     # Recorre subárbol izquierdo
        recorrido_postorden(nodo[2])     # Recorre subárbol derecho
        print(nodo[0], end=' ')          # Imprime el valor del nodo actual

# Función para imprimir el árbol rotado 90° hacia la izquierda
def imprimir_arbol(nodo, nivel=0):
    if nodo:
        imprimir_arbol(nodo[2], nivel + 1)                         # Muestra primero el subárbol derecho (más arriba)
        print('   ' * nivel + str(nodo[0]))                        # Imprime el nodo actual con sangría según su nivel
        imprimir_arbol(nodo[1], nivel + 1)                         # Luego muestra el subárbol izquierdo

# Ejemplo práctico: creación de un árbol de películas
if __name__ == "__main__":
    # Nivel 1 - Nodo raíz
    arbol = crear_arbol("Películas")

    # Nivel 2 - Se agregan las dos categorías principales
    insertar_izquierda(arbol, "Animadas")
    insertar_derecha(arbol, "Ciencia Ficción")

    # Nivel 3 - Películas dentro de la categoría "Animadas"
    insertar_izquierda(arbol[1], "Lilo y Stich")
    insertar_derecha(arbol[1], "Mufasa")

    # Nivel 3 - Películas dentro de la categoría "Ciencia Ficción"
    insertar_izquierda(arbol[2], "Misión Imposible")
    insertar_derecha(arbol[2], "Destino Final")

    # Visualización del árbol rotado 90°
    print(" Árbol rotado 90°:")
    imprimir_arbol(arbol)

    # Recorridos del árbol
    print(" Recorrido Preorden:")
    recorrido_preorden(arbol)

    print(" Recorrido Inorden:")
    recorrido_inorden(arbol)

    print(" Recorrido Postorden:")
    recorrido_postorden(arbol)
