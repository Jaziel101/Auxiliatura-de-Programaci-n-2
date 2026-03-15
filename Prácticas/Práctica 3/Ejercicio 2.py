class Aula:

    def __init__(self, nombre_aula, piso, estudiantes):
        self.nombre_aula = nombre_aula
        self.piso = piso
        self.estudiantes = estudiantes

    def mostrar(self, opcion=None):

        if opcion is None:

            print("\nNombre del aula:", self.nombre_aula)
            print("Piso:", self.piso)

            print("\nLista de estudiantes:")
            for e in self.estudiantes:
                print(e[0], "-", e[1])

        elif opcion == "estado":

            print("\nEstado de estudiantes:")

            for e in self.estudiantes:

                nombre = e[0]
                nota = e[1]

                if nota >= 51:
                    estado = "APROBADO"
                else:
                    estado = "REPROBADO"

                print(nombre, "-", nota, "-", estado)

print("\n CREAR AULA ")

nombre_aula = input("Ingrese nombre del aula: ")
piso = int(input("Ingrese el piso: "))

n = int(input("Cantidad de estudiantes: "))

estudiantes = []

for i in range(n):

    print("\nEstudiante", i+1)

    nombre = input("Nombre: ")
    nota = int(input("Nota sobre 100: "))

    estudiantes.append([nombre, nota])

aula1 = Aula(nombre_aula, piso, estudiantes)

aula1.mostrar()

aula1.mostrar("estado")
