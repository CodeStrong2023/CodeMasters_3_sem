import os

class catalogoPeliculas:

    ruta_archivos = "Peliculas.txt"

    @classmethod
    def agregar_peliculas(cls, pelicula):
        with open(cls.ruta_archivo, "a", encoding="utf8") as archivo:
            archivo.write(f"{pelicula.nombre}\n")

    @classmethod
    def listar_peliculasd(cls):
        with open(cls.ruta_archivos, "r", encoding="utf8") as archivo:
            print(f"Catalogo de peliculas".center(50,"-"))
            print(archivo.read())

    @classmethod
    def eliminar_pelicula(cls):
        os.remove(cls.ruta_archivos)
        print(f"Archivo eliminados: {cls.ruta_archivos}")