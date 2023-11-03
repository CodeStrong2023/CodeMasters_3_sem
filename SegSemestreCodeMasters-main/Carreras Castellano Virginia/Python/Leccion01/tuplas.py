# definimos una tupla
cocina=('cuchara', 'cuchillo', 'tenedor')
print(len(cocina))

#acceder un elemento, para esto utilizamos corchetes NO parentesis
print(cocina[0])
#mostrar de manera inversa
print(cocina[-1])

#acceder a un rango
print(cocina[0:2])

#ejemplo
verduras=('papa') #una tupla necesita aunque sea de un elemento: la coma
#de lo contrario solo sería un tipo str cadena 

#recorremos los elementos de la tupla
for cocinar in cocina: #print esta usando /N para saltos de lineas 
    print(cocinar, end=' ') #usamos end=' ' para eliminar los saltos de lineas 
    
cocinaLista= list(cocina)
cocinaLista[0]= 'plato'
cocina= tuple(cocinaLista)
print('\n', cocina)

del cocina # esto es para eliminar una tupla
print(cocina)