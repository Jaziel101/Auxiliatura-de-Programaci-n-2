from CentroVeterinario import CentroVeterinario
from Perro import Perro
from Gato import Gato

def main():
    centro1 = CentroVeterinario("Centro Veterinario La Paz")
    centro2 = CentroVeterinario("Centro Veterinario El Alto")

    print("=== REGISTRO DE ANIMALES ===\n")

    print("--- Centro 1 ---")
    
    p1 = Perro("Max", 5, "Juan Perez", True, True)
    p2 = Perro("Luna", 3, "Maria Gomez", False, False)
    p3 = Perro("Rocky", 3, "Maria Gomez", True, True)  
    
    centro1.agregar_perro(p1)
    centro1.agregar_perro(p2)
    centro1.agregar_perro(p3)
    
    g1 = Gato("Misi", 4, "Juan Perez", True, True)
    g2 = Gato("Garfield", 7, "Laura Fernandez", False, True)
    g3 = Gato("Tom", 2, "Carlos Lopez", True, False)
    
    centro1.agregar_gato(g1)
    centro1.agregar_gato(g2)
    centro1.agregar_gato(g3)
    
    print("\n--- Centro 2 ---")
    
    p4 = Perro("Bobby", 8, "Ana Condori", True, False)
    p5 = Perro("Rex", 4, "Pedro Mamani", False, True)
    p6 = Perro("Rex", 4, "Pedro Mamani", False, True) 
    
    centro2.agregar_perro(p4)
    centro2.agregar_perro(p5)
    centro2.agregar_perro(p6)
    
    g4 = Gato("Luna", 6, "Ana Condori", True, True)
    g5 = Gato("Simba", 3, "Roberto Quispe", False, True)
    g6 = Gato("Milo", 1, "Roberto Quispe", True, False)
    
    centro2.agregar_gato(g4)
    centro2.agregar_gato(g5)
    centro2.agregar_gato(g6)

    print("\n" + "="*60)
    print("ANTES DE ORDENAR")
    print("="*60)
    centro1.mostrar_todos()
    centro2.mostrar_todos()

    print("\n" + "="*60)
    print("ORDENANDO PERROS (Edad ↑, Dueño ↑, Nombre ↑)")
    print("="*60)
    centro1.ordenar_perros()
    centro2.ordenar_perros()
    centro1.mostrar_perros()
    centro2.mostrar_perros()

    print("\n" + "="*60)
    print("ORDENANDO GATOS (Toma leche primero, Edad ↓, Nombre ↑)")
    print("="*60)
    centro1.ordenar_gatos()
    centro2.ordenar_gatos()
    centro1.mostrar_gatos()
    centro2.mostrar_gatos()

    print("\n" + "="*60)
    print("VERIFICANDO DUEÑOS CON MÚLTIPLES ANIMALES")
    print("="*60)
    centro1.verificar_animales_mismo_dueno()
    centro2.verificar_animales_mismo_dueno()

if __name__ == "__main__":
    main()