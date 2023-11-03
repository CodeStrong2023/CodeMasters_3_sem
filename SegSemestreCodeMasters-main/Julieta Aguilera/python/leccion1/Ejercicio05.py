# Ejercicio 5: Facorial de un numero positivo
# Hacer un programa para calcular el factor de un numero positivo

numero = int(input("Digite un numero: "))
while numero < 0:
    print("Error -> El numero debe ser positivo")
    numero = int(input("Digite un numero: "))
factorial = 1  # la variable para calcular el factorial
for i in range(1, numero+1):
    factorial *= i
print(f'\nEl factorial del numero {numero} positivo ingresado es: {factorial}')

