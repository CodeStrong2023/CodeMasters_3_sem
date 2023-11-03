
def mi_funcion():
    print('Saludo a los alumnos de la tecnicatura')


mi_funcion()# Estamos llamandop a la función

# Desempaquetado de listas
def show (name,lastName):
    print(name+' '+lastName)
person = ['Ariel','Bala']
show(person[0],person[1]) # Pasamos uno por uno los datos de la función
show(*person) # Esto es igual a lop anterior pero pasamos todo junto
person2 = ('Ignacio' , 'Bala')
show(*person2)

person3 = {'lastname':'Lucero', 'name':'Natalia'}
show(*person3)

numbers = [1,2,3,4,5]
for n in numbers:
    print(n)
    if n == 3:
        break
else:
    print('Esto se termina')

# Lista de comprensión
names = ['Mariano','Pablo','Ignacio','Paolo']
alongP = [p for p in names if p[0] == 'p']
print(alongP)

bottleC = [{"name":"Quilmes","country":'Arg'},
           {"name":"Corona","country": "Mx"},
            {"name":"Stella Artois","country": "Delgiun"},
           ]
Arg = [b for b in bottleC if b["country"] == "Arg"]

def mi_Funcion2(name,lastName):
    print('Saludos a los panas ')
    print(f'Nombre: {name}, Apellido: {lastName}')
mi_Funcion2('Raul','Layana')
mi_Funcion2('Pipa','Higuaín')
mi_Funcion2('Nacho','Bala')

# Creamos una función para sumar
def sumar(a,b):
    return  a + b
resultado = sumar(78,22)
print(f'El resultado de la suma es : {sumar(22,66)}')


def sumar2(a= 0, b= 0):
    return a+b
resultado = sumar2()
print(f'Resultado de la suma: {resultado}')
print(f'Resultado de la suma: {sumar2(22, 66)}')

#Argumentos variables en funciones
def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)
listarNombres('Fabio','Tobi','Gastón','Martina','Claudia')
listarNombres('rabio','Zobi','fastón','Martina','Claudia')

def listarTermino(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')

listarTermino() # Si no recibe nada el argumento no muestra nada la consola
listarTermino(IDE = 'Integrated Develoment Enviroment', PK='Primaruy Key')
listarTermino(Nombre = 'Leonel Messi')

def desplegarNombres(nombres):
        for nombre in nombres:
            print(nombre)
nombres2 = ['Tito', 'Pedro', 'Carlos']
desplegarNombres(nombres2)
desplegarNombres('Nefario')
#esplegarNombres(10) # No es un objeto iterable
desplegarNombres((10, 11)) # La convertmios en una tupla
desplegarNombres([22, 55])

#Funciones recursivas
def factorial(numero):

    if numero == 1:#caso base
        return 1
    else:
        return numero * factorial(numero-1)
    numeroFactorial = int(input('Digite algún número para calcular el factorial'))
    resultado = factorial(5)# Lo hacemos en código
    print(f'El factorial del número 5 es :{resultado}')