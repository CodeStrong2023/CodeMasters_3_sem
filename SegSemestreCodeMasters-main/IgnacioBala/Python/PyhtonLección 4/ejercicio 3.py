lista = []
salir = False
while not salir:
    numero = int(input('Digite unb numero: '))
    if numero == 0:
        salir = True
    else:
     lista.append(numero)
lista.sort()
print(f'\nLista ordenada:\n{lista}')