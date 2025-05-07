# Actividades
'''1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
range.'''

lista_1 =list(range(0,101,4))
lista_1.remove(0)
print(lista_1)


'''2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
indexing con números negativos!'''

lista_2 = ["Silla", "Mesa", 2, 3, 9.6]
print(lista_2[3])


'''3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
pantalla. 
'''
lista_vacia_3 = [] 
lista_vacia_3.append("Galletas")
lista_vacia_3.append(65.32)
lista_vacia_3.append(True)

print(lista_vacia_3)

'''4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
en los videos o bien investigar cómo funciona el indexing con números negativos!
animales = ["perro", "gato", "conejo", "pez"]'''

animales = ["perro", "gato", "conejo", "pez"]

animales[1] = "loro"
animales[3] = "oso"

print(animales)


'''5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.'''

numeros = [8,15,3,22,7]
numeros.remove(max(numeros))
print(numeros)

'Lo que se realiza en este caso es remover el numero maximo, es decir el valor mas grande de la lista, '
'en este caso el valor mas grande la lista era el 22 y como se uso el remove, se quito ese numero'

'''6) Crear una lista con numeros del 10 al 30 incluido, haciendo saltos de cinco en cinco y mostrar por
pantalla los dos primeros'''

lista_6 = list(range(10,31,5))
#print(lista_6)

print(lista_6[0],lista_6[1])

'''7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
cualesquiera.
autos = ["sedan", "polo", "suran", "gol"]'''

autos = ["Sedan", "Polo", "Suran", "Gol"]

autos[1]="Cruize"
autos[2]="Ford Fiesta"

print(autos)

'''8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
directamente. Imprimir la lista resultante por pantalla.
'''

dobles = []

dobles.append(5*2)
dobles.append(2*10)
dobles.append(15*2)

print(dobles)

''' 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
diferentes clientes:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]
a) Agregar "jugo" a la lista del tercer cliente usando append.
b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
c) Eliminar "pan" de la lista del primer cliente.
d) Imprimir la lista resultante por pantalla'''

compras =  [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]

#a
compras[2].append("jugo")
print(compras)
#b
compras[1][1] = "tallarines"
print(compras)
#c
compras[0].remove("pan")
print(compras)
#d
print(compras)

'''10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
● Posición lista_anidada[0]: 15
● Posición lista_anidada[1]: True
● Posición lista_anidada[2][0]: 25.5
● Posición lista_anidada[2][1]: 57.9
● Posición lista_anidada[2][2]: 30.6
● Posición lista_anidada[3]: False
Imprimir la lista resultante por pantalla.'''

lista_anidada = [15, True, [25.5,57.9, 30.6],False]

print(lista_anidada)

