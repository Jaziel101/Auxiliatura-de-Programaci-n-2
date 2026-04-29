from Parqueo import Parqueo
from Departamento import Departamento
from Habitacion import Habitacion
from Mueble import Mueble

class Edificio:
    MAX_DEPARTAMENTOS = 100

    def __init__(self, nombre, superficie):
        self._nombre = nombre
        self._superficie = superficie
        self._cant_dep = 0
        self._departamentos = []
        self._parqueo = None

    @property
    def nombre(self):
        return self._nombre

    @property
    def superficie(self):
        return self._superficie

    @property
    def cant_dep(self):
        return self._cant_dep

    @property
    def departamentos(self):
        return self._departamentos

    def agregar_parqueo(self, parqueo):
        self._parqueo = parqueo
        print(f"Parqueo agregado al edificio {self._nombre}")

    def agregar_departamento(self, departamento):
        if self._cant_dep < self.MAX_DEPARTAMENTOS:
            self._departamentos.append(departamento)
            self._cant_dep += 1
            print(f"Departamento {departamento.nro_puerta} (Piso {departamento.nro_piso}) agregado")
            return True
        return False

    def mostrar_departamentos_por_piso(self, piso):
        print(f"\n=== DEPARTAMENTOS DEL PISO {piso} ===")
        encontrados = []
        for dep in self._departamentos:
            if dep.nro_piso == piso:
                dep.mostrar_info()
                encontrados.append(dep)
        if not encontrados:
            print(f"No hay departamentos en el piso {piso}")
        return encontrados

    def departamento_mas_habitaciones_por_piso(self, piso):
        mejor_dep = None
        max_hab = -1
        for dep in self._departamentos:
            if dep.nro_piso == piso:
                if dep.nro_hab > max_hab:
                    max_hab = dep.nro_hab
                    mejor_dep = dep
        if mejor_dep:
            print(f"\n=== DEPARTAMENTO CON MÁS HABITACIONES DEL PISO {piso} ===")
            mejor_dep.mostrar_info()
            return mejor_dep
        print(f"No hay departamentos en el piso {piso}")
        return None

    def agregar_mueble_a_departamento(self, piso, nro_puerta, habitacion_nombre, mueble):
        for dep in self._departamentos:
            if dep.nro_piso == piso and dep.nro_puerta == nro_puerta:
                if dep.agregar_mueble_por_nombre(habitacion_nombre, mueble):
                    print(f"Mueble '{mueble.tipo}' agregado al Depto {nro_puerta} (Piso {piso}) en habitación {habitacion_nombre}")
                    return True
                else:
                    print(f"No se encontró la habitación '{habitacion_nombre}'")
                    return False
        print(f"No se encontró el departamento {nro_puerta} en el piso {piso}")
        return False

    def departamentos_con_mas_muebles(self):
        if not self._departamentos:
            print("No hay departamentos en el edificio")
            return []
        
        max_muebles = max(dep.total_muebles() for dep in self._departamentos)
        
        print(f"\n=== DEPARTAMENTOS CON MÁS MUEBLES ({max_muebles} muebles) ===")
        mejores = []
        for dep in self._departamentos:
            if dep.total_muebles() == max_muebles:
                print(f"\n--- {dep} ---")
                dep.mostrar_habitaciones()
                mejores.append(dep)
        return mejores

    def habitacion_con_mas_muebles_por_piso(self, piso):
        mejor_hab = None
        max_muebles = -1
        mejor_dep = None
        
        for dep in self._departamentos:
            if dep.nro_piso == piso:
                for hab in dep.habitaciones:
                    if hab.cant_muebles > max_muebles:
                        max_muebles = hab.cant_muebles
                        mejor_hab = hab
                        mejor_dep = dep
        
        if mejor_hab:
            print(f"\n=== HABITACIÓN CON MÁS MUEBLES DEL PISO {piso} ===")
            print(f"Departamento: {mejor_dep.nro_puerta}")
            mejor_hab.mostrar_info()
            return mejor_hab.nombre
        print(f"No hay habitaciones en el piso {piso}")
        return None

    def es_primo(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def eliminar_departamentos_habitaciones_primas(self):
        eliminados = []
        nuevos_deps = []
        
        for dep in self._departamentos:
            if self.es_primo(dep.nro_hab):
                eliminados.append(dep)
                print(f"Eliminado: Departamento {dep.nro_puerta} (Piso {dep.nro_piso}) con {dep.nro_hab} habitaciones")
            else:
                nuevos_deps.append(dep)
        
        self._departamentos = nuevos_deps
        self._cant_dep = len(nuevos_deps)
        
        print(f"\nSe eliminaron {len(eliminados)} departamentos")
        return eliminados

    def mostrar_info(self):
        print(f"\n=== EDIFICIO: {self._nombre} ===")
        print(f"Superficie: {self._superficie}m²")
        print(f"Total departamentos: {self._cant_dep}")
        if self._parqueo:
            self._parqueo.mostrar_info()
        else:
            print("\n--- PARQUEO: No asignado ---")
        print("\n--- DEPARTAMENTOS ---")
        for dep in self._departamentos:
            print(f"  - Departamento {dep.nro_puerta} (Piso {dep.nro_piso}) | Habitaciones: {dep.nro_hab} | Total muebles: {dep.total_muebles()}")