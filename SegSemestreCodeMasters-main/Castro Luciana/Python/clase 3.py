
# TEMA: tipo SET o conjuntos y Diccionario

# EJERCICIO Nº4 CLASE3

# La tarea consiste en ingresar elementos al diccionario llamado seleccionArgentina, lo elementos a ingresar deben ser como mínimo 4.
# Estos elementos son los jugadores con su número de camiseta, nombre, apellido, edad, altura, precio y posición de juego, por supuesto ver el video anterior.

print("")
diccionario3 = {
    10: {'Jugador':'Lionel Messi', 'Edad': 36, 'Altura': '1.70', 'Precio': '50.000.000', 'Posicion': 'Delantero'},
    11: {'Jugador':'Angel Di Maria', 'Edad': 35, 'Altura': '1.78', 'Precio': '15.000.000', 'Posicion': 'Delantero'},
    9: {'Jugador':'Lautaro Martinez', 'Edad': 26, 'Altura': '1.74', 'Precio': '80.000.000', 'Posicion': 'Delantero'},
    23: {'Jugador':'Dibu Martines', 'Edad': 31, 'Altura': '1.95', 'Precio': '17.000.000', 'Posicion': 'Arquero'},
    24: {'Jugador':'Paulo Dybala', 'Edad': 28, 'Altura': '1.77', 'Precio': '35.000.000', 'Posicion': 'Media Punta'},
    19: {'Jugador':'Nicolas Otamendi', 'Edad': 34, 'Altura': '1.83', 'Precio': '3.500.000', 'Posicion': 'Defensa Central'},
    7: {'Jugador':'Rodrigo De Paul', 'Edad': 29, 'Altura': '1.80', 'Precio': '40.000.000', 'Posicion': 'Centrocampista'},
    27: {'Jugador':'Julian Alvarez', 'Edad': 23, 'Altura': '1.70', 'Precio': '60.000.000', 'Posicion': 'Delantero'}
}

for llave, valor in diccionario3.items():
    print(llave, valor)

print("")
print('Este diccionario posee un total de:', end=' ')
print(len(diccionario3), 'jugadores.')
