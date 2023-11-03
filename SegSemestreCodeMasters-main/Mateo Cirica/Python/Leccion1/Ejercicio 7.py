# Ejercicio 7: Juego adivina el numero
# Realizar un juego para adivinar un numero. Para ello se debe
# generar un numero aleatorio entre 1 - 100, luego ir pidiendo
# numero indicando "es mayor" o "es menor" segun sea mayor o menor
# con respecto a N. El proceso termina cunado el usuario acierta
# y alli se debe mostrar el numero de intentos.
import random
aleatorio = random.randint(0, 100)
contador = 0
while True:
    numero = int(input("Digite un numero: "))
    contador += 1
    if numero > aleatorio:
        print("\nNo es el numero, digite un numero menor")
    elif numero < aleatorio:
        print("\nNo es el numero, digite un numero mayor")
    else:
        print(f'FELICIDADES, acabas de adivinar el numero {aleatorio}')
        break

print(f'\nNumero de intentos: {contador}')