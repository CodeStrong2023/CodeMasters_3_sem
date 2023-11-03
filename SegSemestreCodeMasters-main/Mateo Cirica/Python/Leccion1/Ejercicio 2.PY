lista = list(range(1, 11))
print('Lista Original: ')
for i in lista:
    print(i, end='-')
numero = int(input('\nDigite un numero a multiplicar: '))


for indice, i in enumerate(lista):
    lista[indice] *= numero

print(f'Lista final con los elementos multiplicados por {numero}')

for i in lista:
    print(i, end='-')