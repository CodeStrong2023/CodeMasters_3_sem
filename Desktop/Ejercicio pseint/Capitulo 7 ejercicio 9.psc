Proceso arreglo
	Definir num,i,posicion Como Entero;
	Dimension num[5];
	Para i<-0 Hasta 4 Hacer
		Escribir i,'.digite un numero: ';
		Leer num[i];
	FinPara
	Repetir
		Escribir 'digite un aposicion del arreglo: ';
		Leer posicion;
	Hasta Que posicion >= 0 Y posicion <= 4
	Para i<-posicion Hasta 3 Hacer
		num[i] <- num[i+1];
	FinPara
	Escribir '';
	Escribir ' el nuevo arreglo es: ';
	Para i<-0 Hasta 3 Hacer
		Escribir i,'.elemento: ',num[i];
	FinPara
FinProceso
