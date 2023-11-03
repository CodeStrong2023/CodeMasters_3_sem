# Listas  =  Nacho , Ariel , Guad

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
