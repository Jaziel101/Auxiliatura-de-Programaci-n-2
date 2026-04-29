class Parqueo:
    def __init__(self, capacidad, precio_hora):
        self._capacidad = capacidad
        self._precio_hora = precio_hora
        self._cant_autos = 0
        self._placas = []

    @property
    def capacidad(self):
        return self._capacidad

    @property
    def precio_hora(self):
        return self._precio_hora

    @property
    def cant_autos(self):
        return self._cant_autos

    @property
    def espacios_disponibles(self):
        return self._capacidad - self._cant_autos

    def ingresar_auto(self, placa):
        if self._cant_autos < self._capacidad:
            self._placas.append(placa)
            self._cant_autos += 1
            print(f"Auto {placa} ingresó. Disponibles: {self.espacios_disponibles}")
            return True
        print(f"Parqueo lleno. No se puede ingresar {placa}")
        return False

    def retirar_auto(self, placa):
        if placa in self._placas:
            self._placas.remove(placa)
            self._cant_autos -= 1
            print(f"Auto {placa} retirado. Disponibles: {self.espacios_disponibles}")
            return True
        print(f"Auto {placa} no encontrado")
        return False

    def mostrar_info(self):
        print(f"\n--- PARQUEO ---")
        print(f"Capacidad: {self._capacidad}")
        print(f"Autos estacionados: {self._cant_autos}")
        print(f"Precio por hora: Bs. {self._precio_hora}")
        print(f"Placas: {', '.join(self._placas) if self._placas else 'Ninguno'}")