def sumar_valor1(*args):
    resultado = 0

    # Iteramos cada valor
    for valor in args:
        resultado += valor

    return resultado

# Llamamos la función
print(sumar_valor1(3, 5, 9))
