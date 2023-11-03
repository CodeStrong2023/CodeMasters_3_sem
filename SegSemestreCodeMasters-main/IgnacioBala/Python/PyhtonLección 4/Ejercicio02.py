lista = list(range(1,11))
print('lista original')
for i in lista:
     print(i,end='-')
valor = int(input('\nDigite un valñor a mutiplicar'))
for indice, i in enumerate(lista):
    lista[indice] *= valor

print(f'Lista final con los elemntos multiplicado por{valor}')
for i in lista :
        print(i,end='-')
