class Monitor:
    def __init__(self, marca, tamaño, tipo_pantalla, conexiones):
        self.marca = marca
        self.tamaño = tamaño
        self.tipo_pantalla = tipo_pantalla
        self.conexiones = conexiones  # lista de conexiones: ["HDMI", "VGA"]

    def mostrar_info(self):
        return f"Monitor {self.marca}, {self.tamaño} pulgadas, {self.tipo_pantalla}, conexiones: {', '.join(self.conexiones)}"

    def agregar_conexion(self, nueva_conexion):
        if nueva_conexion not in self.conexiones:
            self.conexiones.append(nueva_conexion)


class Teclado:
    def __init__(self, marca, lenguaje, tiene_numerico, retroiluminado):
        self.marca = marca
        self.lenguaje = lenguaje
        self.tiene_numerico = tiene_numerico
        self.retroiluminado = retroiluminado

    def mostrar_info(self):
        numerico = "con teclado numérico" if self.tiene_numerico else "sin teclado numérico"
        retro = "con retroiluminación" if self.retroiluminado else "sin retroiluminación"
        return f"Teclado {self.marca}, lenguaje {self.lenguaje}, {numerico}, {retro}"

    def cambiar_lenguaje(self, nuevo_lenguaje):
        self.lenguaje = nuevo_lenguaje


class Mouse:
    def __init__(self, marca, inalambrico, dpi):
        self.marca = marca
        self.inalambrico = inalambrico
        self.dpi = dpi

    def mostrar_info(self):
        tipo = "inalámbrico" if self.inalambrico else "con cable"
        return f"Mouse {self.marca}, {tipo}, {self.dpi} DPI"

    def cambiar_dpi(self, nuevo_dpi):
        self.dpi = nuevo_dpi
