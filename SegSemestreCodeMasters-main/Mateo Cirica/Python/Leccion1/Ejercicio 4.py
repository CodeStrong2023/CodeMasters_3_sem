#  Ejercicio 4: Sumar numeros pares dentro de un rango
# Hacer un programa para sumar numeros pares dentro
# de un rango, por ejemplo:
#                             suma de numeros pares del 2 al 30
#                             suma = 240

suma = 0
for i in range(15,36):
    if i % 2 == 0:
        suma += i

print(f'La suma de los pares en el rango de entre 15 y 36 es: {suma}')