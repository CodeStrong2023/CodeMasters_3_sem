a = int(input('Digite donde va a comenzar la suma : '))
b = int(input('Digite hasta donde quiere llegar a sumar'))
suma = 0
for i in range (a,b+1):
    if i%2 == 0:
         suma += i
print(f"\nLa suma de los numeros pares dentro del rango es : {suma}")