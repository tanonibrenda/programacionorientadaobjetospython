class Teclado:
    def __init__(self, marca: str, lenguaje: str, tecl_num: bool, retroiluminacion: bool):
        self._marca = marca
        self._lenguaje = lenguaje
        self._teclado_numerico = tecl_num
        self._retroiluminacion = retroiluminacion

    # Método de consulta general
    def get_info(self) -> str:
        num = "Sí" if self._teclado_numerico else "No"
        luz = "Sí" if self._retroiluminacion else "No"
        return f"Teclado: {self._marca}, {self._lenguaje}, Numérico: {num}, Retroiluminado: {luz}"

    # Método de modificación general
    def set_info(self, marca=None, lenguaje=None, tecl_num=None, retroiluminacion=None):
        if marca is not None:
            self._marca = marca
        if lenguaje is not None:
            self._lenguaje = lenguaje
        if tecl_num is not None:
            self._teclado_numerico = tecl_num
        if retroiluminacion is not None:
            self._retroiluminacion = retroiluminacion

    # Métodos individuales de consulta
    def get_marca(self) -> str:
        return self._marca

    def get_lenguaje(self) -> str:
        return self._lenguaje

    def tiene_teclado_numerico(self) -> bool:
        return self._teclado_numerico

    def tiene_retroiluminacion(self) -> bool:
        return self._retroiluminacion

    # Métodos individuales de modificación
    def set_marca(self, marca: str):
        self._marca = marca

    def set_lenguaje(self, lenguaje: str):
        self._lenguaje = lenguaje

    def set_teclado_numerico(self, tecl_num: bool):
        self._teclado_numerico = tecl_num

    def set_retroiluminacion(self, retroiluminacion: bool):
        self._retroiluminacion = retroiluminacion