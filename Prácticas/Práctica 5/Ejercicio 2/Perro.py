from Animal import Animal

class Perro(Animal):
    def __init__(self, nombre, edad, nombre_dueno, requiere_bosal, ladra_fuerte):
        super().__init__(nombre, edad, nombre_dueno)
        self._requiere_bosal = requiere_bosal
        self._ladra_fuerte = ladra_fuerte

    @property
    def requiere_bosal(self):
        return self._requiere_bosal

    @property
    def ladra_fuerte(self):
        return self._ladra_fuerte

    def mostrar_info(self):
        print(f"  Perro: {self._nombre} | Edad: {self._edad} | Dueño: {self._nombre_dueno} | "
              f"Requiere bozal: {'Sí' if self._requiere_bosal else 'No'} | "
              f"Ladra fuerte: {'Sí' if self._ladra_fuerte else 'No'}")