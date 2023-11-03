# Ejercicio 7: Juego adivina el numero
# Realiza un juego para adivinar un numero. Para ello se
# debe generar un numero aleatorio entre 1 - 100, y luego ir pidiendo
# numeros indicando "es mayor " o "es menor" segun sea mayor o menor
# con respecto a N. El proceso termina cuando el usuario acierta
# y allí se debe mostrar el numero de intentos.

import random
print("\tJuego Aivina el numero: ")
aleatorio = random.randint(0,100) # con esta funcion va a tomar de 0 a 100 literal, generamos un numero aleatorio
contador = 0
while True:
    numero = int(input("Digite un numero: "))
    contador += 1
    if numero > aleatorio:
        print("\tNo es el numero, digita uno menor: ")
    elif numero < aleatorio:
        print("\tNo es el nuemero, digite un numero mayor")
    else:
        print(f'¡Felicidades, has adivinado el numero! {aleatorio}')
        break # Rompe el ciclo y el bucle
print(f"\nNumero de intentos: {contador}")