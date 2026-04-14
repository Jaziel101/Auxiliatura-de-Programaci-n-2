from abc import ABC, abstractmethod
import math
class Figura(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def obtenerArea(self):
        pass

    def mostrar(self):
        print(f"Color: {self.color}")
        print(f"Área: {self.obtenerArea():.2f}")
        print("------------------------")

class Cuadrado(Figura):
    def __init__(self, color, lado):
        super().__init__(color)
        self.lado = lado

    def obtenerArea(self):
        return self.lado ** 2

class Triangulo(Figura):
    def __init__(self, color, lado1, lado2, lado3):
        super().__init__(color)
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def obtenerArea(self):
        # Fórmula de Herón
        s = (self.lado1 + self.lado2 + self.lado3) / 2
        return math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))

class Redondo(Figura):
    def __init__(self, color, radio):
        super().__init__(color)
        self.radio = radio

    def obtenerArea(self):
        return math.pi * (self.radio ** 2)

c1 = Cuadrado("Rojo", 4)
c2 = Cuadrado("Azul", 6)

t1 = Triangulo("Verde", 3, 4, 5)
t2 = Triangulo("Amarillo", 5, 5, 6)

r1 = Redondo("Negro", 3)
r2 = Redondo("Blanco", 5)

print("=== CUADRADOS ===")
c1.mostrar()
c2.mostrar()

print("=== TRIÁNGULOS ===")
t1.mostrar()
t2.mostrar()

print("=== REDONDOS ===")
r1.mostrar()
r2.mostrar()

if c1.obtenerArea() > t1.obtenerArea():
    print(f"La figura con mayor área es el CUADRADO de color {c1.color}")
else:
    print(f"La figura con mayor área es el TRIÁNGULO de color {t1.color}")