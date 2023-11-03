# Ejercicio 1: Eliminar duplicados de una lista
# Escriba un programa donde tenga una lista y que a continuacion
# Elimine los elementos repetidos, por ultimo mostrar la lista.

#Creamos una lista
lista = [1, 2, 3, "Leti", 7, 7, 3, "Juli", 1, "Mati", 2, "Juli"]
#conjunto = set(lista)
#print(conjunto) #Convertimos la lista a un conjunto de tipo set (se eliminan  las repeticiones)
#lista = list(conjunto) #Convertimos el conjunto a una lista
lista = list(set(lista)) #convercion hecha en una sola linea de codigo (eficiente)
print(lista)
