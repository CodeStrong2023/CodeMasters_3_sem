//Hacer un algoritmo que almacene números en una matriz de 3*4. Imprimir la suma de los números pares almacenados en la matriz. 
Proceso sin_titulo
	Definir num,j,i,suma Como Entero;
	Dimension num[3,4];
	
	Para i<-0 Hasta 2 Con Paso 1 Hacer
		Para j<-0 Hasta 3 Con Paso 1 Hacer
			Escribir Sin Saltar"Digite un número[",i,"] [",j,"];";
			Leer num[i,j];

		FinPara
	FinPara
	Escribir " ";
	Para i<-0 Hasta 2 Con Paso 1 Hacer
		Para j<-0 Hasta 3 Con Paso 1 Hacer
		FinPara
		Escribir "";
	FinPara
	suma<- 0;
	Para i<-0 Hasta 2 Con Paso 1 Hacer
		Para j<-0 Hasta 3 Con Paso 1 Hacer
			Si num[i,j] mod 2 = 0 Entonces
			suma<-suma+ num[i,j];
			FinSi
		FinPara
	FinPara
	Escribir " ";
	Escribir "La suma de los pares es:", suma;
FinProceso
