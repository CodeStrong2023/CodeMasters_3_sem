Proceso principal
	Definir opcion Como Entero;
	Definir matriz Como Real;
	Dimension matriz[4,4];
	Repetir
		Escribir 'MENU';
		Escribir '1. llenar una matriz de 4*4';
		Escribir '2. mostrar la matriz';
		Escribir '3. sumar todos los elementos de la matriz';
		Escribir '4. salir';
		Escribir Sin Saltar 'digite la opcion de menu: ';
		Leer opcion;
		Escribir '';
		Segun opcion Hacer
			1:
				llenarMatriz(matriz);
			2:
				mostrarMatriz(matriz);
			3:
				Escribir 'la suma es: ',sumarMatriz(matriz);
			4:
			De Otro Modo:
				Escribir ' se equivoco de opcion de menu ';
		FinSegun
		Escribir '';
	Hasta Que opcion = 4
FinProceso

SubProceso llenarMatriz(matriz por referencia)
	Definir i,j Como Enteros;
	Para i<-0 Hasta 3 Hacer
		Para j<-0 Hasta 3 Hacer
			Escribir Sin Saltar 'digite un numero[',i,'][',j,']: ';
			Leer matriz[i,j];
		FinPara
	FinPara
FinSubProceso

SubProceso mostrarMatriz(matriz)
	Definir i,j Como Entero;
	Para i<-0 Hasta 3 Hacer
		Para j<-0 Hasta 3 Hacer
			Escribir sin saltar matriz[i,j],' ';
		FinPara
		Escribir '';
	FinPara
FinSubProceso

SubProceso suma <- sumarMatriz(matriz)
	Definir i,j Como Entero;
	Definir suma Como Real;
	suma <- 0;
	Para i<-0 Hasta 3 Hacer
		Para j<-0 Hasta 3 Hacer
			suma <- suma + matriz[i,j];
		FinPara
	FinPara
FinSubProceso
