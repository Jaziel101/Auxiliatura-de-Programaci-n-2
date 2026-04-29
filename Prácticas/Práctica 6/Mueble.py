class Mueble:
    def __init__(self, tipo, material):
        self._tipo = tipo
        self._material = material

    @property
    def tipo(self):
        return self._tipo

    @property
    def material(self):
        return self._material

    def mostrar_info(self):
        print(f"    Mueble: {self._tipo} | Material: {self._material}")

    def __str__(self):
        return f"{self._tipo} ({self._material})"