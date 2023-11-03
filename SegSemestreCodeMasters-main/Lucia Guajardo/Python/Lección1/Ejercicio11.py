# Ejercicio 11: Agenda telefonica
# Hacer un programa que simule una agenda de contactos.
# Crear un diccionario donde la clave sea el nombre del usuario
# y el valor sea el telefono, el programa tendrá eñ siguiente
# menú de opciones:
#                   1. Nuevo contacto
#                   2. Borrar contacto
#                   3. Ver contacto existente
#                   4. Salir
agenda = {}
while True:
    print("\t.¡MENÚ!.")
    print("1. Nuevo contacto")
    print("2. Borrar contacto")
    print("3. Ver contacto existente")
    print("4. Salir")
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el número de telefono: ")
        if nombre not in agenda:
            agenda[nombre] = telefono
            print("Contanto agregado exitosamente")
        else:
            print("Este nombre de contacto ya exixte")
    elif opcion == 2:
        nombre = input("Cuál es el nombre del contacto: ")
        if nombre in agenda:
            del (agenda[nombre])
            print("Se ha eliminado el contacto requerido")
        else:
            print("Este contacto no existe en la agenda")
    elif opcion == 3:
        print("Agenda de contactos")
        for clave, valor in agenda.items():
            print(f"Nombre: {clave}, Telefono: {valor}")
    elif opcion == 4:
        print("Gracias por utilizar su agenda de contacto")
        break
    else:
        print("Se equivoco de opción de menú")
    print()