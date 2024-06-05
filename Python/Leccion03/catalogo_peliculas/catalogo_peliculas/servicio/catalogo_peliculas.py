import os

class CatalogoPeliculas:

    ruta_archivo = "paliculas.txt"

    @classmethod
    def agregar_pelicula(cls, pelicula):
        with open(cls.ruta_archivo, "a", encoding= "utf8") as archivo:
            archivo.read(f"{pelicula.nombre}\n")

    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta_archivo, "r", encoding="utf8") as archivo:
            print("Catalogo de películas".center(50, "-"))
            print(archivo.read())

    @classmethod
    def eliminar_peliculas(cls):
        os.remove(cls.ruta_archivo)
        print(f"ARCHIVO ELIMINADO: {cls.ruta_archivo}")