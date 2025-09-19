class Auto():
    def __inti__(self, marca, modelo, potencia):
        self._marca = marca
        self._modelo = modelo
        self._capacidadDeTanqueMaxima = 40.0
        self._nivelDeCombustibleActual =10.0
        self._motor = Motor(potencia)

class Motor():
    def __init__(self, potencia):
        pass
    
def getMotor(self):
    return self._motor
def setMotor(self,nuevoMotor):
    self._motor = nuevoMotor

def getMarca(self):
    return self._marca
def setMarca(self,nuevoMarca):
    self._marca = nuevoMarca
def getModelo(self):
    return self._modelo
def setModelo(self,nuevoModelo):
    self._modelo = nuevoModelo


