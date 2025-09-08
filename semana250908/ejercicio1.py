#Ejercicio
#Implementar la clase Televisor, en base a las siguientes condiciones:
#1) Debe incluir los atributos de marca (String), totalCanales (entero),
#canalActual (entero), volumen (entero de 0 a 100), encendido (booleano).
#2) Debe incluir los comandos de consulta de todos los atributos de consulta.
#3) Debe incluir todos los comandos de modificación de marca, totalCanales y
#canalActual.
#4) Implementar los siguientes métodos:
# a) canalSiguiente(): para avanzar al próximo canal (simula la tecla CH+).
# b) canalAnterior(): para retroceder al canal anterior (simula la tecla CH-).
# c) subirVolumen(): para incrementar el volumen (simula la tecla V+).
# d) bajarVolumen(): para bajar el volumen (simula la tecla V-).
# e) silenciar(): para silenciar el volumen (simula la tecla MUTE).
# f) apagar(): para apagar el televisor (simula la tecla OFF).
# g) encender(): para encender el televisor (simula la tecla ON).
#5) Realizar el diagrama UML.
#6) Realizar una propuesta para incorporar el método canalPrevio(), que
#permitirá regresar al canal visto anteriormente. Incorporar los atributos y/o
#métodos adicionales que crea necesarios.

class Televisor:
    def __init__(self, marca, totalCanales, canalActual, volumen, encendido):
        self.marca = marca
        self.totalCanales = totalCanales
        self.canalActual = 1    #lo inicializamos en canal 1
        self.volumen = 30
        self.encendido = False  #la idea es que te dan la tele apagada

  #metodos GET = metodo consulta

    def get_marca(self):
        return self.marca
    def get_totalCanales(self):
        return self.totalCanales
    def get_canalActual(self):
        return self.canalActual
    def get_volumen(self):
        return self.volumen
    def get_encendido(self):
        return self.encendido

    #metodo set = metodo modificacion
    def set_marca(self, newMarca):
        self.marca = newMarca
    def set_totalCanales(self, newTotalCanales):
        self.totalCanales = newTotalCanales
    def set_canalActual(self, newCanalActual):
        self.canalActual = newCanalActual
    def set_volumen(self,newVolumen):
        self.volumen = newVolumen

    # Desde acà los mètodos operacionales
    #Metodo para pasar al canal Siguiente

    def canalSiguiente(self):
        #while self.canalActual < self.totalCanales:
        #   self.canalActual += 1
        #    break
        #else:
        #    self.canalActual = 1

        if self.canalActual < self.totalCanales:
            self.canalActual += 1
        else:
            self.canalActual = 1
        return self.canalActual

    def canalAnterior(self):
        if self.canalActual < self.totalCanales:
            self.canalActual -= 1
        else:
            self.canalActual = 1
        return self.canalActual

    def subirVolumen(self):
        nuevo_volumen = self.get_volumen() + 20
        return nuevo_volumen

    def bajarVolumen(self):
        volumenBajo = self.subirVolumen() - 10
        return volumenBajo

    def silenciar(self):
        self.volumen = 0

    def apagar(self):
        self.encendido = True

    def encender(self):
        self.encendido = False

    def cambiarCanal(self, nuevo_canal):
        self.canalAnterior = self.canalActual
        self.canalActual = nuevo_canal
        print(f"Cambiando al canal {nuevo_canal}")

    def canalPrevio(self):
        if self.canalAnterior is not None:
            print(f"Volviendo al canal anterior: {self.canalAnterior}")
            self.canalActual, self.canalAnterior = self.canalAnterior, self.canalActual
        else:
            print("No hay canal anterior registrado.")
