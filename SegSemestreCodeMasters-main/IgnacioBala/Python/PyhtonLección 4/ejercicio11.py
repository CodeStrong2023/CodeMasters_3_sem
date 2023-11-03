agenda = {}
while True :
    print('\t.:MENÚ:.')
    print('1.NUEVO CONTACTO')
    print('2.BORRAR CONATCTO')
    print('3.VER CONTACTOS EXISTENTES')
    print('4.SALIR')
    opcion = int(input('Digite una de as opciones del menú: '))
    if opcion == 1:
        nombre = input('Digite el nombre del contacto: ')
        telefono = input('Digite el el n de teléfono: ')
        if nombre not in agenda:
            agenda[nombre] = telefono
            print('Contacto agregado exitosamente')
        else:
            print('Ese número de contacto existe')

    elif opcion == 2:
        nombre = input('Cuál es eñ nombre de contacto')
        if nombre in agenda:
            del (agenda[nombre])
            print('Se ha borrado el contacto')
        else:
            print('Ese contacto no existe en la agenda')
    elif opcion == 3:
        print('Agenda de contactos')
        for clave,valor in agenda.items():
            print(f'Nombre:{clave}, Teléfono:{valor}')
    elif opcion == 4:
        print('Gracias por usar su agenda de contactos')
        break
    else:
        print('Se equivoco de opción de menú')
        print()