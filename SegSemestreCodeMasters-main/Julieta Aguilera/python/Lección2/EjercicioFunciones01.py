# Comenzamos con funciones

# Definimos una función
# mi_funcion() #No se puede llamar antes de definir a una funcion
def mi_funcion(): # para identificar a la funcion utilizamos parentesis
    print('Buenas tardes')

mi_funcion() #estamos llamando la funcion
mi_funcion() # Se puede llamar a una funcion N cantidad de veces

def sumar2(a = 0, b= 0): #Le damos un valor por defaut
    return a+ b
resultado = sumar2()
print(f'Resultado de la suma: {resultado}')
print(f'Resultado de la suma {sumar2(22, 66)}')

# argumentos, variables en funcion
def listaNombres(*nombres): #Normalmente se utiliza: *args
    for nombre in nombres:
        print(nombre)
listaNombres('Lucas', 'José', 'Claudia', 'Rosa', 'Maria')
listaNombres('Marcos', 'Daniel', 'Romina', 'Pepe', 'Marcela', 'Carlos')

def listaTerminos(**terminos):#Lo mas utilizado es **kwars para recibir los argumentos
    for llave, valor in terminos.items(): #kwargs significa: key word  argument
        print(f'{llave}: {valor}')

listaTerminos() #no recibe nada, nada se va a mostrar
listaTerminos(IDE='Integrated Develoment Enviroment', PK='Primaruy key')
listaTerminos(Nombre='Leonel Messi')

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombres)
nombres2 = ['Leti', 'Juli', 'Mati']
desplegarNombres(nombres2)
#desplegarNombres(10) no es un objeto iterable
desplegarNombres((10, 11)) #la convertimpos en una tupla, en un solo elemento no olvidar la coma
desplegarNombres([22, 55]) # la convertimos en una lista

#Funcion recursivas
def factorial(numero):
    if numero == 1: #caso base
        return 1
    else:
        return numero * factorial(numero - 1)

resultado = factorial(5) # lo hacemos en codigo duro
print(f'El factorial del numero 5 es: {resultado}') # tarea que el usuario ingrese el numero para calcular el factorial

def factorial2(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)
numero = int(input("Ingrese un numero para calcular su factorial: "))
resultado = factorial(numero)
print(f'El factorial de {numero} es: {resultado}')