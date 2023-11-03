
'''

EJERCICIO N° 4

Hacer un programa para sumar números pares dentro de un rango, ej:
suma de números parea del 2 al 30
suma = 240

'''

print(' ')
print('EJERCICIO N°4')
print('SUMAR NÚMEROS PARES DENTRO DE UN RANGO')

a = int(input('Digite de donde quiere comenzar la suma: '))
b = int(input('Digite hasta donde llega la suma: '))
suma = 0

for i in range(a,b,1):
    if i % 2== 0: #Esto es el número par
       suma += i

print(f'\n La suma de los números pares es: {suma}')

'''

EJERCICIO N°5

Hacer un programa para calcular el factorial de un número positivo.

'''

print(' ')
print('EJERCICIO N°5')
print('FACTORIAL DE UN NÚMERO ')

num = int(input('Digite un número: '))
while num < 0:
    print('Error el número de ser positivo.')
    num = int(input('Digite un número: '))

factorial = 1

for i in range(1,num+1):
    factorial *= i
print(f'\n El factorial del número {num} es: {factorial}')

'''

EJERCICIO N°6

HACER UN PROGRAMA QUE PIDA UN NÚMERO POR TECLEADO Y LO GUARDE EN UNA LISTA DE SU TABLA DE MULTIPLICACION HASTA EL 10.
Ej: Si digita el 5 la lista seria:
5,0,15,20,25,30,35,40,45,50

'''

print(' ')
print('EJERCICIO N°6')
print('TABLA DE MULTIPLICAR')

tabla = []
num = int(input('Coloque un número: '))
lista = list(range(1, 11))

for i in lista:
    i *= num
    tabla.append(i)
    i += 1

print(f'\n La tabla del número {num} es: ')
for i in tabla:
    print(i, end='-')

'''
FORMA PROFE:

FOR I IN RANGE(1,11):
    lista.append(i*num)
print(f'\n La tabla del número {num} es: \n {lista} ')

OTRA FORMA: PARA VER LA TABLA COMPLETA :)

FOR I IN RANGE(1,11):
    lista.append(i*num)
    
for indice,i in enumerate(lista):
    print(f'{num} x {i} = {lista(indice)}')

'''

print(' ')

'''

EJERCICIO N°7

Realizar un juego para adivinar un número. Para ello se debe generar un número aleatorio entre 1 - 100, y luego ir pidiendo
números indiccando "es mayor" o "es menor" segun sea mayor o menor con respecto a N.
El proceso termina cuando el usuario acierta y allí se debe mostrar el número de intentos.

'''

print(' ')
print('EJERCICIO N°7')
print('ADIVINA EL NÚMERO')

import random
aleatorio = random.randint(0,100) # Generamos un número aleatorio y lo guardamos.
intentos = 0

while True:
    num = int(input('Coloque un número positivo: '))
    intentos += 1
    if num < aleatorio: # num es menor a el número dado
            print('El número que a colocado es MENOR al buscado :(')
    elif num > aleatorio:
         print('El número que a colocado es MAYOR al buscado :( ')
    else:
         print(f'\n FELICIDADES!! HAZ GANADO :) ')
         print(f'Adivinaste el numero: {aleatorio}')
         break # Esto cierra el ciclo
print(f'El número de intentos es: {intentos}')

'''

EJERCICIO N°8

Hacer un programa que simule un cajero automatico con un saldo inicial de $1000 y tendra el siguiente menú de opciones:
1. Ingrear dinero en la cuenta.
2. Retirar dinero de la cuenta.
3. Mostrar dinero disponible.
4. Salir

'''

print(' ')
print('EJERCICIO N°8')
print('CAJERO AUTOMATICO')

saldo = 1000

while True:
    print(' ')
    print('\t  .:MENU:. ')
    print('1. Ingrear dinero en la cuenta.')
    print('2. Retirar dinero de la cuenta.')
    print('3. Mostrar dinero disponible.')
    print('4. Salir')
    num = int(input('Que desea hacer?'))
    print(' ')
    if num == 1:
        num1 = int(input('Coloque su deposito: '))
        saldo += num1
        print(f'Su saldo actual es: {saldo}')
    elif num == 2:
        num2 = int(input('Cuanto desea retirar: '))
        if num2 > saldo:
            print('No posee esa cantidad')
        else:
            saldo -= num2
            print(f'Su saldo actual es: {saldo}')
    elif num == 3:
        print(f'Su saldo actual es: {saldo}')
    elif num == 4:
        print('Gracias por usar este cajero :)')
        break
    else:
        print('A seleccionado una opción incorrecta. Vuelva a seleccionar por favor.')
print('A seleccionado SALIR')


'''

EJERCICIO N°9

Hacer un programa donde el usuario ingrese una frase, se le devolvera la misma frase pero sin espacion en blanco,
y además un contador de cuántos caracteres tiene la frase (Sin contar los espacios en blanco). Ej:

frase = viva la vida
frase final = vivalavida
N° de caracteres = 10

'''

print(' ')
print('EJERCICIO N°9')
print('MOSTRAR UNA FRASE SIN ESPACIOS Y CONTAR SU LONGITUD ')

frase = input('Digite una frase: ')
frase2 = ''

for i in frase:
    if i != ' ':
        frase2 += i
frase = frase2
print(f'La frase sin especios es: {frase}')
print(f'N° de caracteres: {len(frase)}') # este comando cuenta la cantidad de digitos de una frase