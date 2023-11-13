Proceso Principal
	menu();
	Escribir "";
FinProceso

SubProceso menu()
	Definir opcion como entero;
	definir num,exponente como reales;
	Repetir
		Escribir "MENU";
		Escribir "1. Potenciacion";
		Escribir "2. Raiz cuadrada";
		Escribir "3. Terminar";
		Escribir "Ingrese una opcion";
		Leer opcion;
		Escribir "";
		Segun opcion Hacer
			1:
				Escribir sin saltar "ingrese un numero";
				Leer num;
				Escribir "Digite un exponente: ";
				Leer exponente;
				Escribir "La potencia es: ",potencia(num,exponente);
			2:
				Escribir sin saltar "Difite un numero: ";
				Leer num;
				Escribir "La raiz cuadrada es:",raizCuadrada(num);
			3:
			De Otro Modo:
				Escribir "Seequivoco de opcion";
		FinSegun
		Escribir "";
	Hasta Que opcion = 3
FinSubProceso

SubProceso pot <- potencia(num,exponente)
	Definir pot como real ;
	pot <- num^exponente;
FinSubProceso

SubProceso raiz_C <- raizCuadrada(num)
	Definir raiz_C como real;
	raiz_C <- rc(num);
FinSubProceso
