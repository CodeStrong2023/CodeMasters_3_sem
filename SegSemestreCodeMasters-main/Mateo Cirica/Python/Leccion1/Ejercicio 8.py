# Ejercicio 8: Menu interactivo - Cajero Automatico
# Hacer un programa que simule un cajer automatico con un saldo
# inicial de 1000$ y tendra el siguiente menu de opciones:
#                 1. Ingresar dinero en la cuenta
#                 2. Retirar dinero de la cuenta
#                 3. Mostrar dinero disponible
#                 4. Salir

saldo = 1000
while True:
    print("1. Ingresar dinero en la cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Mostrar dinero disponible")
    print("4. Salir")
    opcion = int(input("\nDigite una opcion: \n"))
    if opcion == 1:
        extra = float(input("¿Cuanto dinero queire ingresar? -> "))
        saldo += extra
        print(f"Dinero en la cuenta: ${saldo}")
        break
    elif opcion == 2:
        retirar = float(input("¿Cuanto dinero quiere retirar? -> "))
        if retirar > saldo:
            print(f"No cuenta con esa cantidad de dinero, recuerde que su saldo es: {saldo}")
            retirar = float(input("Digite una nueva cantidad: "))
        saldo -= retirar
        print(f'Usted ha retirado ${retirar}, su saldo actual es: ${saldo}')
        break
    elif opcion == 3:
        print(f'Su saldo actualmente es de: ${saldo}')
        break
    else: 
        print("Gracias por usar nuestros servicios, Adios")
        break
