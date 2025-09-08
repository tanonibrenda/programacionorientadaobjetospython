print("------ Ejercicio 1 -------")
print("/n/n")
print("Generar numeros en forma aleratoria")
# Ejercicio 1
# Implementar un programa que permita generar cuatro números aleatorios y
# calcule el promedio.

# Importamos librería
import random


# Función para obtener una lista de números aleatorios
def obtener_numeros(cantidad):
    numeros = []
    for i in range(cantidad):
        num = random.randint(1, 100)
        numeros.append(num)
    return numeros


# Función para calcular el promedio
def calcular_promedio(numeros):
    promedio = sum(numeros) / len(numeros)
    return promedio


# Calculo el promedio de cuatro números aleatorios
numeros = obtener_numeros(4)
promedio = calcular_promedio(numeros)

# Imprimo en pantalla
print("Números generados:", numeros)
print("Promedio:", promedio)

# tambien se puede importar una parte de la librería
# from random import randint  esto lo que hace es importar solo la función randint que es mas eficiente.

print("---Opcion importando random---")
# Importamos librería
import random


# Función para obtener una lista de números aleatorios dentro de un rango
def obtener_numeros(cantidad, desde, hasta):
    numeros = []
    for i in range(cantidad):
        num = random.randint(desde, hasta)
        numeros.append(num)
    return numeros


# Función para calcular el promedio
def calcular_promedio(numeros):
    promedio = sum(numeros) / len(numeros)
    return promedio


# Solicito al usuario el rango
print("Generador de números aleatorios")
desde = int(input("Ingrese el valor mínimo (desde): "))
hasta = int(input("Ingrese el valor máximo (hasta): "))

# Calculo el promedio de cuatro números aleatorios dentro del rango
numeros = obtener_numeros(4, desde, hasta)
promedio = calcular_promedio(numeros)

# Imprimo en pantalla
print("Números generados:", numeros)
print("Promedio:", promedio)

print("------ Ejercicio 2 -------")
print("/n/n")
# Ejercicio 2 
# El lenguaje Python provee diversas formas de utilizar cadenas para mostrar 
# resultados en la pantalla. Considerando que se tienen las variables marca = 
# “Motorola”, modelo = “G8”, memoria = “3”, indicar tres o más formas distintas 
# de generar la frase “Su celular es el modelo G8 de la marca Motorola y tiene 
# 3GB de RAM”.

marca = "Motorola"
modelo = "G8"
memoria = "3"
print("Diferentes formas de mostrar el mismo mensaje")
print(f"1. Su celular es el modelo " + modelo + " de la marca " + marca + " y tiene " + memoria + "G de RAM")

print(f"2. Su celular es el modelo {modelo} de la marca {marca} y tiene {memoria}G de RAM")

print("3. Su celular es el modelo " + modelo + " de la marca " + marca + " y tiene " + memoria + "GB de RAM")

# usando listas y join
partes = ["4. Su celular es el modelo", modelo, "de la marca", marca, "y tiene", memoria + "GB de RAM"]
print(" ".join(partes))

# usando un diccionario
celular = {
    "marca": "Motorola",
    "modelo": "G8",
    "memoria": "3"
}

# Usamos f-string para acceder a los valores del diccionario
print(
    f"5. Su celular es el modelo {celular['modelo']} de la marca {celular['marca']} y tiene {celular['memoria']}GB de RAM")

# Ejercicio 3 
# En una aplicación para generar una cuenta de usuario, se aplica una serie de 
# controles para que el usuario ingrese su nombre de usuario de manera 
# correcta, teniendo en cuenta que debe respetar las siguientes condiciones: 
# a) Debe contener al menos 6 caracteres. 
# b) Debe comenzar con una letra mayúscula y todas las demás en minúsculas. 
# c) No debe tener espacios al comienzo ni al final. 
# d) No puede contener números. Indicar las expresiones necesarias para realizar cada uno de los controles 
# sobre la variable nombreUsuario. Luego implementar un programa que permita 
# al usuario ingresar el nombre deseado e indicar si es correcto o no cumple 
# alguna de las condiciones solicitadas. Agregar al menos dos condiciones más 
# (a elección) e implementarlas junto a las anteriores.

