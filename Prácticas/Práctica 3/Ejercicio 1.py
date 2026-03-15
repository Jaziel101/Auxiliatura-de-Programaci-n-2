class Videojuego:

    def __init__(self, nombre, plataforma, jugadores=1):
        self.nombre = nombre
        self.plataforma = plataforma
        self.jugadores = jugadores

    def agregarJugadores(self, cantidad=None):

        if cantidad is None:
            self.jugadores += 1
            print("Se agregó 1 jugador")

        else:
            self.jugadores += cantidad
            print("Se agregaron", cantidad, "jugadores")

    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Plataforma:", self.plataforma)
        print("Cantidad de jugadores:", self.jugadores)
        print("---------------------------")

print(" JUEGOS ")

v1 = Videojuego("Super Smash Bros Ultimate", "Nintendo Switch", 2)
v2 = Videojuego("Minecraft", "Playstation 4")

v1.mostrar()
v2.mostrar()

v1.agregarJugadores()

cantidad = int(input("Ingrese cantidad de jugadores a agregar: "))
v2.agregarJugadores(cantidad)

v1.mostrar()
v2.mostrar()
