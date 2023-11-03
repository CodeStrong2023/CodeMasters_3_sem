saldo = 1000
while True:
    print("\t.:MENÚ:.")
    print("1. Ingresar dinero en la cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Mostrar dinero disponible")
    print("4. Salir")
    opcion = int(input("Digite alguna pcion del menu:"))
    print()
    if opcion == 1:
        extra = float(input("Cuanto dinero desea ingresar -->"))
        saldo+= extra
        print(f'Dinero en la cuenta al momento: ${saldo}')
    elif opcion == 2:
        retirar =   float(input("Cuanto dinero desea retirar --> :"))
        if retirar > saldo:
            print("No tiene esa cant de dinero")
        else:
            saldo -= retirar
            print(f"Dinero en la cuenta al momento: ${saldo}")
    elif opcion  == 3:
        print(f"Dinero en la cuenta al momento: ${saldo}")
    elif opcion == 4:
        print(f"Gracias por utilizar el cajero automatico, hasta luego")
        break
    else:
        print("Se equivoo de opción de menu")