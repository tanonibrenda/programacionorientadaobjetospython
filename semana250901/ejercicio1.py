# Ejercicio 1 
# Realizar la implementación de las siguientes clases, incluyendo los métodos de 
# consulta y modificación. Dibujar el diagrama de clases correspondiente. 
# a) Clase Monitor, que contenga información de su marca, tamaño, tipo de 
# pantalla (ej. LED, LCD) y tipos de conexión (ej. VGA, HDMI, ambas). 
# b) Clase Teclado, que contenga información de su marca, lenguaje, si incluye 
# teclado numérico y si tiene retroiluminación. 
# c) Clase Mouse, que contenga información de su marca, si es inalámbrico y los 
# DPI (puntos por pulgada).

#creacion clase monitor
class Monitor:
    def __init__(self, marca, tamano, tipo_pant, conexion):             #Constructor
        #asignar valores a objetos
        self.marca = marca
        self.tamano = tamano
        self.tipo_pant = tipo_pant
        self.conexion = conexion

    # Metodo de consulta
    def get_info(self):
        return f"Monitor: {self.marca}, {self.tamano}, {self.tipo_pant}, Conexión: {self.conexion}"
        #devuelve str con los atributos cargados

    # Metodo para modificar, con opcion NONE, para que solo se modifiquen los parametros que uno quiere
    def set_info(self, marca=None, tamano=None, tipo_pant=None, conexion=None):
        if marca: self.marca = marca
        if tamano: self.tamano = tamano
        if tipo_pant: self.tipo_pant = tipo_pant
        if conexion: self.conexion = conexion

## Metodos individuales de consulta y modificacion para cada atributo. Es la mejor practica, para despues modificar sin problemas.

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

#creacion clase teclado
class Teclado:
    def __init__(self, marca, lenguaje, tecl_num, retroiluminacion):   #Constructor
        # asignar valores a objetos
        self.marca = marca
        self.lenguaje = lenguaje
        self.tecl_num = tecl_num
        self.retroiluminacion = retroiluminacion

    #Metodo de consulta
    def get_info(self):
        num = "Sí" if self.tecl_num else "No"
        luz = "Sí" if self.retroiluminacion else "No"
        return f"Teclado: {self.marca}, {self.lenguaje}, Numérico: {num}, Retroiluminado: {luz}"
        # Metodo de consulta

    # Metodo para modificar, con opcion NONE, para que solo se modifiquen los parametros que uno quiere
    def set_info(self, marca=None, lenguaje=None, tecl_num=None, retroiluminacion=None):
        if marca: self.marca = marca
        if lenguaje: self.lenguaje = lenguaje
        if tecl_num is not None: self.tecl_num = tecl_num
        if retroiluminacion is not None: self.retroiluminacion = retroiluminacion

#creacion clase Mouse
class Mouse:
    def __init__(self, marca, inalambrico, DPI):                     #Constructor
        # asignar valores a objetos
        self.marca = marca
        self.inalambrico = inalambrico
        self.DPI = DPI

    # Metodo de consulta
    def get_info(self):
        tipo = "Inalámbrico" if self.inalambrico else "Con cable"
        return f"Mouse: {self.marca}, {tipo}, DPI: {self.DPI}"
        # Metodo de consulta

    #Metodo para modificar, con opcion NONE, para que solo se modifiquen los parametros que uno quiere
    def set_info(self, marca=None, inalambrico=None, DPI=None):
        if marca: self.marca = marca
        if inalambrico is not None: self.inalambrico = inalambrico
        if DPI is not None and DPI > 0: self.DPI = DPI