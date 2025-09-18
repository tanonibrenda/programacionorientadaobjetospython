class Mouse:
    def __init__(self, marca: str, inalambrico: bool, DPI: int):
        self._marca = marca
        self._inalambrico = inalambrico
        self._DPI = DPI

    # Método de consulta general
    def get_info(self) -> str:
        tipo = "Inalámbrico" if self._inalambrico else "Con cable"
        return f"Mouse: {self._marca}, {tipo}, DPI: {self._DPI}"

    # Método de modificación general
    def set_info(self, marca=None, inalambrico=None, DPI=None):
        if marca is not None:
            self._marca = marca
        if inalambrico is not None:
            self._inalambrico = inalambrico
        if DPI is not None and DPI > 0:
            self._DPI = DPI

    # Métodos individuales de consulta
    def get_marca(self) -> str:
        return self._marca

    def es_inalambrico(self) -> bool:
        return self._inalambrico

    def get_DPI(self) -> int:
        return self._DPI

    # Métodos individuales de modificación
    def set_marca(self, marca: str):
        self._marca = marca

    def set_inalambrico(self, inalambrico: bool):
        self._inalambrico = inalambrico

    def set_DPI(self, DPI: int):
        if DPI > 0:
            self._DPI = DPI