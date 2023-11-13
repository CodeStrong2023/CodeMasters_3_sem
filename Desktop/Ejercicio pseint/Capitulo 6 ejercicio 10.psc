Proceso sin_titulo
	Definir total, a, b, n, x Como Entero;
	Escribir "Ingresa el total de números";
	leer total;
	x<-1;
	Mientras x <= total Hacer

	Escribir "Ingresa un número";
	leer n;
	si x = 1 Entonces
		a <- n;
		b <- n;
	SiNo
		si n > a Entonces
			a <-n;
		SiNo
			si n < b Entonces
				
			FinSi
		FinSi
	FinSi
	x<- x+1;
FinMientras
Escribir "El numero mayor es:" ,a;
	
Escribir "El numero menor es:",b;
FinProceso
