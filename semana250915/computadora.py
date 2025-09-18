from monitor import Monitor
from teclado import Teclado
from mouse import Mouse

class Computadora:
    def __init__(self, procesador: str, memoriaRAM: int, discoRigido: int,
                 monitor: Monitor, teclado: Teclado, mouse: Mouse):
        self._procesador = procesador
        self._memoriaRAM = memoriaRAM
        self._discoRigido = discoRigido
        self._monitor = monitor
        self._teclado = teclado
        self._mouse = mouse

    # Métodos de consulta (getters)
    def getProcesador(self):
        return self._procesador

    def getMemoriaRAM(self):
        return self._memoriaRAM

    def getDiscoRigido(self):
        return self._discoRigido

    def getMonitor(self):
        return self._monitor.get_info()

    def getTeclado(self):
        return self._teclado.get_info()

    def getMouse(self):
        return self._mouse.get_info()

    # Métodos de modificación (setters)
    def setProcesador(self, procesador: str):
        self._procesador = procesador

    def setMemoriaRAM(self, memoriaRAM: int):
        self._memoriaRAM = memoriaRAM

    def setDiscoRigido(self, discoRigido: int):
        self._discoRigido = discoRigido

    def setMonitor(self, monitor: Monitor):
        self._monitor = monitor

    def setTeclado(self, teclado: Teclado):
        self._teclado = teclado

    def setMouse(self, mouse: Mouse):
        self._mouse = mouse