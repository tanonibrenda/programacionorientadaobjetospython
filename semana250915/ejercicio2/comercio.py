from cliente import Cliente


class Comercio:
    def __init__(self, nombre: str, rubro: str, ventas: float): #No agregar todavia la list de clientes
        self._nombre = nombre
        self._rubro = rubro
        self._ventas = ventas
        self._clientes = [] # lista vacia

    # Getters

    def getNombre(self):
        return self._nombre
    def getRubro(self):
        return self._rubro
    def getVentas(self):
        return self._ventas
    def getListaClientes(self):
        return self._clientes

    # Setters

    def setNombre(self, nuevoNombre: str):
        self._nombre = nuevoNombre
    def setRubro(self, nuevoRubro: str):
        self._rubro = nuevoRubro
    def setVentas(self, nuevaVenta: float):
        self._ventas = nuevaVenta