print("------ Ejercicio 3 -------")
print("/n/n")
print("Validar nombre de usuario")
print("------ Opcion con if-else anidado: si se cumplen las condiciones -------")

# importar modulo para ver si la contraseña tiene caracteres especiales
from string import punctuation


def validar_password1(password1):
    if len(password1) >= 6:  # mide si tiene mas de 6 caracteres
        if any([pw.isdigit() for pw in password1]):  # pide que vea si algun numero
            if any([pw.islower() for pw in password1]):  # Pide minuscula
                if any([pw.isupper() for pw in password1]):  # Pide mayuscula
                    if any([True if pw in punctuation else False for pw in password1]):  # Pide caracter especial
                        print("Contraseña Valida")
                        return True
                    else:
                        print("La contraseña debe contener algun caracter especial")
                else:
                    print("La contraseña debe contener al menos una mayuscula")
            else:
                print("La contraseña debe contener al menos una minuscula")
        else:
            print("La contraseña debe tener al menos un numero")
    else:
        print("La contraseña debe tener al menos 6 caractes")
    return False


if __name__ == "__main__":
    password1 = input(
        "Ahora va a generar una contraseña, debe tener al menos 6 caracteres, una mayuscula, una minucula, un numero y un caracter especial.Ingrese su contraseña: ")
    validar_password1(password1)

print("Opcion 2 con no cumple las condiciones con elif")

# importar modulo para ver si la contraseña tiene caracteres especiales
from string import punctuation


def validar_password2(password2):
    if len(password2) < 6:  # mide si tiene mas de 6 caracteres
        print("La contraseña debe tener 6 o màs caracteres ")
    elif not any([pww.isdigit() for pww in password2]):
        print("La contraseña debe tener al menos un numero")  # pide que vea si algun numero
    elif any([pww.islower() for pww in password2]):  # Pide minuscula
        print("La contraseña debe contener al menos una minuscula")
    elif any([pww.isupper() for pww in password2]):  # Pide mayuscula
        print("La contraseña debe contener al menos una mayuscula")
    elif any([True if pww in punctuation else False for pww in password2]):  # Pide caracter especial
        print("La contraseña debe contener algun caracter especial")
    else:
        print("Contraseña correcta")
        return True
    return False


if __name__ == "__main__":
    password2 = input(
        "Ahora va a generar una contraseña,\n debe tener al menos 6 caracteres,\n una mayuscula, \nuna minucula, \nun numero y un caracter especial.\nIngrese su contraseña: ")
    validar_password2(password2)

print("\n")
print("\n\n")
print("ahora con bucle")

intentos = 0  # inicializo la cantidad de intentos

while True:
    password_input = input("Introduce la contraseña para el primer bucle: ")
    intentos += 1

    if validar_password1(password_input):
        print(f"La contraseña introducida ha sido: {password_input}")
        break
    elif intentos > 5:
        print("No ha podido acceder a su cuenta. Intentelo mas tarde.")
        break

print("\n")
print("\n\n")
print("-----Ejercicio 4-------")
print("/n/n")
# Ejercicio 4 
# generen una lista con al menos 7 palabras y a continuación implementen un 
# script que pueda detectar cuantas de esas palabras son palíndromos y cuál es 
# el palíndromo con más caracteres.

print("Detectar palíndromos en una lista")
print("\n")
print(
    "Definicion de palindromo de la Real Academia Española: \n Palabra o frase cuyas letras están dispuestas de tal manera que resulta la misma leída de izquierda a derecha que de derecha a izquierda; por ejemplo, anilina; dábale arroz a la zorra el abad.")
print("\n")
# ejemplos de palindromos: arenera, erre, ana, rodador, salas

print(" Version 1")
print("\n")
word = input("ingrese una palabra: ")


def palindromo(word):
    reverse = str(word).lower().replace(' ', ' ')  # cadenas van a ser minuscula
    print(reverse, reverse[::-1])
    if reverse == reverse[::-1]:  # [::-1] se invierte la cadena y quita los espacios vacios
        return True
    else:
        return False


print(palindromo(word))

# Version 2
print("\n")
print("\n")
print("---- Version 2 de ejercicio 4")
print("\n")


