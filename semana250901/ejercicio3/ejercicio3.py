# Ejercicio 3 
# Realizar una implementación de la clase Encomienda, que contenga 
# información de su remitente, destinatario, peso, dimensiones y costo. Incluir 
# todos los comandos de consulta y modificación de atributos. Dibujar el 
# diagrama de clases correspondiente. 
# Incorporar los atributos y métodos que considere necesario para modelar el 
# estado del envío (ej. Despachado, en viaje, visita a domicilio, recibido, 
# rechazado, etc).

class Encomienda():
    def __init__(self, remitente, destinatario, peso, dimension, costo):
        self.remitente = remitente
        self.destinatario = destinatario
        self.peso = peso    
        self.dimension = dimension
        self.costo = costo
        
    def despachado(self):
        return "Encomienda despachada"
    
    def en_viaje(self):
        return "Encomienda en viaje"
    
    def recibido(self):
        return "Encomienda recibida"
    
    def rechazado(self):
        return "Encomienda rechazada"
    
    def __str__(self):
        return f"Encomienda de {self.remitente} a {self.destinatario}, peso: {self.peso}kg, dimensión: {self.dimension}, costo: ${self.costo}"
        

