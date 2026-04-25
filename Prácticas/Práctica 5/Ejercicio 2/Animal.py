from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nombre, edad, nombre_dueno):
        self._nombre = nombre
        self._edad = edad
        self._nombre_dueno = nombre_dueno

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        self._edad = valor

    @property
    def nombre_dueno(self):
        return self._nombre_dueno

    @nombre_dueno.setter
    def nombre_dueno(self, valor):
        self._nombre_dueno = valor

    @abstractmethod
    def mostrar_info(self):
        pass