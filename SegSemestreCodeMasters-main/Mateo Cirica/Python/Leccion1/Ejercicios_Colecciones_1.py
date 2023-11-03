# Ejercicio 1: Eliminar duplicados de una lista
# Escriba un programa donde tenga una lista y que a continuacion
# elimine los elementos repetidos, por ultimo mostrar la lista.

# Creamos una lista

lista = [1, 2, 3, "Messi", 4, 4, 5, "Joaquin", 9, "Messi"]
# conjunto = set(lista)
# lista = list(conjunto)
lista =list(set(lista))
print(lista)