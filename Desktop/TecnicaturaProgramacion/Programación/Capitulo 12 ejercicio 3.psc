Proceso Principal
	menu();
	Escribir "";
FinProceso

SubProceso menu()
	Definir opcion Como Entero;
	Definir pesos,dolares Como Real;
	Repetir
		Escribir "Menu";
		Escribir "1. Cambiar pesos a dolares";
		Escribir "2. Cambiar dolares a pesos";
		Escribir "3. Salir";
		Escribir Sin Saltar"Digite una opcion";
		Leer opcion;
		Escribir "";
		Segun opcion Hacer
			1:
				Escribir Sin Saltar "Digite la cantidad de pesos: ";
				Leer pesos;
				dolares <- cambiopesosAdolares(pesos);
				Escribir "El cambio a dolar es: $", dolares;
			2:
				Escribir Sin Saltar"Digite la cantidad de dolares";
				Leer dolares ;
				pesos <- cambiodolaresAPesos(dolares);
				Escribir "El cambio a pesos es: $", pesos;
			3:
			De Otro Modo:
				Escribir "Rspuesta incorrecta";
		FinSegun
		Escribir "";
	Hasta Que opcion = 3
FinSubProceso

SubProceso dolar <- cambiopesosAdolares(pesos)
	definir dolar como real;
	dolar <- pesos/200;
FinSubProceso

SubProceso pesos <- cambiodolaresAPesos(dolares)
	definir pesos como real;
	pesos <- dolares*200;
FinSubProceso
