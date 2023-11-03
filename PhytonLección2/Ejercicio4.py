import math

# Pedir al usuario que ingrese el radio
radio = float(input("Ingrese el radio del círculo: "))

# Calcular el área y la longitud de la circunferencia
area = math.pi * radio ** 2
longitud = 2 * math.pi * radio

# Imprimir los resultados
print("El área del círculo es:", area)
print("La longitud de la circunferencia es:", longitud)