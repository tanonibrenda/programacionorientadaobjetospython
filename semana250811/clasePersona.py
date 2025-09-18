class Persona():
    # constructor
    def __init__(self, edad, nombre, saldo = 0):
        self._edad = edad
        self._nombre = nombre
        self._saldo = saldo
        self._colorDeCabello = "Rojo"

    # metodos de consulta
    def getEdad(self):
        return self._edad

    def getNombre(self):
        return self._nombre

    def getSaldo(self):
        return self._saldo

    # metodos de modificacion
    def setEdad(self, nuevaEdad):
        self._edad = nuevaEdad

    def setNombre(self, nuevoNombre):
        self._nombre = nuevoNombre

    def setSaldo(self, nuevoSaldo):
        self._saldo = nuevoSaldo

    # metodos operacionales
    def cumplirAnios(self):
        self._edad = self._edad + 1

    def ingresarDinero(self, monto):
        self._saldo = self._saldo + monto

    def retirarDinero(self, monto):
        # si podemos retirar ese monto, es decir, si lo tenemos disponible
        if monto <= self._saldo :
            # que podamos retirar el dinero
            self._saldo = self._saldo - monto
            return True
        else:
            return False

print()