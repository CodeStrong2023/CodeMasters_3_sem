Proceso sin_titulo
	Definir i Como Entero;
	Definir numReales, suma, promedio Como Real;
	Dimension numReales[5];
	suma<- 0;
	Para i<-0 Hasta 4 Con Paso 1 Hacer
		Escribir i,". Digite un número:";
		leer numReales[i];
		suma<- suma + numReales[i];
	
	FinPara
	promedio<- suma/5;
	Escribir "La suma es:", suma;
	Escribir "El promedio es:", promedio;
FinProceso
