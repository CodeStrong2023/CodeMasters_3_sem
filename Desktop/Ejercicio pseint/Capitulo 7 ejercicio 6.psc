Proceso sin_titulo
	Definir creciente,decreciente como logico ;
	Dimension num [5];
	Para i<-0 Hasta 4 Hacer
		Escribir (i+1),",Digite un n�mero:";
		Leer num[i];
	FinPara
	creciente <- falso;
	decreciente <- falso;
	Para i<-0 Hasta 3 Hacer
		Si num[i] < num[i+1] Entonces
			creciente <- verdadero;
		FinSi
		Si condicion Entonces
			decreciente <- verdadero;
		FinSi
	FinPara
	Si creciente=verdadero y decreciente= falso Entonces
		Escribir "El arreglo esta en forma creciente";
	SiNo
		Si creciente=falso y decreciente= verdadero Entonces
			Escribir "El arreglo est� en forma decreciente";
		SiNo
			Escribir "El arreglo est� desordenado";
		FinSi
	FinSi
FinProceso
