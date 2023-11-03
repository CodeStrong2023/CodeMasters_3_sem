# Ejericicio 6: Tabla de multiplicar
# Hacer un programa que pida un numero por teclado y guarde
# en una lista su tabla de multiplicar hasta el 10. Por ejemplo:
# Si digita el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50

numero = int(input("Digite un numero: "))
tabla = []

for i in range(1,11):
    tabla.append(numero * i)
print(f'\nLa tabla del {numero} es la siguiente: {tabla}')