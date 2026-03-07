class ServidorMinecraft:

    def __init__(self, capacidad=10):
        self.capacidad = capacidad
        self.jugadores = {}

    def agregar_jugador(self, nombre, diamantes):
        if len(self.jugadores) < self.capacidad:
            self.jugadores[nombre] = diamantes
            print("Jugador agregado correctamente.")
        else:
            print("El servidor está lleno.")

    def verificar_stacks(self):
        print("\nStacks de diamantes por jugador:")
        for nombre, diamantes in self.jugadores.items():
            stacks = diamantes // 64
            print(nombre, "tiene", stacks, "stack(s)")

    def jugador_con_mas_diamantes(self):
        jugador = max(self.jugadores, key=self.jugadores.get)
        print("\nJugador con más diamantes:", jugador)

    def total_diamantes(self):
        total = sum(self.jugadores.values())
        print("\nTotal de diamantes:", total)

servidor = ServidorMinecraft()

cantidad = int(input("¿Cuántos jugadores quieres agregar?: "))

for i in range(cantidad):
    nombre = input("Nombre del jugador: ")
    diamantes = int(input("Cantidad de diamantes: "))
    servidor.agregar_jugador(nombre, diamantes)

servidor.verificar_stacks()
servidor.jugador_con_mas_diamantes()
servidor.total_diamantes()