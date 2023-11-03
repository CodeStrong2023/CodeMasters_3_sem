Proceso sin_titulo
	Definir n_elementos Como Entero;
	Definir i,suma como Enteros;
	Escribir "Digite la cantidad de elementos a susmarse:";
	leer n_elementos;
	i<-1;
	suma<- 0;
	Mientras i<=n_elementos Hacer
		
		suma<- suma+i^2;
		i<-i +1;
	FinMientras
	Escribir "la suma es:",suma;
FinProceso
