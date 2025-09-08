# Ejercicio 8 
# a) Implementar una función que permita extraer la última cifra de un número 
# entero positivo (es decir, la cifra de unidad).  
# b) Implementar una función que permita extraer todas las cifras excepto la 
# última de un número entero positivo (es decir, todas menos la cifra de unidad).  
# c) Implementar una función que devuelva la cantidad de cifras que contiene un 
# número entero positivo.

def contieneCifra():   #1º convertir el numero en cadena de caracteres
    numero_a_string = str(numero)       #con str converitimos el numero en string
    cifra_a_string = str(cifra)
    return cifra_a_string in numero_a_string   #in devuelve true o false si la cifra esta en el numero

def contarCifras(numero, cifra):
    numero_a_string = str(numero)
    cifra_a_string = str(cifra) 
    return numero_a_string.count(cifra_a_string)   #count cuenta cuantas veces aparece la cifra en el numero

# print(contieneCifra(123456, 5))   #True
print(contarCifras(1234556, 5))    #2



# Ejercicio 8

# a) Extraer la última cifra (unidad) de un número entero positivo
def ultima_cifra(numero):
    return numero % 10  # El módulo 10 devuelve la última cifra

# b) Extraer todas las cifras excepto la última
def sin_ultima_cifra(numero):
    return numero // 10  # La división entera elimina la última cifra

# c) Contar la cantidad de cifras que contiene un número entero positivo
def cantidad_cifras(numero):
    return len(str(numero))  # Convertimos a string y contamos los caracteres

# Extra: Verificar si una cifra está en el número
def contiene_cifra(numero, cifra):
    return str(cifra) in str(numero)

# Extra: Contar cuántas veces aparece una cifra en el número
def contar_cifra(numero, cifra):
    return str(numero).count(str(cifra))

# Pruebas
print("Última cifra de 123456:", ultima_cifra(123456))           # 6
print("Sin última cifra de 123456:", sin_ultima_cifra(123456))   # 12345
print("Cantidad de cifras en 123456:", cantidad_cifras(123456))  # 6
print("¿Contiene el número 123456 la cifra 5?:", contiene_cifra(123456, 5))  # True
print("¿Cuántas veces aparece la cifra 5 en 1234556?:", contar_cifra(1234556, 5))  # 2

# Ejercicio 12 
# a) Implementar una función que al pasarle dos valores (x,y) retorne un 
# diccionario con la siguiente estructura. 
#             p = {“x”: x, “y”: y} 
# emulando un punto P = (x,y). 
# b) Implementar una función que genere 10 puntos, como en el inciso anterior y 
# lo almacene en una lista. 
# c) Implementar una función que encuentre el o los puntos más cercanos al 
# origen

import random

def crear_punto(x, y):
    return {"x": x, "y": y}

def generar_puntos(cantidad=10):
    lista_puntos = []
    for i in range(cantidad):
        x = random.randint(-10, 10)
        y = random.randint(-10, 10)
        lista_puntos.append(crear_punto(x, y))
    return lista_puntos

puntos= generar_puntos()
print(puntos)   
exit()


#calcular la distancia al origen  ver teorema de pitagoras
def distancia_al_origen(punto):
    x = punto.get("x")
    y = punto.get("y")
    distancia = (x**2 + y**2)**0.5
    return distancia


distancia_min = distancia_al_origen(puntos[0])
for p in puntos:
    distancia = distancia_al_origen(p)
   