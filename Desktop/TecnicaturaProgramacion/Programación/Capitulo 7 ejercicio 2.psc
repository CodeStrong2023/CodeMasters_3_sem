Proceso sin_titulo
	Definir num , n_elementos , i Como Entero; 
	Dimension num[100];
	
	Escribir "Digite el número de elementos para el arreglo";
	Leer n_elementos;
	Para  i<-0 Hasta n_elementos Con Paso 1 Hacer 
		num[i]<- azar(100);
	FinPara
	
	Para i<-0 Hasta n_elementos Con Paso 1 Hacer
		Escribir Sin Saltar num[i], "";
		Escribir "";
	FinPara
FinProceso
