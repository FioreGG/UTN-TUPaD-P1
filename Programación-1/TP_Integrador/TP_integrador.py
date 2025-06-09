# TP INTEGRADOR - CASO PRÁCTICO DE ÁRBOLES

# Árbol binario de peliculas - implementado con listas

def crear_arbol(valor):
    return [valor, [], []]  #Creamos un nodo raiz

def insertar_izquierda(nodo, valor): #Teniendo en cuenta que puede existir un subarbol 
    if nodo[1]:
        nodo[1] = [valor, nodo[1], []]
    else:
        nodo[1] = [valor, [], []]

def insertar_derecha(nodo, valor):
    if nodo[2]:
        nodo[2] = [valor, [], nodo[2]]
    else:
        nodo[2] = [valor, [], []]

def recorrido_preorden(nodo):
    """Preorden: raíz → izquierda → derecha"""
    if nodo:
        print(nodo[0], end=' ')
        recorrido_preorden(nodo[1])
        recorrido_preorden(nodo[2])

def recorrido_inorden(nodo):
    """Inorden: izquierda → raíz → derecha"""
    if nodo:
        recorrido_inorden(nodo[1])
        print(nodo[0], end=' ')
        recorrido_inorden(nodo[2])

def recorrido_postorden(nodo):
    """Postorden: izquierda → derecha → raíz"""
    if nodo:
        recorrido_postorden(nodo[1])
        recorrido_postorden(nodo[2])
        print(nodo[0], end=' ')

def imprimir_arbol(nodo, nivel=0):
    """Imprime el árbol rotado 90° hacia la izquierda."""
    if nodo:
        imprimir_arbol(nodo[2], nivel + 1)
        print('   ' * nivel + str(nodo[0]))
        imprimir_arbol(nodo[1], nivel + 1)

# Ejemplo práctico: Árbol de peliculas
if __name__ == "__main__":
    # Nivel 1 - Raíz
    arbol = crear_arbol("Películas")

    # Nivel 2
    insertar_izquierda(arbol, "Animadas")
    insertar_derecha(arbol, "Ciencia Ficción")

    # Nivel 3 Animadas
    insertar_izquierda(arbol[1], "Lilo y Stich")
    insertar_derecha(arbol[1], "Mufasa")

    # Nivel 3 Ciencia Ficción
    insertar_izquierda(arbol[2], "Misión Imposible")
    insertar_derecha(arbol[2], "Destino Final")

    print(" Árbol rotado 90°:")
    imprimir_arbol(arbol)

    print(" Recorrido Preorden:")
    recorrido_preorden(arbol)

    print(" Recorrido Inorden:")
    recorrido_inorden(arbol)

    print(" Recorrido Postorden:")
    recorrido_postorden(arbol)
