# Ejercicio 5: convertidor de temperaturas
# Realizar dos funciones para convertir de grados celcius
# a fahrenheit y viseversa.
# investigar las formulas

def celcius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

celsius = float(input('Digite la temperaatura en grados celsius: '))
resultado = celcius_a_fahrenheit(celsius)
print(f'{celsius} C a F -> {resultado:.2f}')

fahrenheit = float(input('Digite la temperaatura en grados fahrenheit: '))
resultado = fahrenheit_a_celsius(fahrenheit)
print(f'{fahrenheit} F a C -> {resultado:.2f}')