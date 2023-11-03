# Ejercicio 1:
# Llenar una lista con los numeros del 1 al 50, luego muestra
# la lista con el bucle for, los elementos deben mostrarse
# de la suiguente forma:
# 1-2-3-4-5...-50

#lista = []
#i = 1
#while i <=50:
#    lista.append(i)
#    i += 1
lista = list(range(1, 51)) #Algoritmo eficas, en 5 lineas
for i in lista:
    print(i,end='-')