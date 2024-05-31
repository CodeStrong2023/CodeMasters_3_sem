from Numeros_iguales_exception import NumerosIgualesException
resultado = None

try:
    a = int(input("Digite el primer número: "))
    b = int(input("Digite el segundo número: "))
    if a == b:
        raise NumerosIgualesException("Son numeros iguales")
    resultado = a/ b #Modificamos
except TypeError as e:
    print(f'TypeError - Ocurrió un error: {type(e)}')

except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrió un error: {type(e)}')
except Exception as e:
    print(f'Exception - Ocurrió u error: {type(e)}')
else:
    print("No se arrojo ninguna excepción")
finally:#siempre se va a ejecutar el final
    print("Ejecución de este bloque final")


print(f'El resultado es: {resultado}')
print('seguimos...')

    