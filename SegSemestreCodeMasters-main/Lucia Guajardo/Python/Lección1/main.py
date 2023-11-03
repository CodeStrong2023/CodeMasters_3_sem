#lista = Ariel, Liliana, Natalia, osvaldo
# Colecciones en python

# Las listas es lo que se conoce en otros lenguajes como arreglos o vetores

nombres = ['Naty', 'osvaldo ', 'Lily', 'Ariel']
print(nombres)
print(nombres[0:2]) #solo muestra el indice 0, 1 pero no el indice 2
#ir del inicio de la lista al indice (sin incluirlo)
print(nombres[:3]) #Indices a mostrar 0, 1, 2
#Desde el indice hasta el final
print(nombres[1: ])
#Modificamos un valor
nombres[2] = 'Liliana'
nombres[0] = 'Natalia'
print(nombres)
# Iterar una lista
for nombre in nombres: #nombre es singular, la lista es plural
    print(nombre)
else:
    print('Se acabaron los elementos de la lista')

#Preguntamos cuantos elementos tiene
print(len(nombres)) # le pasamos como parametro la lista

#Agregamos un elemento
nombres.append('Marcelo')
nombres.append([1, 2, 3])
nombres.append(True)
nombres.append(10.45)
nombres.append(7)
print(nombres)

#Insertar un elemento en un indice especifico
nombres.insert(1,'Alberto')
print(nombres)
nombres.insert(1,'Debora')
print(nombres)

#Eliminamos un elemento
nombres.remove('Alberto')
print(nombres)

# Eliminar el ultimo elemento
nombres.pop()
print(nombres)

# Eliminar un indice especifico
del nombres[2] #del significado delate (eliminar)
print(nombres)

# Borar lista
nombres.clear()
print(nombres)

#Eliminar la lista
#del nombres
print(nombres)

#Definimos una tupla
cocina = ('cuchara', 'cuchillo', 'tenedor')
print(len(cocina))

# Acceder a un elemento, para esto utilizamos corchetes no parentesis
print(cocina[0])
# mostar de manera inversa
print(cocina[-1])

#Acceder a un rango
print(cocina[0:1])
#ejemplo
verduras = ('papa,') #una tupla necesita aunque sea de un elemento: la coma
#de lo contrario solo seria un tipo str cadena

#Recorremos los elemntos de la tupla
for cocinar in cocina: #Print enta usando \n para saltos de lineas
    print(cocinar, end= ' ') # usamos end= para eliminar los saltos de linea

cocinaLista = list(cocina)
cocinaLista[0] = 'plato'
cocina = tuple(cocinaLista)
print('\n', cocina)

#del cocina #esto es para eliminar una tupla


#Tipo set
planetas = {'Martes', 'Júpiter', 'Venus'}
print(len(planetas)) #usamos la funcion len = length significa largo

#Revisar si un elemento existe dentro de set
print('Júpiter' in planetas)

#Agregar un elemento
planetas.add('Tierra') #Add es una funcion
print(planetas)

#Eliminar elementos, puede arrojar un erro si el elemneto no existe
planetas.remove('Júpiter') #esta funcion ante un mal ingreso u inexistencia del elemento da error
print(planetas)
planetas.discard('Tierra') #esta funcion no nos presenta un error
print(planetas)

# Limpiar set
planetas.clear()
print(planetas)

#Eliminar set
#del planetas
print(planetas) #al eliminar nos muestra error

# 'Maradona':10 un diccionario esta compuesto por dos elementos
# Una llave y un valor
# dict(key, value)
diccionario = {
    'IDE': 'Integrated Development Environment',
    'POO': 'Programacion Orientada a Objetos',
    'SABD': 'Sistema de Administracion de Base de Datos'

}
#verificar la cantidad de elementos del diccionario
print(len(diccionario))
print(diccionario)

#Acceder a un diccionario con la llave(key)
print(diccionario['IDE'])

#Otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

# Modificammos elementos
diccionario['IDE'] = 'Entornos de desaroolo Integrado'
print(diccionario)

# Como recorrer elementos
for termino in diccionario:
    print(termino)

#for termino, valor in diccionario:
#   print(termino, valor)

# Otras maneras de acceder a un diccionario
for termino in diccionario.keys(): #estamos usando una funcion
    print(termino) # Muestra solo las llaves

for valor in diccionario.values():
    print(valor)

# Comprobar la existencia de algun elemento
print('IDE' in diccionario) #devuelve un booleano

# Agregar un elemento
diccionario['PK'] = 'Primary key'
print(diccionario)

# Elimainar un elemento
diccionario.pop('SABD')
print(diccionario)

# Eliminar diccionario
del diccionario  # El diccionario se elimino

# Concatenamos listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 =lista1 + lista2
print(lista3)

lista3.extend([7, 8, 9]) #Funcion para agregar varios elementos a una lsita
print(lista3)

print(lista3.index(5)) #Funcion para ubicar en que indice esta el valor ingresado
#print(lista3.index(0)) # esto diria un error por no ser el elemento parte de la lista

#Como saber cuantos valores repetidos hay dentro de una lista
print(lista3.count(1)) #cuanto cuantos valores iguales hay dentro de la lista

