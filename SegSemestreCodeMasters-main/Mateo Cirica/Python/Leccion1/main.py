# Listas = Mateo, Maria Jose, Pablo, Joaquin, Emiliano

nombres = ['Mateo', 'Maria Jose', 'Pablo', 'Joaquin', 'Emiliano']
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[2])
print(nombres[-1])
print(nombres[-2])

print(nombres[0:2]) # Solo muestra el indidce 0, 1 pero no el indice 2
# Ir del incio de la lista al indice (sin incluirlo)
print(nombres[ :3]) #Indices a mostrar 0, 1 y 2
# Desde el indice indicado hasta el final
print(nombres[1: ])
# Modificamos un valor

nombres[2] = 'Sergio'
nombres[4] = 'Emi'
print(nombres)

# Iterar una lista
for nombre in nombres: # Nombre es singular, la lista es plural
    print(nombre)
else:
    print('Se acabaron los elementos de la lista')

# Preguntamos cuantos elementos tiene
print(len(nombres)) # Le pasamos como parametro la lista

# Agregamos un elemento
nombres.append('Marcelo')
print(nombres)

# Insertar un elemento en un indice especifico
nombres.insert(1, 'Alberto')
print(nombres)
nombres.insert(3, 'Debora')
print(nombres)

# Eliminamos un elemento
nombres.remove('Alberto')
print(nombres)

# Eliminar el ultimo elemento
nombres.pop()
print(nombres)

# Eliminar un indice especifico
del nombres[2]
print(nombres)

# Eliminar todos los elementos
nombres.clear()
print(nombres)

# Eliminar la lista
del nombres
# print(nombres)

# Definimos una tupla
cocina = ('cuchara', 'cuchillo', 'tenedor')
print(len(cocina))

# Acceder a un elemento, para esto utilizamos corchetes no parentesis
print(cocina[0])
# Mostrar de manera inversa
print(cocina[-1])

# Acceder a un rango
print(cocina[0:2])

# Ejemplo
verduras = ('papa',) # Una tupla necesita aunque sea un elemento la coma
# De lo contrario seria un tipo str cadena

# Recorremos los elementos de la tupla 
for cocinar in cocina: # Print usta usando \n para saltos de lineas
    print(cocinar, end=' ') # Usamos end= para eliminar los saltos de linea

cocinaLista = list(cocina)
cocinaLista[0] = 'Plato'
cocina = tuple(cocinaLista)

print('\n', cocina)

# del cocina esto es para eliminar la tupla

# Tipo set

planetas = {'Marte', 'Júpiter', 'Venus'}
print(len(planetas))

# Revisar si un elemento esta dentro de set
print('Marte' in planetas)

# Agregar un elemento
planetas.add('Tierra')
print(planetas)

# Eliminar elementos, puede arrojar un error si el elemento no existe
planetas.remove('Júpiter')
planetas.discard('Marte')

# Limpiar set o conjunto
planetas.clear()

# Eliminar set
del planetas
# print(planetas)

# 'Maradona':10 Un diccionario esta compuesto por dos elementos
# UNA LLAVE Y UN VALOR
# dict(key,value)
diccionario = {
    'IDE':'Integrated Development Environment',
    'POO':'Programacion Orientada a Objetos',
    'SABD':'Sistema de Administracion de Base de Datos'
}
print(len(diccionario))
print(diccionario)

# Acceder a un diccionario con la llave(key)
print(diccionario['IDE'])

# Otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

# Modificamos elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

# Como recorrer los elementos
for termino in diccionario: # Recorremos mostrando solo las llaves
    print(termino)

# Necesitamos una funcion para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

# Otras maneras de acceder a un diccionario
for termino in diccionario.keys(): # Estamos usando una funcion
    print(termino) # Muestra solo las llaves

for valor in diccionario.values(): # Usamos una funcion para acceder al valor
    print(valor)

# Comprobar la existencia de algun elemento
print('IDE' in diccionario) # devuelve un booleano

# Agregar un elemento
diccionario['PK'] = 'Primary key'
print(diccionario)

# Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

# Vaciar un diccionario
diccionario.clear()
print(diccionario)

# Eliminar diccionario
del diccionario # el diccionario se borro

# Concatenamos listas
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = lista1+lista2
print(lista3)

lista3.extend([7, 8, 9, 1]) # Funcion para agregar varios elementos a una lista
print(lista3)

print(lista3.index(5)) # Funcion para ubicar en que indice esta el valor ingresado
# print(lista3.index(0)) esto daria un error por que elemento no es parte de la lista

# Como saber cuantos valores repetidos hay dentro de una lista
print(lista3.count(1)) # Cuenta cuantos valores iguales hay dentro de la lista

# Para poner al reves una lista
lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo sus elementos
lista3 = lista3 * 2
print(lista3)

# Metodos de ordenamiento
lista3.sort() # Ordena los elementos ascendentemente
print(lista3)
lista3.sort(reverse=True) # Odesna descendentemente
print(lista3)

