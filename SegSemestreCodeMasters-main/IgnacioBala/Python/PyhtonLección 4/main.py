# Listas  =  Nacho , Ariel , Guad
# Colecciones pyhton
nombres = ['Nacho','Raúl', 'Marciano', 'Ariel']
print(nombres)
print(nombres[0:2])
# Ir al inicio de la lista al indice (sin incluirlo)
print(nombres[ :3]) # Indices a mostrar 0,1,2
print(nombres[1: ])
# Modificamos un valor
nombres[3] = 'Raquel'
print(nombres)
# Iterar nuestra lista
for nombre in nombres: # nombre es singular, la lista es plural
    print(nombre)
else:
    print('Se acaban los lementos de la lista')
    # Preguntamos cuantos eleemntos tiene nuestra lista
print(len(nombres)) # Le pasamos como parámetro
# Aregamos un elemento
nombres.append('Marcelo')
print(nombres)
# Insertar un elemento en un índice específico
nombres.insert(1,'Albeto')
print(nombres)
nombres.insert(3, 'nachonesa')
print(nombres)
# Eliminar el último elemento
nombres.pop()
print(nombres)
# Eliminar un índice específico
del nombres[2]
print(nombres)
# Definimos uina tupla
cocina = ('cuchara', 'cuchillo', 'tenedor' )
print (len(cocina))

# Acceder a un elemento con corchetes, no con paréntesis
print(cocina[0])
# Mostrar de una manera inversa
print(cocina[-1])
#Acceder a un rango
print(cocina[0:1])
# Ejemplo
verdura =('papa',)
# Recooremos los elementios de unja tupla
for cocinar in cocina:
    print(cocinar, end=' ')

cocinarLista = list(cocina)
cocinarLista [0] = 'Plato'
cocina = tuple(cocinarLista)
print('\n',cocina)
#del cocina
print(cocina)

# Tipo set
planeta = {'Marte','Júpiter','Venus'}
print(len(planeta)) # Usamos la función len = lenght significa largo

# Revisar si existe un elemento dentro de un se
print('Marte' in planeta)

# Agregar un elemento

planeta.add('Tierra') # es una fx
print(planeta)

# Eliminar un elemento que no existe puede arrojar error

planeta.remove('Júpiter')
print(planeta)

# Limpiar set
planeta.clear()
print(planeta)
# Eliminar set



diccionario = {
    'IDE':'Integrated Development Environment',
    'POO':'Programación Orientada a Objetos',
    'SABD' : 'Siste de Administración de Datos'
}
print(len(diccionario))
print(diccionario)
print(diccionario["IDE"])

print(diccionario.get('SABD'))
print(diccionario.get('POO'))

# Cómo Recorrer elementos
for termino in diccionario:
    print(termino)

for termino,valor in diccionario.items():
    print(termino,valor)

# Otras maneras de acceder al diccionario

for termino in diccionario.keys():
    print(termino)

for termino in diccionario.values():
    print(termino)

# Comprobar la existencia de un valor
print('IDE'in diccionario) # Devuelve un booleano

# Agregar un elemnto

diccionario['Pk'] = 'Primary Key'
print(diccionario)

# Eliminar un elemento

diccionario.pop('SABD')
print(diccionario)

# Limpiar un diccionario
diccionario.clear()
print(diccionario)


# Repaso set o conjunt
conjuto2 = set()
conjunto1 = {"bye",}
conjuto2.add(7)
conjuto2.add("Hola")
print(conjuto2)
conjunto1.add("hola")
print(conjunto1)
print(3 not in conjunto1)
print(conjunto1 == conjuto2)

# Operaciones en conjunto

conjunto3 = conjunto1 | conjuto2
print(conjunto3)

conjunto3 = conjunto1 & conjuto2
print(conjunto3)

conjunto3 = conjunto1 - conjuto2
print(conjunto3)

conjunto3 = conjuto2 - conjunto1 # ra
print(conjunto3)

conjunto3 = conjunto1 | conjuto2
print(conjuto2.issubset(conjunto3))
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))

print(conjunto3.issubset(conjunto1))


seleccionArgentina = {
    10:{ 'Nombre' :'Lionel Messi', 'Edad': 35,'Altura':1.70, 'Precio':'50 millones', 'Posición': 'Extremo derecho'},
    11: {'Nombre': 'Di María', 'Edad': 34, 'Altura': 1.80, 'Precio': '12 millones', 'Posición': 'Extremo derecho'},
    9:{ 'Nombre' :'Julian Álvarez', 'Edad': 21,'Altura':1.75, 'Precio':'10 millones', 'Posición': 'Central'},
    5:{ 'Nombre' :'Paredes', 'Edad': 23,'Altura':1.80, 'Precio':'30 millones', 'Posición': 'Mediocampista'},

}

for llave,valor in seleccionArgentina.items():
        print(llave,valor)
print('Tenemos en el diccionario la cantidad de jugadores', end='')
print(len(seleccionArgentina))

# Pilas usando listas
pila = [1,2,3]
# Agregar elementos a la pila  por el final
pila.append(4)
pila.append(5)
print(pila)

# Sacamos elementos desdw el final
pila.pop()
print(pila)

# Sacamos elementos desde el final
elementoBorrado = pila.pop()
print(pila)

# Colas con listas
# Estructura de datos  de tipo fifo (first input / first output
cola = ['ARIEL','OSVALDO','LILIANA','PILAR']

# Agregamos elemento al final de la cola
cola.append('Natalia')
cola.append('Jose')
print(cola)

# Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f'Atendido Ariel')
print(cola)