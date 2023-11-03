import random
print("\t.:Juego adivina la palabra:.")
aleatorio = random.randint(0,100)
contador = 0
while True:
    numero = int(input("Digite el numero: "))
    contador+=1
    if numero > aleatorio:
        print("\nNo es el número, digite un número menor")
    elif numero < aleatorio:
        print("\nNo es el número, digite un número mayor")
    else:
        print(f"Felicidades, acabas de adivinar el numero {aleatorio}")
        break
        print(f"\nNúmero de intentos : {contador}")