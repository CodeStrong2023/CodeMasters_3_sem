def multiplicar_valores(*numeros):
    resultado = 1
    for numero in numeros:
        resultado *= numero

    return resultado


# LLamamos fx
print(multiplicar_valores(3, 5, 15, 3))
