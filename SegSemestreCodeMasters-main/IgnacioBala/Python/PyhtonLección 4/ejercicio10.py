cadena = input('Digite una cadena: ')
lista = []
for i in cadena:
    if i not in lista:
        lista.append(i)
print(f'\nLista de caracteres sin repetir ninguno: \n{lista}')