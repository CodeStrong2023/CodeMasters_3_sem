lista1 = [1,2,3,4,5,6,4,4,4,2,3]
lista2 = [5,9,7,4,7,2,1,1,6,7,3,]

# Elimine numero repetidos
conjunto1 = set(lista1)
conjunto2 = set(lista2)

union = list(conjunto1 | conjunto2) # Unimos los dos conjuntos
solo1 = list(conjunto1 - conjunto2)  # list de palabaras que aparecen en la primer lista, pero no en la segunda
solo2 = list(conjunto2 -conjunto1) #  list de palabaras que aparecen en la segunda lista, pero no en la primera
intersección = list(conjunto1 & conjunto2)

print(f"Lista de palabras que aparecen en la listas : {union}")
print(f"list de palabaras que aparecen en la segunda lista, pero no en la segunda   : {solo1}")
print(f"ist de palabaras que aparecen en la segunda lista, pero no en la primera : {solo2}")
print(f"list de palabaras que aparecen en ambas listas : {intersección}")

