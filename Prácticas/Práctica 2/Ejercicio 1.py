class Bus:

    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.pasajeros = 0
        self.costo_pasaje = 1.50

    def subir_pasajeros(self, cantidad):
        if self.pasajeros + cantidad <= self.capacidad:
            self.pasajeros += cantidad
            print("Subieron", cantidad, "pasajeros.")
        else:
            print("No hay suficientes asientos disponibles.")

    def cobrar_pasaje(self):
        total = self.pasajeros * self.costo_pasaje
        print("Total recaudado: Bs.", total)

    def asientos_disponibles(self):
        disponibles = self.capacidad - self.pasajeros
        print("Asientos disponibles:", disponibles)

bus1 = Bus(30)  

bus1.subir_pasajeros(12)

bus1.cobrar_pasaje()

bus1.asientos_disponibles()