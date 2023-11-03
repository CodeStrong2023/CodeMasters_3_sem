# ejercicio 3: funcion recursiva
# imprimir numeros de 5 sl 1 de manera descendente usando funciones recursivas
# valor de 5, debe imprimir
# 5
# 4
# 3
# 2
# 1
# en caso de ser el numero 3 debe imprimir
# 3
# 2
# 1
# si se ingresan numeros negativos no imprime nada

def imprimir_numeros_recursivos(numero):
    if numero >= 1: #caso base
        print(numero) # caso recursivo
        imprimir_numeros_recursivos(numero-1)
    elif numero == 0:
        return
    elif numero <=0:
        print('Valor ingresado incorrecto')
numero = int(input('Ingrese un numero: '))
imprimir_numeros_recursivos(5)# tarea, que el usuario ingrese el numero

