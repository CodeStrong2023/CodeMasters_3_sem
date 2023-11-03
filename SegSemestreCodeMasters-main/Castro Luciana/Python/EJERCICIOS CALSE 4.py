
'''
EJERCICIO N°1

Escriba un programa donde tenga una lista y que a continuacion elimine los elementos repetidos,
por ultimo mostrar la lista.

'''

print('EJERCICIO N°1')
print('ELIMINAR ELEMENTOS DUPLICADOS DE UNA LISTA')

lista = [1,2,3,3,3, 'Lu', 1,5,6,5, 'Lucia', 'Nacho', 'Lu']
conjunto = set(lista) # El conjunto set no admite valores repetidos
lista = list(conjunto)
print(lista)
print(' ')

# asi lo hizo el profe:
# lista = list(set(lista)) la convercion esta hecha en una sola linea

'''
EJERCICIO N°2

Escriba un programa que tenga 2 listas y que a continuación cree las siguientes listas (No debe haber repetición)
1) Lista de palabras que aparecen en las listas.
2) Lista de palabras que aparecen en la primer lista, pero NO en la segunda.
3) Lista de palabras que aparecen en la segunda lista, pero NO en la primera.
4) Lista de palabras que aparecen en ambas listas.

'''

print('EJERCICIO N°2')
print('OPERACIONES DE CONJUNTOS CON LISTAS')

lista1 = [1, 2, 3, 4, 5, 5, 6, 7]
lista2 = [10, 9, 8, 8, 7, 6, 5, 4]
lista1 = (set(lista1))
lista2 = (set(lista2)) # Acá ya no hay repeticion de ningun dato

print('1) Lista de palabras que aparecen en las listas.')
lista3 = list(lista2 | lista1)
print(lista3)

print('2) Lista de palabras que aparecen en la primer lista, pero NO en la segunda.')
lista4 = list(lista1 - lista2)
print(lista4)

print('3) Lista de palabras que aparecen en la segunda lista, pero NO en la primera.')
lista5 = list(lista2 - lista1)
print(lista5)

print('4) Lista de palabras que aparecen en ambas listas.')
lista6 = list(lista1 & lista2)
print(lista6)
print(' ')

'''
EJERCICIO N°3

Escriba un programa donde cree una lista con los siguientes personajes del señor de los anillos.
NOMBRE: Aragon
CLASE:Guerrero
RAZA: Dunedain del Norte

NOMBRE: Gandalf
CLASE: Mago
RAZA: Istar

NOMBRE: Legolas
CLASE: Arquero
RAZA: Elfo Sindar

'''

print('EJERCICIO N°3')
print('AGREGAR PERSONAJES A UNA LISTA')

diccionario = {
    1: {'Nombre':'Aragon' ,'Clase': 'Guerrero' ,'Raza': 'Dunedain del Norte'},
    2: {'Nombre':'Gandalf','Clase':'Mago' ,'Raza':'Istar'},
    3: {'Nombre':'Legolas' ,'Clase':'Arquero' ,'Raza':'Elfo Sindar'}
}
for llave, valor in diccionario.items():
    print(llave, valor)
print('')

'''
EJERCICIO N°4

Llenar una lista con los números del 1 al 50, luego mostrar la lista con el bucle for,
los elementos deben mostrarse de la siguiente manera:
1-2-3-4-5...-50

'''

print('EJERCICIO N°4')
print('LLENAR UNA LISTA')
lista7 = []
i = 1
while i <= 50:
    lista7.append(i)
    i += 1
for i in lista7:
    print(i, end='-')
print(' ')

# OTRA FORMA:
# lista = list(range(1, 51))

print(' ')
print('EJERCICIO RAÍZ CUADRADA (SOLO PARA NÚMERO POSITIVO)')

import math #importamos la clase math para hacer uso de la funsion sqrt (raíz cuadrada)

num = int(input('Digite un número positivo: '))
while num < 0:
    print('Error -> Debe colocar un número positivo')
    num = int(input('Digite un número positivo: '))
print(f'Su raíz cuadrada es: {math.sqrt(num):.2f}') #2f se coloca para que no de mas de 2 dijitos luego de la coma

'''
EJERCICIO N°5
Llenar una lista con los números del 1 al 10, luego modificar los elementos de la lista multiplicandolos
por un valor ingresado por el usuario.

'''

print(' ')
print('EJERCICIO N°5')
print('MODIFICAR LOS ELEMENTOS DE LA LISTA')

elementos = list(range(1, 11))
print(elementos)

num1 = int(input('Digite un número para multiplicar los datos: '))
for indice, i in enumerate(elementos):
    elementos[indice] *= num1

print(f'Lista final con los elementos multiplicados por {num1}:')
for i in elementos:
    print(i, end='-')
print(' ')

'''
EJERCICIO N°6
Pedir números y meterlos en una lista, cuando el usuario introduzca un número 0, nuestro programa dejaria de insertar.
Por último, mostrar los números ordenados de menor a mayor.

'''

print(' ')
print('EJERCICIO N°6')
print('Insertar elementos y ordenarlos')

lista = []
salir = False

while not salir:
     num2 = int(input('Digite los números que decea en su lista: '))
     if num2 == 0:
         salir = True
         print('A seleccionado salir de la lista.')
     else:
         lista.append(num2)

lista.sort() #esta funcion ordena la lista)
print(f'\nLa lista ordenada es: \n{lista}')
