#lista= ariel ,julio, mario, pedro

nombres= ['naty','osvaldo','lili','ariel']
print(nombres)
# print(nombres[0])
# print(nombres[1])
# print(nombres[3])
# print(nombres[-1])
# print(nombres[-2])
print(nombres[0:2])# solo muestra el indice 0,1 pero no el indice 2 
#ir del inicio de la lista al indice (sin incluirlo)
print(nombres[:3])#indice mostrara 0,1,2
#desde el indice indicado hasta el final
print(nombres[1:])
#modificamos un valor
nombres[2]= 'liliana'
nombres[0]= 'natalia'
print(nombres)
#iterar unalista
for nombre in nombres: #nombre es singular, la lista es plurarl
    print(nombre)
else:
    print('se acabaron los elementos de la lista ')
#preguntamos cuantos elementos toiene
print(len(nombres)) # le pasamos como parametro la lista

#agregamos un elemento 
nombres.append('marcelo')
print(nombres)

#inseratr un elemento en un indice especifico
nombres.insert(1, 'alberto')
print(nombres)
nombres.insert(3, 'debora')
print(nombres)

#eliminamos  un elemento
nombres.remove('alberto')
print(nombres)

#eliminamos el ultimo elemento
nombres.pop()
print(nombres)

#eliminamos un indice especifico
del nombres[2] #del significa delete
print(nombres)

#eliminar, borraro limpiar todos los elementos 
nombres.clear()
print(nombres)

#eliminar la lista 
del nombres
print(nombres)