import random

# TP4: Estructuras repetitivas

# Actividad 1

"""  Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea. """

for i in range (101):
    print(i)

# Actividad 2

""" Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene"""

numero = (input("Ingrese un numero entero: "))

long = len(numero)

print(f"La cantidad de digitos que contiene el {numero} es: {long}" )

# Actividad 3

""" Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores """

numero1=int(input("Ingrese el numero 1: "))
numero2=int(input("Imgrese el numero 2: "))

if numero1>numero2:
    numero1, numero2=numero2, numero1

suma=0
for i in range(numero1+1, numero2):
    suma+=i

print("La suma de los numeros entre ", numero1, " y ", numero2, " es: ", suma)

# Actividad 4

"""Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0."""

total = 0

while True:
    numero = int(input("Ingrese un numero entero (0 para terminar): "))
    if numero ==0:
        break
    total += numero

print("La suma total es: ", total)

# Actividad 5

""" Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número."""

numero_secreto = random.randint(0,9)
intentos=0

print("Adivina el numero entre 0 y 9: ")

while True:
    intento = int(input("Tu intento: "))
    intentos += 1
    if intento == numero_secreto:
        print("El numero ingresado es correcto, acertaste en ", intentos, "intentos.")
        break
    else:
        print("Incorrecto, pruebe de nuevo")


# Actividad 6

''' Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente. '''

for i in range(100, -1, -1):
    if i % 2 ==0:
        print(i)

# Actividad 7

''' Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario.'''

numero_ingresado=int(input("Ingrese un numero entero positivo: "))

if numero_ingresado <0:
    print("El numero debe ser positivo")
else:
    suma=sum(range(numero_ingresado+1))
    print("La suma de los numeros entre ", numero_ingresado, " y 0 es: ", suma)

# Actividad 8

''' Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio).'''

pares = 0
impares = 0
positivos = 0
negativos = 0

cantidad = 100  # Puedes cambiarlo a un número menor para probar

for _ in range(cantidad):
    numero = int(input("Ingresa un número entero: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero >= 0:
        positivos += 1
    else:
        negativos += 1

print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")

# Actividad 9

''' Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor).
'''

suma = 0
cantidad = 10  # Puedes cambiarlo para probar

for _ in range(cantidad):
    numero = int(input("Ingresa un número entero: "))
    suma += numero

media = suma / cantidad
print(f"La media de los números ingresados es {media}.")

# Actividad 10

''' ) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.'''

numero = int(input("Ingresa un número entero: "))

# Tomamos el valor absoluto para invertir sin el signo
numero_invertido = int(str(abs(numero))[::-1])

# Si el número original era negativo, lo hacemos negativo
if numero < 0:
    numero_invertido = -numero_invertido

print(f"El número invertido es {numero_invertido}")
