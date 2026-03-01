#Primera clase
class Anime:
    def __init__(self, nombre, genero, nroEpisodios):
        #Publico
        self.nombre = nombre
        self.genero = genero
        #Privado
        self.__nroEpisodios = nroEpisodios
        self.__episodios = []

    def agregar_episodio(self, episodio):
        self.__episodios.append(episodio)

    def __str__(self):
        return f"Anime: {self.nombre}, Género: {self.genero}, Episodios: {self.__nroEpisodios}"
#Segunda clase
class Televisor:
    def __init__(self, marca=None, resolucion=None, tipo=None):
        #Privado
        self.__marca = marca
        self.__resolucion = resolucion
        self.__tipo = tipo

    def __str__(self):
        return f"Televisor Marca: {self.__marca}, Resolución: {self.__resolucion}, Tipo: {self.__tipo}"
#Tercera clase
class Instrumento:
    def __init__(self, nombre, material, tipo):
        #Publico
        self.nombre = nombre
        #Privado
        self.__material = material
        self.__tipo = tipo

    def __str__(self):
        return f"Instrumento: {self.nombre}, Material: {self.__material}, Tipo: {self.__tipo}"
#Clase principal
if __name__ == "__main__":

    anime1 = Anime("Boku no Hero", "Acción", 174)
    anime2 = Anime("Kimi no Koto ga Dai Dai Dai Dai Daisuki na 100-nin no Kanojo", "Romance", 24)

    tv1 = Televisor("Samsung", 1080, "OLED")
    tv2 = Televisor("LG", 4000, "IPS")

    instrumento1 = Instrumento("Guitarra", "Madera", "Cuerda")
    instrumento2 = Instrumento("Flauta", "Metal", "Aire")

    print(anime1)
    print(anime2)
    print(tv1)
    print(tv2)
    print(instrumento1)
    print(instrumento2)