from Mueble import Mueble

class Habitacion:
    MAX_MUEBLES = 100

    def __init__(self, nombre, tamano):
        self._nombre = nombre
        self._tamano = tamano
        self._cant_muebles = 0
        self._muebles = []

    @property
    def nombre(self):
        return self._nombre

    @property
    def tamano(self):
        return self._tamano

    @property
    def cant_muebles(self):
        return self._cant_muebles

    def agregar_mueble(self, mueble):
        if self._cant_muebles < self.MAX_MUEBLES:
            self._muebles.append(mueble)
            self._cant_muebles += 1
            return True
        return False

    def mostrar_muebles(self):
        if self._cant_muebles == 0:
            print("    No hay muebles en esta habitación")
        else:
            for mueble in self._muebles:
                mueble.mostrar_info()

    def mostrar_info(self):
        print(f"  Habitación: {self._nombre} | Tamaño: {self._tamano}m² | Muebles: {self._cant_muebles}")

    def __str__(self):
        return f"{self._nombre} ({self._tamano}m², {self._cant_muebles} muebles)"