# Repaso de tuplas
tupla = (4, 'Hola', 6.78, [1, 2, 78], 4, 'Hola') # Puede tener diferentes tipos de datos dentro
print(tupla)

print(4 in tupla) # Accion booleana, su respuesta es de tipo booleana
# Lo que podemos usar dentrp de tuplas son: index, count, len
# En tuplas se puede convertir de tupla a lista y de lista a tupla

# Repaso de set o conjunto
# para definir un conjunto
conjunto2 = set()
conjunto1 = {'bye',}
conjunto2.add(7)
conjunto2.add('Hola')
print(conjunto2) 
conjunto1.add('Hola')
print(conjunto1)
print(3 not in conjunto1)

# Como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto2)

# Operaciones en conjuntos
conjunto3 = conjunto1 | conjunto2
print(conjunto3)

conjunto3 = conjunto1 & conjunto2
print(conjunto3)

conjunto3 = conjunto1 - conjunto2
print(conjunto3)

conjunto3 = conjunto2 - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3)) #Aqui preguntamos si un conjunto es un subconjunto dentro de otro
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issuperset(conjunto1)) # Preguntamos si los elementos del conjunto1 estan dentro del 3
print(conjunto3.issuperset(conjunto2)) # Si es verdadero quiere decir que el conjunto3 es un superconjunto
print(conjunto2.issuperset(conjunto3))

# Como saber si ambos conjuntos son disconexos, esto es si no comparten elementos en comun
print(conjunto1.isdisjoint(conjunto2)) # No hay cosa en comun

# Convertir un conjunto totalmente en inmutable
conjunto1 =  frozenset # Esto hace que el conjunto sea totalmente inmuntable
# No se puede agregar, modificar ni eliminar elementos del conjunto

# Repaso Diccionarios
diccionarioNuevo = {'Azul': 'Blue', 'Rojo': 'Red', 'Verde': 'Green', 'Amarillo': 'Los platanos(Yellow)'}
print(diccionarioNuevo)
# Como eliminar
del (diccionarioNuevo['Azul'])
print(diccionarioNuevo)

# Los diccionarios pueden almacenar diferentes tipos de datos
diccionario2 = {'Mateo': {'Edad': 20, 'Altura': 1.75}, 'Osvaldo': [20, 1.70], 'Maria Jose': [41, 1.65]}
print(diccionario2)

seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 36, 'Altura': 1.70, 'Precio': '30 Millones', 'Posicion': 'Segundo Delantero' },
    11: {'Nombre': 'Angel Di Maria', 'Edad': 35, 'Altura': 1.80, 'Precio': '15 Millones', 'Posicion': 'Extremo' },
    8: {'Nombre': 'Enzo Fernandez', 'Edad': 22, 'Altura': 1.78, 'Precio': '130 Millones', 'Posicion': 'Mediocampista' },
    9: {'Nombre': 'Julian Alvarez', 'Edad': 23, 'Altura': 1.71, 'Precio': '55 Millones', 'Posicion': 'Centrodelantero' },
    17: {'Nombre': 'Alejandro Garnacho', 'Edad': 19, 'Altura': 1.80, 'Precio': '20 Millones', 'Posicion': 'Extremo Izquierdo' },
    23: {'Nombre': 'Emiliano Martinez', 'Edad': 31, 'Altura': 1.93, 'Precio': '40 Millones', 'Posicion': 'Arquero' },
    13: {'Nombre': 'Cristian Romero', 'Edad': 25, 'Altura': 1.85, 'Precion': '45 Millones', 'Posicion': 'Defensor Central' },
    4: {'Nombre': 'Gonzalo Montiel', 'Edad': 26, 'Altura': 1.78, 'Precio': '15 Millones', 'Posicion': 'Lateral Derecho'} 
}

for llave, valor in seleccionArgentina.items():
    print(llave, valor)

print('Tenemos cargados en el diccionario la cantidad de: ', end=' ')
print(len(seleccionArgentina))

# Pilas usando listas
pila = [1, 2, 3]

# Agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

# Sacamos elementos desde el final
elementoBorrado = pila.pop() # Quita el ultimo elemento y lo guarda
print(f'Sacamos el elemento {elementoBorrado}')
print(f'La pila ahora quedo asi: {pila}')

# Colas con listas
# Estructura de datos de tipo fifo(fist input / first output)
cola = ['Mateo', 'Joaquin', 'Sergio', 'Lionel']

# Agregamos elementos al final de la cola
cola.append('Natalia')
cola.append('Jose')
print(cola)

# Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f'Atendido el cliente {seRetira}')
print(cola)

# Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f'Atendido el cliente {seRetira}')
print(cola)

# Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f'Atendido el cliente {seRetira}')
print(cola)

for i in seleccionArgentina:
    print(f'{i} -> {seleccionArgentina[i]}')