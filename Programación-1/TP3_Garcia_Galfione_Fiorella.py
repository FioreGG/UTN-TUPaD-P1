
from statistics import mean, median, mode
import random

# Actividad 1
print("Actividad 1")
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")
print("-" * 40)

# Actividad 2
print("Actividad 2")
nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
print("-" * 40)

# Actividad 3
print("Actividad 3")
numero = int(input("Ingrese un número par: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")
print("-" * 40)

# Actividad 4
print("Actividad 4")
edad_categoria = int(input("Ingrese su edad: "))
if edad_categoria < 12:
    print("Niño/a")
elif edad_categoria >= 12 and edad_categoria < 18:
    print("Adolescente")
elif edad_categoria >= 18 and edad_categoria < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")


# Actividad 5
print("Ejercicio 5: Validar longitud de contraseña")
contrasena = input("Ingrese una contraseña (entre 8 y 14 caracteres): ")

if 8 <= len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")
    
print("-" * 40)


# Actividad 6
print("Ejercicio 6: Calcular media, mediana y moda, y analizar sesgo")
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

if media > mediana > moda:
    print("La distribución tiene sesgo positivo (a la derecha).")
elif media < mediana < moda:
    print("La distribución tiene sesgo negativo (a la izquierda).")
elif media == mediana == moda:
    print("La distribución no tiene sesgo.")
else:
    print("No se puede determinar un sesgo claro.")

print("-" * 40)

# Actividad 7
print("Ejercicio 7: Verificar si una frase termina con vocal")
frase = input("Ingrese una palabra o frase: ")
ultima_letra = frase[-1].lower()

if ultima_letra in "aeiou":
    frase += "!"
    print("Frase modificada:", frase)
else:
    print("Frase sin modificar:", frase)

print("-" * 40)

# Actividad 8
print("Ejercicio 8: Modificar el nombre según la opción elegida")
nombre = input("Ingrese su nombre: ")
opcion = input("Ingrese una opción (1: MAYÚSCULAS, 2: minúsculas, 3: Capitalizada): ")

if opcion == "1":
    print("Nombre en MAYÚSCULAS:", nombre.upper())
elif opcion == "2":
    print("Nombre en minúsculas:", nombre.lower())
elif opcion == "3":
    print("Nombre Capitalizado:", nombre.title())
else:
    print("Opción no válida.")

print("-" * 40)

# Actividad 9
print("Ejercicio 9: Clasificación de terremotos según escala de Richter")

magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible).")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible).")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos).")
else:  # magnitud >= 7
    print("Extremo (puede causar graves daños a gran escala).")

print("-" * 40)

# Actividad 10
print("Ejercicio 10: Determinar estación del año según hemisferio y fecha")

hemisferio = input("Ingrese el hemisferio en el que se encuentra (N/S): ").upper()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día (1-31): "))

# Convertimos la fecha a un número para facilitar comparación: MMDD
fecha = mes * 100 + dia

if hemisferio == "N":
    if 1221 <= fecha <= 1231 or 101 <= fecha <= 320:
        estacion = "Invierno"
    elif 321 <= fecha <= 620:
        estacion = "Primavera"
    elif 621 <= fecha <= 920:
        estacion = "Verano"
    elif 921 <= fecha <= 1220:
        estacion = "Otoño"
    else:
        estacion = "Fecha no válida"
elif hemisferio == "S":
    if 1221 <= fecha <= 1231 or 101 <= fecha <= 320:
        estacion = "Verano"
    elif 321 <= fecha <= 620:
        estacion = "Otoño"
    elif 621 <= fecha <= 920:
        estacion = "Invierno"
    elif 921 <= fecha <= 1220:
        estacion = "Primavera"
    else:
        estacion = "Fecha no válida"
else:
    estacion = "Hemisferio no válido"

print("La estación del año es:", estacion)

print("-" * 40)