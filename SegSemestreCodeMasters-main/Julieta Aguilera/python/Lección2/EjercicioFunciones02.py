# Ejercicio 2: Funciones con * argumentos para multiplicar
# Crear una funcion para multiplicar los valores recibidos
# de tipo numerico, utilizamos argumentos variables *args
# como parametros de la funcion y regresamos como resultado
# la multiplicacion de todos los valores pasados como argumentos
# definimos la funcion para multiplicar
def multiplicar_valores(*numeros): # el mas utilizado es *args
    resultado = 1 # el cero no nos ayuda a multiplicar
    for numero in numeros:
        resultado *= numero
    return resultado

# llamamos a la funcion
print(multiplicar_valores(3, 5, 15, 3)) # le pasamos los argumentos
