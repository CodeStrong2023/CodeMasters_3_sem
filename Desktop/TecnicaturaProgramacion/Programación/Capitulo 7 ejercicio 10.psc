Proceso arreglos
	Definir i,j,k Como Enteros;
	Definir creciente Como Logico;
	Definir a,b,c como enteros;
	Dimension a[5],b[5],c[10];
	
	Escribir 'digite los elementos del primer arreglo: ';
	
	Repetir
		creciente <- Verdadero;
		Para i<-0 Hasta 4 con paso 1 Hacer
			Escribir i,'.digite un numero: ';
			Leer a[i];
		FinPara
	
	
	
		Para i<-0 Hasta 3 Con Paso 1 Hacer
			si a[i] > a[i+1] Entonces
				
				creciente <- Falso;
			FinSi
		FinPara
		
		
		si creciente = Falso Entonces
			Escribir 'arreglo desordenado, vuelva a digitarlo';
			
		FinSi
	Hasta Que creciente = Verdadero
	
	Escribir 'digite los elementos del segundo arreglo: ';
	
	Repetir
		creciente <- Verdadero;
		Para i<-0 Hasta 4 con paso 1 Hacer
			Escribir i,'.digite un numero: ';
			Leer b[i];
		FinPara
		
		
		
		Para i<-0 Hasta 3 Con Paso 1 Hacer
			si b[i] > b[i] Entonces
				creciente <- Falso;
			FinSi
		FinPara
		
		
		si creciente = Falso Entonces
			Escribir 'arreglo desordenado, vuelva a digitarlo';
			
		FinSi
	Hasta Que creciente = Verdadero
	
	
	i <- 0;
	j <- 0;
	k <- 0;
	
	Mientras (i<5 y j < 5) Hacer
		si a[i] < b[j] Entonces
			c[k] <- a[i];
			i <- i + 1;
		SiNo
			c[k] <- b[j];
			j <- j + 1;
		FinSi
		k <- k +1;
	FinMientras
	
	si (i=5) Entonces
		Mientras (j<5) Hacer
			c[k] <- b[j];
			j <- j + 1;
			k <- k + 1;
		FinMientras
	SiNo
		si (j=5) Entonces
			Mientras  (i<5) Hacer
				c[k] <- a[i];
				i <- i + 1;
				k <- k + 1;
				
			FinMientras
		FinSi
		
	FinSi
	
	Para  i<-0 Hasta 9 Con Paso 1 Hacer
		Escribir i,'.elemento: ',c[i];
		
	FinPara
	
FinProceso
