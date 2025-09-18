class Monitor:
    def __init__(self, marca: str, tamano: str, tipo_pantalla: str, conexion: str):
        self._marca = marca
        self._tamano = tamano
        self._tipo_pantalla = tipo_pantalla
        self._conexion = conexion

    # Método de consulta general
    def get_info(self) -> str:
        return f"Monitor: {self._marca}, {self._tamano}, {self._tipo_pantalla}, Conexión: {self._conexion}"

    # Método de modificación general
    def set_info(self, marca=None, tamano=None, tipo_pantalla=None, conexion=None):
        if marca is not None:
            self._marca = marca
        if tamano is not None:
            self._tamano = tamano
        if tipo_pantalla is not None:
            self._tipo_pantalla = tipo_pantalla
        if conexion is not None:
            self._conexion = conexion

    # Métodos individuales de consulta
    def get_marca(self) -> str:
        return self._marca

    def get_tamano(self) -> str:
        return self._tamano

    def get_tipo_pantalla(self) -> str:
        return self._tipo_pantalla

    def get_conexion(self) -> str:
        return self._conexion

    # Métodos individuales de modificación
    def set_marca(self, marca: str):
        self._marca = marca

    def set_tamano(self, tamano: str):
        self._tamano = tamano

    def set_tipo_pantalla(self, tipo_pantalla: str):
        self._tipo_pantalla = tipo_pantalla

    def set_conexion(self, conexion: str):
        self._conexion = conexion