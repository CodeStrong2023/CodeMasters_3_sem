import math
# Ejercicio de Matematicas
# Para sacar la raiz cuadrada de un numero positivo

numero = int(input("Digite un numero positivo: "))
while(numero < 0):
    print("Error, el numero que ingresaste es negativo, ingresa uno positivo")
    numero = int(input("Digite un numero positivo"))
print(f'\nSu raiz cuadrada es: {math.sqrt(numero):.2f}')
