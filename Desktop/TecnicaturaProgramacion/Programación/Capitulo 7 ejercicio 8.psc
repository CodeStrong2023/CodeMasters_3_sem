Proceso arreglo
	Definir num,i,dato,posicion,j Como Entero;
	Definir creciente Como Logico;
	Dimension num[6];
	Repetir
		creciente <- verdadero;
		Para i<-0 Hasta 4 Hacer
			Escribir (i+1),'.digite un numero:';
			Leer num[i];
		FinPara
		Para i<-0 Hasta 3 Hacer
			Si num[i]>num[i+1] Entonces
				creciente <- falso;
			FinSi
		FinPara
		Si creciente=falso Entonces
			Escribir 'el arreglo no esta ordenado, digite nuevamente';
		FinSi
	Hasta Que creciente=verdadero
	Escribir 'digite un valor a agregar';
	Leer dato;
	posicion <- 0;
	j <- 0;
	Mientras num[j]<dato Y j<5 Hacer
		posicion <- posicion+1;
		j <- j+1;
	FinMientras
	Para i<-4 Hasta posicion Con Paso -1 Hacer
		num[i+1]<-num[i];
	FinPara
	num[posicion] <- dato;
	Escribir '';
	Escribir 'el nuevo arreglo es: ';
	Para i<-0 Hasta 5 Hacer
		Escribir sin saltar num[i],'' Sin Saltar;
	FinPara
	Escribir '';
FinProceso

