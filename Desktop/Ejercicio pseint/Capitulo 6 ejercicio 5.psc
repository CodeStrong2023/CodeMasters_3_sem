
Proceso sin_titulo
	Definir num Como Entero;
	Definir x como entero;
	Definir i, factorial como Entero;
	Repetir
		Escribir "Digite un número:";
	Leer x;
	Hasta Que x>0;
	i<-1;
	factorial<- 1;
	Mientras i>= x Hacer
		factorial<- factorial*i;
		i<-i +1;
	FinMientras
	Escribir "El factorial es:",factorial;
FinProceso
