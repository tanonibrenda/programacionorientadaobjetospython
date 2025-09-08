from pruebasAuto import Auto
class PruebasAuto():
    def __init__(self):
        self.auto1 = Auto("Toyota", "Corolla")
        self.auto2 = Auto("Honda", "Civic")

    def mostrarDetalles(self):
        print(f"Auto 1: Marca: {self.auto1._marca}, Modelo: {self.auto1._modelo}, Capacidad de Tanque: {self.auto1.getCapacidadDeTanque()} litros")
        print(f"Auto 2: Marca: {self.auto2._marca}, Modelo: {self.auto2._modelo}, Capacidad de Tanque: {self.auto2.getCapacidadDeTanque()} litros")

    def modificarCapacidad(self, auto, nueva_capacidad):
        auto.setCapacidadDeTanque(nueva_capacidad)
    
    print("Detalles iniciales de los autos:")
    print(mostrarDetalles())