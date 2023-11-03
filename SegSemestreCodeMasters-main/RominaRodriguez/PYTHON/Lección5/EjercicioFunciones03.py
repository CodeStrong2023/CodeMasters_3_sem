# Ejercicio 3: Función Recursiva
# Imprimir números de 5 a 1 de manera descendente usando funciones recursivas
# Puede ser cualquier valor positivo, por ejemplo, si pasamos el valor
# de 5, debe imprimir:
# 5
# 4
# 3
# 2
# 1
# En caso de ser el número 3 debe imprimir:
# 3
# 2
# 1
# Si se ingresa números negativos no imprime nada
def imprimir_numeros_recursivos(numero):
    if numero >= 1:#caso base
        print(numero)
        imprimir_numeros_recursivos(numero-1)#caso recursivo
    elif numero == 0:
        return
    elif numero <= 0:
        print("Valor ingresado incorrecto...")
numero_recursivo = int(input("Digite un número: "))
resultado = imprimir_numeros_recursivos(numero_recursivo)

