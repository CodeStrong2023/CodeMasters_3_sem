Proceso arreglo
	definir num,ultimo,i Como Entero;
	Dimension num[6];
	
	para i<-0 Hasta 5 Con Paso 1 Hacer
		Escribir (i+1), '. digite un numero: ';
		Leer num[i];
	FinPara
	
	ultimo <- num[5];
	
	Para i<-4 Hasta 0 Con Paso -1 hacer
		num[i+1] <- num[i];
	FinPara
	
	num[0] <- ultimo;
	
	Escribir 'el nuevo arreglo es: ';
	Para i<-0 Hasta 5 Con Paso 1 Hacer
		Escribir Sin Saltarnum[i];
	FinPara
	Escribir '';
FinProceso
