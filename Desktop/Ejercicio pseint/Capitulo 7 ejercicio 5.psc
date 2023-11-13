Proceso sin_titulo
	Definir num,i como entero;
	Dimension num[8];
	Para i<-0 Hasta 7 Hacer
		Escribir (i+1),".Digite un número:";
		Leer num[i];
	FinPara
	Para i<-0 Hasta 3 Hacer
		Escribir num[i];
		Escribir num[7-i];
	FinPara
FinProceso
