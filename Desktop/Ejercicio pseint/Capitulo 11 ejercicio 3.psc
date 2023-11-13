Proceso sin_titulo
	Definir num,i,j Como Entero;
	Dimension num[4,4];
	Definir filas,suma_filas,posFila Como Entero;
	Dimension filas[4];
	Definir columnas,suma_col,posCol Como Entero;
	Dimension columnas[4];
	Para i<-0 Hasta 3 Hacer
		Para j<-0 Hasta 3 Hacer
			Escribir 'Digite un numero[',i,'][',j,']:';
			Leer num[i,j];
		FinPara
	FinPara
	Escribir '';
	Para i<-0 Hasta 3 Hacer
		Para j<-0 Hasta 3 Hacer
			Escribir num[i,j],' ' Sin Saltar;
		FinPara
		Escribir '';
	FinPara
	posFila <- 0;
	Para i<-0 Hasta 3 Hacer
		suma_filas <- 0;
		Para j<-0 Hasta 3 Hacer
			suma_filas <- suma_filas+num[i,j];
		FinPara
		filas[posFila] <- suma_filas;
		posFila <- posFila+1;
	FinPara
	posCol <- 0;
	Para j<-0 Hasta 3 Hacer
		suma_col <- 0;
		Para i<-0 Hasta 3 Hacer
			suma_col <- suma_col+num[i,j];
		FinPara
		columnas[posCol] <- suma_col;
		posCol <- posCol+1;
	FinPara
	Escribir ' ';
	Escribir 'La suma de las filas son:' Sin Saltar;
	Para i<-0 Hasta 3 Hacer
		Escribir filas[i],' ' Sin Saltar;
	FinPara
	Escribir '';
	Escribir 'La suma de las columnas son:' Sin Saltar;
	Para i<-0 Hasta 3 Hacer
		Escribir 'columnas',(i),'';
	FinPara
	Escribir '';
FinProceso
