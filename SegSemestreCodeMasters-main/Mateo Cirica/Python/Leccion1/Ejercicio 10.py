# Ejercicio 10: No repetir caracteres
# Hacer un programa que pida una cadena por teclado, luego
# meter los caracteres en una lista sin repetir caracteres

cadena = str(input("Digite una frase/cadena: "))
lista = []
for i in cadena:
    lista.append(i)

lista2 = set(lista)
lista = sorted(list(lista2))

print(lista)