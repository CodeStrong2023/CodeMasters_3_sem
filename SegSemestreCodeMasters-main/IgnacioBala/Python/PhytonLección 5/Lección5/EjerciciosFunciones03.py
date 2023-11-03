def imprimir_numeros_recursivos(numero):
    if numero >= 1:
        print(numero)
        imprimir_numeros_recursivos(numero-1)

imprimir_numeros_recursivos(5)