
# TEMA: Listas
# Tambien conocidas como arreglos o vectores.

# Sintaxis de range (inicio<opcional>, fin<requerido>,incremento <opcional>)

print("")
print("EJERCICIO N°1: Iterar un rango de 0 a 10 e imprimir numeros divisibles entre 3.")

# EJEMPLO DE SOLUCION: 0,3,6,9

for i in range(11):
    if i % 3 == 0:
        print(i)

print("")
print("EJERCICIO N°2: Crear un rango de numeros de 2 a 6 e imprimelos.")

# EJEMPLO DE SOLUCION: 2,3,4,5,6
# rango = rango (2,7) Asi lo hizo el profe

for i in range(2,7):
    if i:
        print(i)

print("")
print("EJERCICIO N°3: Crear un rango de 3 a 10 pero con incremento de 2 en 2.")

# EJEMPLO DE EJECUCION: 3,5,7,9

for i in range(3,10,2): #Se coloca el incremento en el tercer lugar :o
    if i:
        print(i)

#TEMA 2: TUPLAS

print('')
print('EJERCICIO N°4')

print("DADA LA SIGUIENTE TUPLA: TUPLA = (13,1,8,3,2,5,8) Definimos la tupla")
print("crear una lista que solo incluya los números menores al 5 e imprima por consola [1,2,3]")

tupla = (13, 1, 8, 3, 2, 5, 8)
print(tupla)

lista = list(tupla)

'''
for i in range(0,5):
    if i:
        print(i)
'''
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
        print(elemento)