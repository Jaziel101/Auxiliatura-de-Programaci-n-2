from Habitacion import Habitacion
from Mueble import Mueble

class Departamento:
    MAX_HABITACIONES = 100

    def __init__(self, nro_puerta, nro_piso):
        self._nro_puerta = nro_puerta
        self._nro_piso = nro_piso
        self._nro_hab = 0
        self._habitaciones = []

    @property
    def nro_puerta(self):
        return self._nro_puerta

    @property
    def nro_piso(self):
        return self._nro_piso

    @property
    def nro_hab(self):
        return self._nro_hab

    @property
    def habitaciones(self):
        return self._habitaciones

    def agregar_habitacion(self, habitacion):
        if self._nro_hab < self.MAX_HABITACIONES:
            self._habitaciones.append(habitacion)
            self._nro_hab += 1
            return True
        return False

    def agregar_mueble_a_habitacion(self, nro_habitacion, mueble):
        if 0 <= nro_habitacion < self._nro_hab:
            return self._habitaciones[nro_habitacion].agregar_mueble(mueble)
        return False

    def agregar_mueble_por_nombre(self, nombre_habitacion, mueble):
        for hab in self._habitaciones:
            if hab.nombre == nombre_habitacion:
                return hab.agregar_mueble(mueble)
        return False

    def total_muebles(self):
        total = 0
        for hab in self._habitaciones:
            total += hab.cant_muebles
        return total

    def mostrar_habitaciones(self):
        print(f"  Departamento {self._nro_puerta} (Piso {self._nro_piso}) - {self._nro_hab} habitaciones:")
        for hab in self._habitaciones:
            hab.mostrar_info()

    def mostrar_info(self):
        print(f"\n--- DEPARTAMENTO ---")
        print(f"Número de puerta: {self._nro_puerta}")
        print(f"Piso: {self._nro_piso}")
        print(f"Cantidad de habitaciones: {self._nro_hab}")
        self.mostrar_habitaciones()

    def __str__(self):
        return f"Depto {self._nro_puerta} (Piso {self._nro_piso}, {self._nro_hab} habs)"