from monitor import Monitor
from teclado import Teclado
from mouse import Mouse
from computadora import Computadora

# Creamos Perifericos
monitor1 = Monitor("Dell", "24 pulgadas", "LED", "HDMI")
teclado1 = Teclado("Logitech", "Español", True, True)
mouse1 = Mouse("Razer", True, 16000)

# Creamos Computadora
computadora1 = Computadora("Intel i7", 16, 512, monitor1, teclado1, mouse1)
print("Información de la computadora:")
print(f"Procesador: {computadora1.getProcesador()}")    
print(f"Memoria RAM: {computadora1.getMemoriaRAM()} GB")
print(f"Disco Rígido: {computadora1.getDiscoRigido()} GB")
print(computadora1.getMonitor())

