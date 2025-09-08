from ejercicio1 import *

#Tele nueva en stock
print("Ejercicio de Television")
tele001 = Televisor(
    marca="Samsung",
    totalCanales=100,
    canalActual=1,
    volumen=30,
    encendido=False
)
print("La primera Tele: ")
print("Marca: ", tele001.get_marca())
print("Total de Canales: ", tele001.get_totalCanales())
print(" Canal Actual: "), tele001.get_canalActual()
print(" Volumen: ", tele001.get_volumen())
print("Encedido: ", tele001.get_encendido())

print("''''''''''''''''")
#prueba de 1 de los metodos set
tele001.set_totalCanales(120)
print("Total de canales modificado con set :", tele001.get_totalCanales())

#Cambiar de Canal
print("·················")
print("Cambio de canal")
print("canal siguiente")
print("canal actual: ", tele001.canalSiguiente())
#input(int("Ingrese en que numero de canal que se encuentra: ))
print("ir al canal anterior, pero primero subimos uno mas")
print("canal actual: ", tele001.canalSiguiente())
print("canal actual: ", tele001.canalAnterior())
print("················")

#Subir el volumen

print(("Ahora vamos a subir el volumen. Tapate los oidos"))
print("este es el volumen ahora: ", tele001.get_volumen())
print("Subiendo el volumen ....")
print("ahora el volumen està en : ", tele001.subirVolumen())
print("ahora lo pese muy alto. Ahora lo bajo")
print("bajando el volumen")
print("el volumen ahora es: ", tele001.bajarVolumen())


print("···············")

# vc Silenciar
print("ahora el silencio: ", tele001.silenciar())

print(" y si mejor apagamos? , ", tele001.apagar())
print("vuelvo a prender: ", tele001.encender())

print("·················")
print("busquemos un canal: ", tele001.cambiarCanal(314))
print("pasamos a otro canal: ", tele001.cambiarCanal(390))

