class Cliente:
    def __init__(self, mail: str, nombre: str, telefono: str):
        self._mail = mail
        self._nombre = nombre
        self._telefono = telefono

    # Getters

    def getMail(self):
        return self._mail
    def getNombre(self):
        return self._nombre
    def getTelefono(self):
        return self._telefono

    # Setters
    def setMail(self, nuevoMail):
        self._mail = nuevoMail
    def setNombre(self, nuevoNombre):
        self._nombre = nuevoNombre
    def setTelefono(self, nuevoTelefono):
        self._telefono = nuevoTelefono

    #print("debug de cliente")