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
print(f"1. Su celular es el modelo " + modelo + " de la marca " + marca + " y tiene " + memoria + "G de RAM" )

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
print(f"5. Su celular es el modelo {celular['modelo']} de la marca {celular['marca']} y tiene {celular['memoria']}GB de RAM")

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


#importar modulo para ver si la contraseña tiene caracteres especiales
from string import punctuation

def validar_password1(password1):
    if len(password1)>=6: #mide si tiene mas de 6 caracteres
        if any ([pw.isdigit() for pw in password1]): # pide que vea si algun numero
            if any ([pw.islower() for pw in password1]): # Pide minuscula
                if any([pw.isupper() for pw in password1]): # Pide mayuscula
                    if any ([True if pw in punctuation else False for pw in password1]): # Pide caracter especial
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
      password1 = input("Ahora va a generar una contraseña, debe tener al menos 6 caracteres, una mayuscula, una minucula, un numero y un caracter especial.Ingrese su contraseña: ")
      validar_password1(password1)

print("Opcion 2 con no cumple las condiciones con elif")

#importar modulo para ver si la contraseña tiene caracteres especiales
from string import punctuation

def validar_password2(password2):
    if len(password2)<6: #mide si tiene mas de 6 caracteres
        print("La contraseña debe tener 6 o màs caracteres ")
    elif not any ([pww.isdigit() for pww in password2]):
        print("La contraseña debe tener al menos un numero")# pide que vea si algun numero
    elif any ([pww.islower() for pww in password2]): # Pide minuscula
        print("La contraseña debe contener al menos una minuscula")
    elif any([pww.isupper() for pww in password2]): # Pide mayuscula
        print("La contraseña debe contener al menos una mayuscula")
    elif any ([True if pww in punctuation else False for pww in password2]): # Pide caracter especial
        print("La contraseña debe contener algun caracter especial")
    else:
        print("Contraseña correcta")
        return True
    return False

if __name__ == "__main__":
      password2 = input("Ahora va a generar una contraseña,\n debe tener al menos 6 caracteres,\n una mayuscula, \nuna minucula, \nun numero y un caracter especial.\nIngrese su contraseña: ")
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
print("Definicion de palindromo de la Real Academia Española: \n Palabra o frase cuyas letras están dispuestas de tal manera que resulta la misma leída de izquierda a derecha que de derecha a izquierda; por ejemplo, anilina; dábale arroz a la zorra el abad.")
print("\n")
# ejemplos de palindromos: arenera, erre, ana, rodador, salas

print(" Version 1")
print("\n")
word = input("ingrese una palabra: ")

def palindromo(word):
    reverse = str(word).lower().replace(' ', ' '  )   #cadenas van a ser minuscula
    print(reverse, reverse[::-1])
    if reverse == reverse[::-1]: # [::-1] se invierte la cadena y quita los espacios vacios
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
print("Version 3")
#version con lista
print("\n")
def es_palindromo_lista(palabra):
    # Normalizar: minúsculas, sin espacios ni tildes un poco mas corto de codigo
    palabra = palabra.lower().replace(" ", "")
    palabra = palabra.replace("á", "a").replace("é", "e").replace("í", "i")
    palabra = palabra.replace("ó", "o").replace("ú", "u")

    # Convertir a lista de caracteres
    lista_letras = list(palabra)

    # Comparar con la lista invertida
    if lista_letras == lista_letras[::-1]:   #compara el espejo
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