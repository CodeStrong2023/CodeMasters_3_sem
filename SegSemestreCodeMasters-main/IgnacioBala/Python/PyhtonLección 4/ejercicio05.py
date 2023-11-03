numero = int(input('Digite un numero: '))
while numero <0 :
    print('Error -> el numero tiene que ser positivo')
    numero= int(input('Digite el numero: '))
factorial= 1
for i in range(1,numero + 1):
    factorial*=i
print(f'\nEl factorial  {numero} positivo ingresado es: {factorial}')