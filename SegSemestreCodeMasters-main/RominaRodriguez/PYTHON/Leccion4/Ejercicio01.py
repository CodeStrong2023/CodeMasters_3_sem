# Ejercicio 1: Llenar una lista
# Llenear una lista con los número del 1 al 50, luego mostrar
# la lista con el bucle for, los elementos deben mostrarse de la
# siguente forma:
#1-2-3-4....-50
#lista = []
#i = 1
#while i <= 50:
#    lista.append(i)
#    i += 1
lista = list(range(1,51))# Algorítmo eficas
for i in lista:
    print(i, end='-')