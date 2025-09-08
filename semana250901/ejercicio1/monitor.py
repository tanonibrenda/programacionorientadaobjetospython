class Monitor:
    def __init__(self, marca, tamano, tipo_pant, conexion):             #Constructor
        #asignar valores a objetos
        self.marca = marca
        self.tamano = tamano
        self.tipo_pant = tipo_pant
        self.conexion = conexion

    # Metodo de consulta

    def getInfo_marca(self):
        return self.marca
    def setInfo_marca(self, marca):
        self.marca = marca
    def getInfo_tamano(self):
        return self.tamano
    def setInfo_tamano(self, tamano):
        self.tamano = tamano
    def getInfo_tipo_pant(self):
        return self.tipo_pant
    def setInfo_tipo_pant(self, tipo_pant):
        self.tipo_pant = tipo_pant
    def getInfo_conexion(self):
        return self.conexion
    def setInfo_conexion(self, conexion):
        self.conexion = conexion