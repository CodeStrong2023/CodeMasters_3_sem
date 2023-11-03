#dad la sig tupla 
tupla= (13,1,8,3,2,5,8) #definimos la tupla
#crear una lista que solo incluya los números  menortes a 5 e imprimir [1,3,2]
lista=[]#definimos la lista 
#filtramos los elementos menores a 5
for elemento in tupla:
    if elemento<5:
        lista.append(elemento)
print(lista)