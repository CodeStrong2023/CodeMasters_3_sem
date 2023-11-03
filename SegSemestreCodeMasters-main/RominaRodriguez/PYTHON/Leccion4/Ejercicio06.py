# Ejercicio 6: Tabla de multiplicar
# Hacer un programa que pida un número por teclado y guarde
# en una lista su tabls de multiplicar hasta el 10. Por ejemp,o:
# Si digita el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50
numero = int(input("Digite un número: "))
lista = [] # Creamos una lista vacia
for i in range(1,11):
    lista.append(i*numero)
print(f"\nTabla de multipicar del {numero}: \n {lista}")

for indice,i in enumerate(lista):
    print(f"{numero} * {i} = {lista[indice]}") # Este formato es para visualizar el formato de una tabla de multiplicar
