'''''
miVariable = 3
print(miVariable)
miVariable = "a"
print(miVariable)
miVariable = 3.5
print(miVariable)
x = 10
y = 2
z = x + y
print(id(x))
print(id(y))
print(id(z))
a = 10.78
print(type(a))
# vamos a hacer un resumen
x = 10
print(x)
print(type(x))
x = 14.5
print(x)
print(type(x))
x = "Hola alumnos"
print(type(x))
x = True
print(x)
print(type(x))
x =False
print(x)
print(type(x))
# Manejo de cadenas (string)
miGrupoFavorito = "The letter black"
Características = "The best rock band"
print("Mi grupo favorito es",miGrupoFavorito,Características)
numero1 ="7"
numero2 ="8"
print(int(numero1)+ int(numero2))
# Tipos booleanos
miBooleano = 3>2
print(miBooleano)

# procesador de datos
# Función input
#resultado = input("Digite un número:")
#print(resultado)

#numero1 = int (input("Escribe el primer número:"))
#numero2 = int(input("Escribe el segundo número:"))
#resultado = numero1 + numero2
#print("El resultado de la suma es:", resultado)

#


dia = input("Cómo estuvo tu día en la escala del uno al 10:")
print("Mi día en la escala del uno al 10 es :", dia)

titulo = input("Proporciona el título de la obra:")
autor = input("Proporciona el nombre del autor de la obra:")
print(titulo,"fué escrito por",autor)

operandoA = 8
operandoB = 5
suma = operandoA+operandoB
print(f"El resultado de la suma es: {suma}")

resta = operandoA-operandoB
print(f"El resultado de la resta es: {resta}")

multiplicación =operandoA*operandoB
print(f"El resultado de la multiplicaión es: {multiplicación}")

division = operandoA / operandoB
print(f"El resultado de la división es: {division}")

division = operandoA// operandoB
print(f"El resultado de la division (int) es: {division}")

modulo = operandoA % operandoB
print(f"El resto de la division es (modulo): {modulo}")

exponente = operandoA**operandoB
print(f"El resultado del exponente es :{exponente}")


alto = int(input("Proporciona el alto de rectangulo"))
ancho = int(input("Proporciona el ancho del rectangulo"))
area = ancho*alto
perímetro= (alto+ancho)*2
print("El área del rectangulop es:", area)
print("El perímetro del rectángulo es:",perímetro)


miVariable3 = 10
print(miVariable3)
# Operadores de reasignación
miVariable3 = miVariable3 + 1
print(miVariable3)
miVariable3 += 1

print(miVariable3)

miVariable3-= 2
print(miVariable3)

miVariable3 *=2
print(miVariable3)

miVariable3 /= 2
print(miVariable3)

# Operador de comparación

d= 4
b= 2
resultado = d == b #Comprobamos si son iguales
print(resultado)

# Operador diferente
resultado= d!= b
print(resultado)

# Operador mayor que

resultado= d > b


# operadores lógicos

a = True
b = True
resultado = a and b
print(resultado)

# Operador or
resultado = a or b
print(resultado)
# operador not
resultado = not a

# Ejercicio valor dentro de un rango
valor = int(input("Digite un número dentro del rango 0 al 5:"))
valorMinimo = 0
valorMaximo = 5
dentroRango = valor >= valorMinimo and valor <= valorMaximo
if dentroRango:
 print(f'El valor {valor} esta dentro del rango')
else:
  print(f'El valor {valor} no esta dentro del rango')

# Ejercicio con el operador or, operador not
vaciones = False
diaDescanso = True
if not (vaciones or diaDescanso):
     print('Tiene trabajo que hacer')
else:
    print('Puede asisitir')

# Ejercicio Rango entre 20 y 30
edad =int(input("Digite su edad:"))
#veinte = edad >= 20 and edad < 30
#print(veinte)
#treinta = edad >= 30 and edad < 40
#print(treinta)
#if veinte or treinta:

if (20<= edad    <30) or (30 <= edad < 40):
    print("Estas dentro del rango de los (20'0) a (30'0) años")
#if veinte:
    #print("Estas dentro del rango de los (20\'0) años" )
#elif treinta:
    #print("Estas dentro del rango de los (30\'0) años")
else:
    print("No estas dentro del rango de los (20'0) a (30'0) años")

numero1 = int(input("Digite un numero"))
numero2 = int(input("Digite el valor para el numero 2"))

if numero1> numero2:
    print("El número 1 es mayor")
else:
    print("El número 2 es mayor")
'''''
print("Digite los siguientes datos del libro")
nombre = input("Digite el nombre del libro")
id = int(input("Digite el id del libro"))
precio = float(input("Digite el precio del libro"))
envioGratuito = input("Indicar si el libro es gratuito (True/False)")
if envioGratuito == "True":
    envioGratuito = True
elif envioGratuito == 'False':
    envioGratuito = False
else:
        envioGratuito = ("El valor es incorrecto, debes escribir (True/False)")
 print(f''' 
        Nombre: {nombre} 
        Id: {id}
        Precio: {precio}
        Envio Gratuito?: {envioGratuito}     
                        ''')

