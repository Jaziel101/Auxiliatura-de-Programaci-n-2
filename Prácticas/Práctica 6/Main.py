from Edificio import Edificio
from Parqueo import Parqueo
from Departamento import Departamento
from Habitacion import Habitacion
from Mueble import Mueble

def main():
    print("="*60)
    print("a. CREANDO EDIFICIO Y AGREGANDO PARQUEO")
    print("="*60)
    
    edificio = Edificio("Torre Central", 2500.0)
    parqueo = Parqueo(capacidad=50, precio_hora=5.0)
    edificio.agregar_parqueo(parqueo)
    
    parqueo.ingresar_auto("ABC-123")
    parqueo.ingresar_auto("XYZ-789")
    
    print("\n--- CREANDO DEPARTAMENTOS ---")
    
    dep1 = Departamento(101, 1)
    hab1_1 = Habitacion("Sala", 25.0)
    hab1_2 = Habitacion("Cocina", 12.0)
    hab1_3 = Habitacion("Dormitorio", 18.0)
    hab1_4 = Habitacion("Baño", 5.0)
    
    dep1.agregar_habitacion(hab1_1)
    dep1.agregar_habitacion(hab1_2)
    dep1.agregar_habitacion(hab1_3)
    dep1.agregar_habitacion(hab1_4)
    
    hab1_1.agregar_mueble(Mueble("Sofá", "Tela"))
    hab1_1.agregar_mueble(Mueble("Mesa", "Madera"))
    hab1_2.agregar_mueble(Mueble("Refrigerador", "Acero"))
    hab1_3.agregar_mueble(Mueble("Cama", "Madera"))
    
    dep2 = Departamento(102, 1)
    hab2_1 = Habitacion("Sala", 30.0)
    hab2_2 = Habitacion("Cocina", 15.0)
    hab2_3 = Habitacion("Dormitorio Principal", 20.0)
    hab2_4 = Habitacion("Dormitorio Secundario", 12.0)
    hab2_5 = Habitacion("Baño", 6.0)
    
    dep2.agregar_habitacion(hab2_1)
    dep2.agregar_habitacion(hab2_2)
    dep2.agregar_habitacion(hab2_3)
    dep2.agregar_habitacion(hab2_4)
    dep2.agregar_habitacion(hab2_5)
    
    hab2_1.agregar_mueble(Mueble("Sofá", "Cuero"))
    hab2_1.agregar_mueble(Mueble("Mesa Centro", "Vidrio"))
    hab2_1.agregar_mueble(Mueble("Lámpara", "Metal"))
    hab2_3.agregar_mueble(Mueble("Cama King", "Madera"))
    hab2_4.agregar_mueble(Mueble("Cama Individual", "Madera"))
    
    dep3 = Departamento(201, 2)
    hab3_1 = Habitacion("Sala", 28.0)
    hab3_2 = Habitacion("Cocina", 14.0)
    hab3_3 = Habitacion("Dormitorio", 16.0)
    
    dep3.agregar_habitacion(hab3_1)
    dep3.agregar_habitacion(hab3_2)
    dep3.agregar_habitacion(hab3_3)
    
    hab3_1.agregar_mueble(Mueble("Sofá", "Tela"))
    hab3_1.agregar_mueble(Mueble("Mesa", "Madera"))
    
    dep4 = Departamento(202, 2)
    hab4_1 = Habitacion("Sala Comedor", 35.0)
    hab4_2 = Habitacion("Cocina", 10.0)
    hab4_3 = Habitacion("Dormitorio", 15.0)
    hab4_4 = Habitacion("Estudio", 12.0)
    
    dep4.agregar_habitacion(hab4_1)
    dep4.agregar_habitacion(hab4_2)
    dep4.agregar_habitacion(hab4_3)
    dep4.agregar_habitacion(hab4_4)
    
    hab4_1.agregar_mueble(Mueble("Sofá Esquinero", "Tela"))
    hab4_1.agregar_mueble(Mueble("Mesa", "Madera"))
    hab4_3.agregar_mueble(Mueble("Cama", "Madera"))
    hab4_4.agregar_mueble(Mueble("Escritorio", "Metal"))
    hab4_4.agregar_mueble(Mueble("Silla", "Plástico"))
    
    edificio.agregar_departamento(dep1)
    edificio.agregar_departamento(dep2)
    edificio.agregar_departamento(dep3)
    edificio.agregar_departamento(dep4)
    
    edificio.mostrar_info()
    
    print("\n" + "="*60)
    print("b. DEPARTAMENTO CON MÁS HABITACIONES DEL PISO 1")
    print("="*60)
    edificio.departamento_mas_habitaciones_por_piso(1)
    
    print("\n" + "="*60)
    print("c. AGREGANDO MUEBLE AL DEPARTAMENTO 202 (PISO 2) EN HABITACIÓN 'Sala Comedor'")
    print("="*60)
    nuevo_mueble = Mueble("Biblioteca", "Madera")
    edificio.agregar_mueble_a_departamento(piso=2, nro_puerta=202, habitacion_nombre="Sala Comedor", mueble=nuevo_mueble)
    
    print("\n" + "="*60)
    print("d. DEPARTAMENTO(S) CON MÁS MUEBLES")
    print("="*60)
    edificio.departamentos_con_mas_muebles()
    
    print("\n" + "="*60)
    print("e. HABITACIÓN CON MÁS MUEBLES DEL PISO 2")
    print("="*60)
    edificio.habitacion_con_mas_muebles_por_piso(2)
    
    print("\n" + "="*60)
    print("f. ELIMINANDO DEPARTAMENTOS CON CANTIDAD PRIMA DE HABITACIONES")
    print("="*60)
    print("Cantidad de habitaciones por departamento:")
    for dep in edificio.departamentos:
        print(f"  - Depto {dep.nro_puerta} (Piso {dep.nro_piso}): {dep.nro_hab} habitaciones {'(PRIMO)' if edificio.es_primo(dep.nro_hab) else ''}")
    
    edificio.eliminar_departamentos_habitaciones_primas()
    
    print("\n" + "="*60)
    print("ESTADO FINAL DEL EDIFICIO")
    print("="*60)
    edificio.mostrar_info()

if __name__ == "__main__":
    main()