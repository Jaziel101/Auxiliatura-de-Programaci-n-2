from Perro import Perro
from Gato import Gato

class CentroVeterinario:
    MAX_ANIMALES = 100

    def __init__(self, nombre):
        self._nombre = nombre
        self._perros = []
        self._gatos = []

    @property
    def nombre(self):
        return self._nombre

    def agregar_perro(self, perro):
        if len(self._perros) < self.MAX_ANIMALES:
            self._perros.append(perro)
            print(f"Perro '{perro.nombre}' agregado al centro {self._nombre}")
            return True
        print(f"No hay espacio para más perros en {self._nombre}")
        return False

    def agregar_gato(self, gato):
        if len(self._gatos) < self.MAX_ANIMALES:
            self._gatos.append(gato)
            print(f"Gato '{gato.nombre}' agregado al centro {self._nombre}")
            return True
        print(f"No hay espacio para más gatos en {self._nombre}")
        return False

    def ordenar_perros(self):
        """Ordena perros por edad ascendente, luego nombre dueño, luego nombre perro"""
        self._perros.sort(key=lambda p: (p.edad, p.nombre_dueno, p.nombre))
        print(f"Perros ordenados en {self._nombre}")

    def ordenar_gatos(self):
        """Ordena gatos: primero los que toman leche, luego edad descendente, luego nombre ascendente"""
        self._gatos.sort(key=lambda g: (not g.toma_leche, -g.edad, g.nombre))
        print(f"Gatos ordenados en {self._nombre}")

    def verificar_animales_mismo_dueno(self):
        """Verifica si hay dueños con múltiples animales en el centro"""
        conteo = {}
        
        for perro in self._perros:
            dueno = perro.nombre_dueno
            conteo[dueno] = conteo.get(dueno, 0) + 1
        
        for gato in self._gatos:
            dueno = gato.nombre_dueno
            conteo[dueno] = conteo.get(dueno, 0) + 1
        
        print(f"\n=== ANIMALES POR DUEÑO EN {self._nombre.upper()} ===")
        hay_duplicados = False
        for dueno, cantidad in conteo.items():
            if cantidad >= 2:
                print(f"Dueño: {dueno} tiene {cantidad} animales.")
                hay_duplicados = True
        
        if not hay_duplicados:
            print("No hay dueños con múltiples animales.")

    def mostrar_perros(self):
        print(f"\n=== PERROS EN {self._nombre.upper()} ===")
        if not self._perros:
            print("  No hay perros registrados.")
        else:
            for perro in self._perros:
                perro.mostrar_info()
        print(f"Total: {len(self._perros)} perro(s)")

    def mostrar_gatos(self):
        print(f"\n=== GATOS EN {self._nombre.upper()} ===")
        if not self._gatos:
            print("  No hay gatos registrados.")
        else:
            for gato in self._gatos:
                gato.mostrar_info()
        print(f"Total: {len(self._gatos)} gato(s)")

    def mostrar_todos(self):
        self.mostrar_perros()
        self.mostrar_gatos()