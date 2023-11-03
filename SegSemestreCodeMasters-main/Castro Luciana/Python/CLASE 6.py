
'''

EJERCICIO N°10:
Hacer un programa que pida una cadena por teclado, luego meter los caracteres en una lista sin repetir caracteres.

'''

print(' ')
print('EJERCICIO N°10')
print('NO REPETIR CARACTERES')

cadena = input('Digite una cadena: ')
lista = []

for i in cadena:
    if i not in lista: # Si el caracter aún no esta en la lista
        lista.append(i) # Lo agrego a la lista :)
print(f'La nueva lista sin caracteres repetidos es: \n {lista}')

'''

EJERCICIO N°11:
Hacer un programa que simule una agenda de contactos. Crear un diccionario donde la clave sea el nombre del usuario y el valor sea el telefono,
el programa tendra el siguiente menu de opciones:
1. Nuevo contacto
2. Borrar contacto
3. Ver contactos Existentes
4. Salir

'''

print(' ')
print('EJERCICIO N°11')
print('AGENDA TELEFONICA')

contactos = {}

while True:
    print(' ')
    print('\t  .:MENU:. ')
    print('1. Nuevo contacto')
    print('2. Borrar contacto.')
    print('3. Ver contactos Existentes.')
    print('4. Salir')
    num = int(input('Que desea hacer?'))
    print(' ')
    if num == 1:
        print('Coloque los datos del contacto')
        nombre = input('Nombre: ')
        telefono = input('Número: ')
        if nombre not in contactos:
            contactos[nombre] = telefono
            print('Contacto agendado exitosamente :)')
        else:
            print('Este contacto ya existe.')
    elif num == 2:
        nombre = input('Que contacto desea borrar?')
        if nombre not in contactos:
            print('El contacto que busca no existe.')
        else:
            del (contactos[nombre])
            print('El contacto se ha eliminado correctamente.')
    elif num == 3:
        print(f'\n CONTACTOS: {contactos}')
    elif num == 4:
        break
    else:
        print('A seleccionado una opción incorrecta. Vuelva a seleccionar por favor.')
print('A seleccionado salir.')

'''
                    EJERCICIOS FUNCIONES
EJERCICIO N°1:
Crear una funcion para sumar los valores recibidos de tipo numericos, utilizando argumentos variables *args como parametro de la funcion
y agregar como resultado la suma de todos los valores pasados como argumentos.

'''

print(' ')
print('EJERCICIOS FUNCIONES')
print('EJERCICIO N°1')

def sumarValor(*args):
    resultado = 0
    for valor in args:
        resultado += valor
    return resultado

print(sumarValor(3,7,8,2))