def es_palindromo(palabra):
    # Normalizar: pasar a minúsculas y eliminar espacios
    palabra = palabra.lower()
    palabra = palabra.replace(' ', '')

    # Reemplazo de tildes
    palabra = palabra.replace("á", "a")
    palabra = palabra.replace("é", "e")
    palabra = palabra.replace("í", "i")
    palabra = palabra.replace("ó", "o")
    palabra = palabra.replace("ú", "u")

    # Comparación desde los extremos hacia el centro
    a = 0
    b = len(palabra) - 1

    for i in range(len(palabra) // 2):  # solo hasta la mitad, sino sigue
        if palabra[a] != palabra[b]:
            return False
        a += 1
        b -= 1

    return True


# Bloque principal
palabra = input("Ingrese una palabra o frase: ")
if es_palindromo(palabra):
    print("Es un palíndromo")
else:
    print("No es un palíndromo")

print("\n")
print("\n")
print("----Version 3-----")
# version con lista
print("\n")


def es_palindromo_lista(palabra):
    # Normalizar: minúsculas, sin espacios ni tildes un poco mas corto de codigo
    palabra = palabra.lower().replace(" ", "")
    palabra = palabra.replace("á", "a").replace("é", "e").replace("í", "i")
    palabra = palabra.replace("ó", "o").replace("ú", "u")

    # Convertir a lista de caracteres
    lista_letras = list(palabra)

    # Comparar con la lista invertida
    if lista_letras == lista_letras[::-1]:  # compara el espejo
        return True
    else:
        return False


texto = input("Ingrese una palabra o frase: ")
if es_palindromo_lista(texto):
    print("Es un palíndromo (usando listas)")
else:
    print("No es un palíndromo")
print("\n")
print("\n")
print("-------Version 4 ----------")
print("\n")
# importo numpy
import numpy as np


def es_palindromo_array(palabra):  # quitar tildes y mayusculas
    palabra = palabra.lower().replace(" ", "")
    palabra = palabra.replace("á", "a").replace("é", "e").replace("í", "i")
    palabra = palabra.replace("ó", "o").replace("ú", "u")

    # Convertir a array de caracteres
    array_letras = np.array(list(palabra))  # version con array son mas utiles con operaciones largas

    # Comparar con el array invertido
    if np.array_equal(array_letras, array_letras[::-1]):  # si el array es igual al derecho y al reves
        return True
    else:
        return False


texto = input("Ingrese una palabra o frase: ")
if es_palindromo_array(texto):
    print("Es un palíndromo (usando arrays)")
else:
    print("No es un palíndromo")

# Version 5 con todo el enunciado
print("\n")
print("-------Version 5 con todo el enunciado ----------")
print("\n")
print(
    "Generar una lista con al menos 7 palabras y detectar cuantas de esas palabras son palíndromos y cuál es el palíndromo con más caracteres."
    )
lista_palabras = ["anilina", "erre", "radar", "rodador", "salas", "python", "reconocer", "arenera", "palindromo"]
print("Lista de palabras:", lista_palabras)
print("\n")


def sacartilde(parola):
    parola = parola.lower().replace(" ", "")
    reemplazos = {"á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u"}
    for original, reemplazo in reemplazos.items():
        parola = parola.replace(original, reemplazo)
    return parola


def un_palindroma(parola):
    parola_normale = sacartilde(parola)
    return parola_normale == parola_normale[::-1]


# Detectar palíndromos
ultimopalindromo = [p for p in lista_palabras if un_palindroma(p)]

print(f"La cantidad de palíndromos encontrados en la lista: {len(ultimopalindromo)}")
print("Son palíndromos de la lista:")
for p in ultimopalindromo:
    print(f"- {p}")


# Función para encontrar el palíndromo más largo
def palindromo_mas_largo(lista):
    elveres = [p for p in lista if un_palindroma(p)]
    if not elveres:
        return None
    return max(elveres, key=lambda x: len(sacartilde(x)))


resultado = palindromo_mas_largo(lista_palabras)
if resultado:
    print(
        f"\n El palíndromo más largo es: '{resultado}' con {len(sacartilde(resultado))} caracteres (sin espacios ni tildes)")
else:
    print(" No se encontraron palíndromos.")


######################################################################
# version de clase
# 1º crear la función que detecta si es palíndromo
def es_palindromo(palabra):
    return palabra == palabra[::-1]
def analizar_palindromos(lista):
    palindromos = []
    palindromo_mas_largo = ""   # inicializo variable para guardar el palindromo mas largo
    for palabra in lista:
        if es_palindromo(palabra):
            palindromos.append(palabra)
            if (len(palabra) > len(palindromo_mas_largo)):  # si la palabra actual es mas larga que la guardada
                palindromo_mas_largo = palabra
    cantidad_palindromos = len(palindromos)
    return palindromos



# Ejercicio 5
# Implementar un programa que permita al usuario ingresar tres valores: 
# valorInicial, valorFinal y salto. En base a esos tres valores, mostrar la lista de 
# todos los números a partir de valorInicial de salto en salto hasta valorFinal. 
# Resolver el ejercicio utilizando la estructura de control for y luego la estructura 
# de control while. Ejemplo: si valorInicial = 10, valorFinal = 30 y salto = 5, se 
# deberán mostrar los números “a partir de 10, de 5 en 5 hasta llegar a 20”, es 
# decir: 10, 15, 20, 25, 30. 

print("-------Ejercicio 5-------")
print("\n")
print("Generar una lista de numeros desde un valor inicial a un valor final con un salto determinado")

print("Ahora va a ingresar los 3 valores deseados")
valorInicial = int(input("Ingrese el valor inicial: "))
valorFinal = int(input("Ingrese el valor final: "))
salto = int(input("Ingrese el salto: "))

# Convertir los valores en una lista
parametros_ejercicio5 = [valorInicial, valorFinal, salto]
print(f"Parámetros ingresados: {parametros_ejercicio5}")  # para ver si pude crear bien la lista
print("\nOpción de ejercicio con for")


# Función que genera la secuencia
def salta_con_for(parametros):
    inicio, fin, paso = parametros  # Python tomo valorInicial=inicio, valorFinal=fin, salto=paso, por el orden en que fueron ingresados
    resultado_con_for = []
    for x in range(inicio, fin + 1, paso):  # fin +1 es el limite superior
        resultado_con_for.append(x)  # guarda en x como variable en la iteracion
    return resultado_con_for


# Mostrar el resultado
secuencia = salta_con_for(parametros_ejercicio5)
print(f"Los valores entre {valorInicial} y {valorFinal}, saltando de {salto} en {salto}, son:")
print(secuencia)

print("\nOpción de ejercicio con while")
print("Ahora va a ingresar los 3 valores deseados")
valorInicial = int(input("Ingrese el valor inicial: "))
valorFinal = int(input("Ingrese el valor final: "))
salto = int(input("Ingrese el salto: "))

# Convertir los valores en una lista
parametros_ejercicio5 = [valorInicial, valorFinal, salto]
print(f"Parámetros ingresados: {parametros_ejercicio5}")
print("\n Opción de ejercicio con while")


def salta_con_while(parametros):
    inicio, fin, paso = parametros  #
    resultado_con_while = []  # guardo en una lista los resultaso para iterar
    indice_while = inicio  # inicializo la funcion en el valor inicial quepone el usuario

    while indice_while <= fin:  # se hace hasta llegar al valor final elegido por el usuario
        resultado_con_while.append(indice_while)  # agrego a la lista el valor actual de indice_while
        indice_while += paso  # incremento el valor de indice_while en el salto elegido por el usuario

    return resultado_con_while


# Mostrar resultado
secuencia = salta_con_while(parametros_ejercicio5)
print(f" Los valores entre {valorInicial} y {valorFinal}, saltando de {salto} en {salto}, son:")
print(secuencia)

print("\n")
print("-------Ejercicio 6-------")
# Ejercicio 6
# Implementar un programa que permita ingresar valores enteros positivos. El
# ingreso termina cuando el usuario no desee ingresar más valores, para lo cual
# se deberá definir un criterio que indique esta decisión. Luego deberá calcular y
# mostrar el promedio, la cantidad de valores ingresados, el mayor y menor valor.

print("Calcular promedio, cantidad de valores, mayor y menor valor de una lista de numeros enteros positivos")

print("\n")
print(
    "A continuacion, podra ingresar varios numeros. La condicion es que deben ser enteros positivos (desde el 1, sin comas). Cuando no desee ingresar mas numeros escriba la palabra fin")
print()
print("---version usando operador sum")
num_ejer6 = []  # Creo lista vacía para calcular promedio con suma

while True:
    n_ej6 = input("Ingrese un número. Si desea terminar, escriba 'Fin': ")

    if n_ej6.lower() == "fin":  # Ignora mayúsculas/minúsculas
        break
        print(" Ingreso finalizado.")

    if n_ej6.isdigit():  # Verifica si es un número entero positivo
        numero = int(n_ej6)
        num_ejer6.append(numero)  # Agrega el número a la lista
        promio_sum = sum(num_ejer6) / len(num_ejer6)

    else:
        print("Por favor, ingrese un número entero positivo o escriba 'Fin' para salir.\n")
print(f"Lista completa de números: {num_ejer6}")
print(f"el promedio total: {promio_sum}")

print("\n")
print("\n")
print("---- Version usando acumulador-----")

num_ejer6_acuCont = []  # Creo lista vacía

print("Ingrese números enteros positivos. Escriba 'Fin' para terminar.")

while True:
    n_ej6 = input("Ingrese un número (o 'Fin' para salir): ")

    if n_ej6.lower() == "fin":
        print("Ingreso finalizado.\n")
        break

    if n_ej6.isdigit():
        numero = int(n_ej6)
        num_ejer6_acuCont.append(numero)
        print(f"Números ingresados hasta ahora: {num_ejer6_acuCont}\n")
    else:
        print("Entrada inválida. Ingrese un número entero positivo o 'Fin'.\n")

# Calcular promedio con acumulador y contador manual
if num_ejer6_acuCont:
    suma_acu = 0
    contador = 0
    for pr_acu in num_ejer6_acuCont:
        suma_acu += pr_acu
        contador += 1
    promedio_con = suma_acu / contador

    print(f"Lista completa de números: {num_ejer6_acuCont}")
    print(f"Promedio calculado manualmente: {promedio_con}")
else:
    print("No se ingresaron números. No se puede calcular el promedio.")

# Ejercicio 7
# a) Crear una lista que contenga valores enteros desde 3 a 12 incluidos. Utilizar 
# el identificador listaNumeros. 
# b) Indicar el resultado de las siguientes operaciones realizadas sobre la lista 
# del inciso anterior:  
# i) x = len(listaNumeros)  
# ii) x = listaNumeros[3]  
# iii) x = listaNumeros[:3]  
# iv) x = listaNumeros[3:]  
# v) x = listaNumeros[3:6]  
# vi) x = listaNumeros[1:8:2]  
# vii) x = listaNumeros[-1]  
# viii) x = listaNumeros[-6:-2]  
# ix) x = listaNumeros[ : : -1]

print("Crear una lista de nuemros enteros de 3 a 12 que los incluya")
listaNumeros = list(range(2, 14))
print(f"la lista es {listaNumeros}")
print("Punto i. Cantidad de elementos de la lista")
a=len(listaNumeros)
print(f"Rta {a}")
print("\n")
print("Punto ii. Numero en ubicacion 3")
b=listaNumeros[3]
print(f"Rta {b}")
print("\n")
print("Punto iii. Indexación por corte (o slicing) antes")
c=listaNumeros[:3]
print(c)
print("\n")
print("Punto iv. Indexacion por corte o slicing despues ")
d=listaNumeros[3:]
print(d)
print("\n")
print("Punto v. Indexacion entre 3 y 6")
e=listaNumeros[3:6]
print(e)
print("\n")
print("Punto vi. Indexacion con inicio, fin y paso")
f=listaNumeros[1:8:2]
print(f)
print("\n")
print("Punto vi. Quitar el ultimo elemento de la lista")
g=listaNumeros[-1]
print(g)
print("\n")
print("Punto vii. Indice negativos, cuenta desde el ultimo al primero. Aca 6to indice desde el ultimo y frena en el 2")
print("lista = [ 2,  3,  4,  5,  6,  7,  8,  9,  10,  11,  12,  13]")
print("indice=   0   1   2   3   4   5   6   7    8    9   10   11  ")
print("indNeg= -12 -11 -10  -9  -8  -7  -6  -5   -4   -3   -2   -1 ")
h= listaNumeros[-6:-2]
print(h)
print("\n")
print("Punto viii. Indice Invertido")
i=listaNumeros[ : : -1]
print(i)
print("\n")


# Ejercicio 8 
# a) Implementar una función que permita extraer la última cifra de un número 
# entero positivo (es decir, la cifra de unidad).  
# b) Implementar una función que permita extraer todas las cifras excepto la 
# última de un número entero positivo (es decir, todas menos la cifra de unidad).  
# c) Implementar una función que devuelva la cantidad de cifras que contiene un 
# número entero positivo. 
print("-------Ejercicio 8-------")
print("\n")
print("Funciones para extraer cifras de un número entero positivo")

pto8 = [2, 4, 9, -1, 3, -2, -9, 10, -3]
print(f"La lista de donde extraer el último número entero positivo es: {pto8}")

def ent_positivo():
    indexar = len(pto8) - 1  # De ultimo indece

    while indexar >= 0:
        if pto8[indexar] > 0:  # valor es entero positivo
            print(f"Último número entero positivo encontrado: {pto8[indexar]}")
            break
        indexar -= 1

ent_positivo()
print("\n")
print("Función para extraer todas las cifras excepto la última de un número entero positivo")

ultimo_positivo = ent_positivo()

def menos_ent_positivo():
    nueva_lista = pto8.copy()  # Copiamos la lista para no modificar la original
    if ultimo_positivo is not None:
        nueva_lista.remove(ultimo_positivo)  # Elimina la primera aparición del número
    return nueva_lista

# Ejecutamos la función y mostramos el resultado
rta8b = menos_ent_positivo()

print(f"Lista sin el último entero positivo: {rta8b}")

# Ejercicio 9 
# a) Implementar una función contieneCifra(numero, cifra), que devuelva un valor 
# booleano indicando si la cifra aparece en el numero dado. 
# b) Implementar una función contarCifra(numero, cifra), que devuelva la 
# cantidad de veces que aparece la cifra en el número. 
# Ejemplos: 
# a = contieneCifra(1810, 8) # True, porque 1810 contiene al menos un 8 
# b = contarCifra(1810, 1) # 2, porque 1810 contiene dos unos.



# Ejercicio 10
# a) Implementar una función de devuelva el mayor de dos números reales.
# b) Utilizando la solución del inciso anterior, implementar una función que
# devuelva el mayor de tres números reales.

print("-------Ejercicio 10-------")
print("\n")
print("Funciones para devolver el mayor de dos o tres números reales")


def leer_num_reales():
    num1 = float(input("Ingrese el primer número real: "))
    num2 = float(input("Ingrese el segundo número real: "))

    if num1 > num2:
        return num1
    else:
        return num2


# Llamada a la función y almacenamiento del resultado
ejercicio10 = leer_num_reales()
print(f"El número mayor es {ejercicio10}")

## Error en la parte b
# def leer_num_reales():
#     num1 = float(input("Ingrese el primer número real: "))
#     num2 = float(input("Ingrese el segundo número real: "))
    
#     if num1 > num2:
#         return num1
#     else:
#         return num2

# # Llamada a la función y almacenamiento del resultado
# ejercicio10 = leer_num_reales()
# print(f"El número mayor es {ejercicio10}")

# print("parte b: usar el punto a y compararlo con un tercer numero")

# def tercer_num():
#   num3 = float(input("Ingrese el tercer numero"))

#     if num3>ejercicio10():
#       return True
#     else:
#       False
# ptobej10 = tercer_num
# print(f"El mayor de todos es {ptobej10}")

# Parte A: Leer dos números reales y devolver el mayor
def leer_num_reales():
    num1 = float(input("Ingrese el primer número real: "))
    num2 = float(input("Ingrese el segundo número real: "))

    if num1 > num2:
        return num1
    else:
        return num2


# Guardamos el resultado de la comparación
ejercicio10 = leer_num_reales()
print(f"El número mayor entre los dos primeros es: {ejercicio10}")


# Parte B: Comparar ese número con un tercer número
def tercer_num(mayor_anterior):
    num3 = float(input("Ingrese el tercer número real: "))

    if num3 > mayor_anterior:
        return num3
    else:
        return mayor_anterior


# Llamamos a la función pasando el resultado anterior
ptobej10 = tercer_num(ejercicio10)
print(f"El mayor de todos los números ingresados es: {ptobej10}")