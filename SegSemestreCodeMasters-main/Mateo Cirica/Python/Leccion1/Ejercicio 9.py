# Ejercicio 9: Mostrar una frase sin espacios y contar su longitud
# Hacer un programa donde el usuario ingrese una frase, se le 
# devolvera la misma frase pero sin espacios en blanco, y 
# ademas un contador de cuantos caracteres tiene la frase
# (sin contar los espacios en blanco)
# Ejemplo:    frase =  vivir por siempre en paz
#             frase final = vivirporsiempreenpaz
#             N° de caracteres = 20

frase = input("Digite una frase: ")
fraseFinal = frase.replace(" ", "")
caracteres = len(fraseFinal)

print(f"Su frase es: {frase}")
print(f'Su frase sin espacios es: {fraseFinal}')
print(f'La cantidad de caracteres de su frase (sin espacios) es: {caracteres}')