'''
Ejercicio 3: Crear un rango de 3 a 10 pero con incremento de 2 en 2, en lugar de 1 en 1
Ejemplo de ejecucion: 3,5,7,9
'''
# Ejercicio 1: Iterar un rango de 0 a 10 e imprimir numeros divisibles entre 3


# Ejemplo de ejecucion: 0,3,6,9}

print('Rango de 0 a 10 con numeros divisibles entre 3')
for i in range(11):
    if i % 3 == 0:
        print(i)

# Ejercicio 2: Crear un rango de numeros de 2 a 6 a imprimelos
# Ejemplo de ejecucion: 2,3,4,5,6

print('Rango de 2 a 6')
for i in range(2,7):
    print(i)

# Dada la siguiente tupla 
tupla = (13, 1, 8, 3, 2, 5, 8) # Definimos la tupla
# Crear una lista que solo incluya los numeros menores a 5 e imprima por consola [1, 3, 2]

Lista = []
for nuevaLista in tupla:
    if nuevaLista < 5:
        Lista.append(nuevaLista)

print(Lista)