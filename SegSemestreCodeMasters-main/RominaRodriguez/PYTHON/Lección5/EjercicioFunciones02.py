# Ejercicio 2: Función con *args para multiplicar
# Crear una función para multiplicar los valores recibidos
# de tipo númerico, utilizando argumentos variables *args
# como parámetro de la función y regresar como resultado
# la multiplicación de todos los valores pasados como argumento

#Definimos la función pR multiplicar
def multiplicar_valor(*numeros):# El mas utilizado *args
    resultado = 1
    for numero in numeros:
        resultado *= numero
    return resultado

#Llamamos a la funvión
print(multiplicar_valor(3, 5, 15, 3)) # Le pasamos los argumentos
