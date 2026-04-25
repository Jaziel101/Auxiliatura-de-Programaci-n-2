from Animal import Animal

class Gato(Animal):
    def __init__(self, nombre, edad, nombre_dueno, caza_ratones, toma_leche):
        super().__init__(nombre, edad, nombre_dueno)
        self._caza_ratones = caza_ratones
        self._toma_leche = toma_leche

    @property
    def caza_ratones(self):
        return self._caza_ratones

    @property
    def toma_leche(self):
        return self._toma_leche

    def mostrar_info(self):
        print(f"  Gato: {self._nombre} | Edad: {self._edad} | Dueño: {self._nombre_dueno} | "
              f"Caza ratones: {'Sí' if self._caza_ratones else 'No'} | "
              f"Toma leche: {'Sí' if self._toma_leche else 'No'}")