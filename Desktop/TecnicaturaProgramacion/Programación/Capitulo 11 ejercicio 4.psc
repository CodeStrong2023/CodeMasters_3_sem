Proceso sin_titulo
	Definir num,i,j Como Entero;
	Dimension num[3,4];
	Definir mayor,suma_col,posCol Como Entero;
	Para i<-0 Hasta 2 Hacer
		Para j<-0 Hasta 3 Hacer
			Escribir 'Digite un numero[',i,'][',j,']:' Sin Saltar;
			Leer num[i,j];
		FinPara
	FinPara
	Para i<-0 Hasta 2 Hacer
		Para j<-0 Hasta 3 Hacer
			Escribir num[i,j],' ' Sin Saltar;
		FinPara
		Escribir '';
	FinPara
	suma_col <- 0;
	Para i<-0 Hasta 2 Hacer
		suma_col <- suma_col+num[i,0];
	FinPara
	mayor <- suma_col;
	posCol <- 0;
	Para j<-1 Hasta 2 Hacer
		suma_col <- 0;
		Para i<-0 Hasta 2 Hacer
			suma_col <- suma_col+num[i,j];
		FinPara
		Si suma_col>mayor Entonces
			mayor <- suma_col;
			posCol <- j;
		FinSi
	FinPara
	Escribir '';
	Escribir 'La columna con la mayor suma es: ',posCol;
	Escribir 'La suma de dicha columna es: ',mayor;
	Escribir '';
FinProceso
