class Persona:
    def __init__(self, nombre, carnet, edad):
        self.nombre = nombre
        self.carnet = carnet
        self.edad = edad

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Carnet: {self.carnet}")
        print(f"Edad: {self.edad}")

class Estudiante(Persona):
    def __init__(self, nombre, carnet, edad, matricula, carrera):
        super().__init__(nombre, carnet, edad)
        self.matricula = matricula
        self.carrera = carrera

    def mostrar(self):
        super().mostrar()
        print(f"Matrícula: {self.matricula}")
        print(f"Carrera: {self.carrera}")
        print("------------------------")

    def misma_carrera(self, otro):
        return self.carrera == otro.carrera

class Docente(Persona):
    def __init__(self, nombre, carnet, edad, antiguedad, sueldo):
        super().__init__(nombre, carnet, edad)
        self.antiguedad = antiguedad
        self.sueldo = sueldo

    def mostrar(self):
        super().mostrar()
        print(f"Antigüedad: {self.antiguedad}")
        print(f"Sueldo: {self.sueldo}")
        print("------------------------")

est1 = Estudiante("Juan", 123, 20, 1001, "Sistemas")
est2 = Estudiante("Maria", 456, 25, 1002, "Industrial")
doc = Docente("Carlos", 789, 25, 10, 5000)

print("=== ESTUDIANTE 1 ===")
est1.mostrar()

print("=== ESTUDIANTE 2 ===")
est2.mostrar()

print("=== DOCENTE ===")
doc.mostrar()

if est1.edad == doc.edad:
    print("Juan tiene la misma edad que el docente")

if est2.edad == doc.edad:
    print("Maria tiene la misma edad que el docente")

if est1.misma_carrera(est2):
    print("Están en la misma carrera")
else:
    print("No están en la misma carrera")