# Para poner al reves una lista
lista3.reverse()
print(lista3)

#para que una lista se multiplique repitiendo sus elementos
lista = [1, 2 ,3] * 2
print(lista)

#metodo de ordenamiento, en python es una funcion
lista3.sort() #ordena los elementos ascendentemente
print(lista3)
lista3.sort(reverse=True) #ordena desendentemente
print(lista3)

tupla = (4, 'Hola', 6.78, [1, 2, 78], 4, 'Hola')
print(tupla)

print(4 in tupla) # Accion booleana, su respuesta es de tipo booleano
# Lo que podemos usar dentro de tuplas son: index, count, len
# En tuplas se puede convertir de tupla a lista y de lista a tupla

# Repaso de set o conjunto
# para definir un conjunto
conjunto2 = set()
conjunto1 = {'bye', }
conjunto2.add(7)
conjunto2.add('Hola')
print(conjunto2)
conjunto1.add('hola')
print(conjunto1)
print(3 not in conjunto1) #preguntamos si el numero 3 esta en el conjuntto1

#Como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto2) #nos devuelve como respuesta un booleano

# Operaciones en conjunto
conjunto3 = conjunto1 | conjunto2 #nos devuelve como respuesta un booleano
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 #que elemento tienen en comun
print(conjunto3)

conjunto3 = conjunto1 - conjunto2 # Asigna el valor que esta en el conjunto1 y no en el conjunto2
print(conjunto3)
conjunto3 = conjunto2 - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 #elementos que no comparten o que son diferentes entre ambos
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3)) # Aqui preguntamos si unconjunto es un subconjunto dentro de otro
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issubset(conjunto1))# Preguntamos si los elementos del conjunto1 estan dentro del 3
print(conjunto3.issubset(conjunto2))# Si es verdadero quiere decir que el conjunto3 es un superconjunto
print(conjunto2.issubset(conjunto3))

# como saber si ambos conjuntos son disconexos, esto es si no comparten elementos en comun
print(conjunto1.isdisjoint(conjunto2)) #No hay cosas en comun

# Convertir un conjunto totalmente en inmutable
conjunto1 = frozenset #Esto hace que el conjunto sea totalmente inmutable
# No se puede agregar modificar ni eliminar elementos del conjunto

# Repaso diccionarios
diccionarioNuevo = {'Azul': 'Blue', 'Red': 'Rojo', 'Verde': 'Green', 'Amarillo': 'yellow'}

# Como eliminar
del (diccionarioNuevo['Azul'])
print(diccionarioNuevo)

# Los diccionarios pueden almacenar diferente tipos de datos
diccionario2 = {'Ariel': {'edad': 40, 'Altura': 1.83}, 'Osvaldo': [45, 1.85], 'Natalia': [35, 1.67]}
print(diccionario2)

seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '50 Millones', 'Posicion': 'Extremo Derecho'},
    11: {'Nombre': 'Angel Di Maria', 'Edad': 34, 'Altura': 1.80, 'Precio': '12 Millones', 'Posicion': 'Extremo derecho'},
    21: {'Nombre': 'Paulo Dybala', 'Edad': 28, 'Altura':1.77, 'Precio': '35 Millones', 'Posicion':  'Media punta'},
    19: {'Nombre': 'Nicolas Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '3.5 Millones', 'Posicion': 'Defensa central'},
    1: {'Nombre': 'Franco Armani', 'Edad': 35, 'Altura': 1.89, 'Precio': '3.5 Millones', 'Posicion': 'Portero'},
    8: {'Nombre': 'Marcos Acuña', 'Edad': 31, 'Altura': 1.72, 'Precio': '2 millones', 'Posicion': 'Defensa'},
    7: {'Nombre': 'Rodrigo De Paul', 'Edad': 29, 'Altura': 1.77, 'Precio': '292 mil ', 'Posicion': 'centrocampista'},
    26: {'Nombre': 'Nahuel Molina', 'Edad': 25, 'Altura': 1.75, 'Precio': '18 millones ', 'Posicion': 'Defensa'},
    9: {'Nombre': 'Julian Álvarez', 'Edad': 23, 'Altura': 1.70, 'Precio': '32 millones ', 'Posicion': 'Delantero'}

}
for llave, valor in seleccionArgentina.items():
    print(llave, valor)

# Como tarea agregar por lo menos 4 jugadores mas al diccionario seleccionArgentina
print('Tenemos cargado en el diccionario la cantidad de jugadores: ', end=' ')
print(len(seleccionArgentina))

#Pilas usando listas
pila = [1, 2, 3]

#Agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

#Sacamos elementos desde el final
elementoBorrado = pila.pop() #Quita el ultimo y lo guarda en la variable
print(f'Sacamos el elemento: {elementoBorrado}')
print(f'La pila ahora quedo asi: {pila}')

#Colas con listas
#Estructura de datos de tipo fifo (first input / first output)
cola = ['Ariel', 'Osvaldo', 'Liliana', 'Pilar']

#Agregamos elementos al final de la cola
cola.append('Natalia')
cola.append('José')
print(cola)

# Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendiendo el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

#seguimos mostrando como recorre un diccionario con el ciclo for
for i in seleccionArgentina:
    print(f'{i} -> {seleccionArgentina[i]}')
