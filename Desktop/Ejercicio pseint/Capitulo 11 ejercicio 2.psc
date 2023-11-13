Proceso sin_titulo
	Definir  num,i,j,mayor,posfila,posCol Como Entero;;
	Dimension num[4,4];
	Para i<-0 Hasta 3 Con Paso 1 Hacer
		Para j<-0 Hasta 3 Con Paso 1 Hacer
			Escribir Sin Saltar"Digite un número[",i,"] [",j,"];";
			Leer num[i,j];
		FinPara
	FinPara
	Escribir " ";
	Para i<-0 Hasta 3 Con Paso 1 Hacer
		Para j<-0 Hasta 3 Con Paso 1 Hacer
		FinPara
	FinPara
	
	mayor<- 0;
	Para i<-0 Hasta 3 Con Paso 1 Hacer
		Para j<-0 Hasta 3 Con Paso 1 Hacer
			si num[i,j] > mayor Entonces
				
				mayor<- num[i,j];
				posfila<- i;
				posCol<- j;
				
			FinSi
		FinPara
		
	FinPara
	Escribir " ";
	Escribir " La posición del número es ", posfila,", Columna:",posCol;
FinProceso
