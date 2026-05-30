import re

class SueldoInvalidoException(Exception):
    pass

class CargoInvalidoException(Exception):
    pass

class Empleado:
    def __init__(self, nombre, cargo, sueldo):
        self.nombre = nombre
        self.cargo = cargo
        self.sueldo = sueldo
    
    def mostrar_info(self):
        print(f"  {self.nombre} | Cargo: {self.cargo} | Sueldo: Bs. {self.sueldo:.2f}")


class Empresa:
    SALARIO_MINIMO = 2500
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []  
    
    def registrar_empleado(self):
        print("\n REGISTRO DE NUEVO EMPLEADO")
        
        nombre = input("Nombre: ").strip()
        
        cargo = self._ingresar_cargo_valido()
        
        sueldo = self._ingresar_sueldo_valido()
        
        empleado = Empleado(nombre, cargo, sueldo)
        self.empleados.append(empleado)
        print(f"\n Empleado '{nombre}' registrado exitosamente.\n")
    
    def _ingresar_cargo_valido(self):
        while True:
            try:
                cargo = input("Cargo: ").strip()
                if not cargo:
                    print(" El cargo no puede estar vacío. Intente nuevamente.\n")
                    continue
                
                # Verificar si el cargo contiene números
                if re.search(r'\d', cargo):
                    raise CargoInvalidoException("El cargo no puede contener números.")
                
                return cargo
                
            except CargoInvalidoException as e:
                print(f" Error: {e}")
                print("   Por favor, ingrese un cargo válido (solo letras, espacios y símbolos permitidos).\n")
    
    def _ingresar_sueldo_valido(self):
        while True:
            try:
                sueldo_input = input("Sueldo (Bs.): ").strip()
                
                try:
                    sueldo = float(sueldo_input)
                except ValueError:
                    print(" Error: Debe ingresar un valor numérico.\n")
                    continue
                
                if sueldo < self.SALARIO_MINIMO:
                    raise SueldoInvalidoException(
                        f"El sueldo Bs. {sueldo:.2f} es menor al salario mínimo nacional (Bs. {self.SALARIO_MINIMO})."
                    )
                
                return sueldo
                
            except SueldoInvalidoException as e:
                print(f" {e}")
                print(f"   Se asignará automáticamente el salario mínimo de Bs. {self.SALARIO_MINIMO}.\n")
                return self.SALARIO_MINIMO
    
    def mostrar_empleados(self):
        print(f"\n{'='*50}")
        print(f"EMPLEADOS DE: {self.nombre}")
        print(f"{'='*50}")
        
        if not self.empleados:
            print("No hay empleados registrados.\n")
        else:
            for i, empleado in enumerate(self.empleados):
                print(f"[{i}] ", end="")
                empleado.mostrar_info()
        print()
    
    def mostrar_empleado_por_indice(self, indice):
        if 0 <= indice < len(self.empleados):
            print("\n EMPLEADO ENCONTRADO")
            self.empleados[indice].mostrar_info()
        else:
            print(f" No existe empleado con índice {indice}")
    
    def total_empleados(self):
        return len(self.empleados)
    
    def nomina_total(self):
        total = sum(e.sueldo for e in self.empleados)
        print(f" Nómina total de '{self.nombre}': Bs. {total:.2f}")
        return total


def main():
    print("  SISTEMA DE RECURSOS HUMANOS")
    
    nombre_empresa = input("\nNombre de la empresa: ").strip()
    empresa = Empresa(nombre_empresa)
    
    while True:
        print("\n" + "="*40)
        print("   MENÚ PRINCIPAL")
        print("="*40)
        print("1. Registrar nuevo empleado")
        print("2. Mostrar todos los empleados")
        print("3. Buscar empleado por índice")
        print("4. Mostrar nómina total")
        print("5. Salir")
        
        opcion = input("\nSeleccione una opción: ").strip()
        
        if opcion == "1":
            empresa.registrar_empleado()
        elif opcion == "2":
            empresa.mostrar_empleados()
        elif opcion == "3":
            if empresa.total_empleados() == 0:
                print("No hay empleados registrados aún.")
            else:
                try:
                    indice = int(input("Ingrese el índice del empleado: "))
                    empresa.mostrar_empleado_por_indice(indice)
                except ValueError:
                    print("Debe ingresar un número válido.")
        elif opcion == "4":
            empresa.nomina_total()
        elif opcion == "5":
            print(f"\n Saliendo del sistema. Total de empleados registrados: {empresa.total_empleados()}")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()