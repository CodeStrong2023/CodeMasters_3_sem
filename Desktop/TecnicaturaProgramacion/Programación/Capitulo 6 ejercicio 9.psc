Proceso sin_titulo
	Definir x,signo,i Como Entero;
	Definir suma Como Real;
	Repetir
		
		Escribir "Digite el valor de x:";
		Leer x;
	Hasta Que x> 0
	suma<- 0;
	signo<- 1;
	i<-1;
	Repetir
		suma<- suma+ signo/i;
		signo<- signo*(-1);
		i<-i +1;
	Hasta Que i> x;
	Escribir "El resultado es:",suma;
	
FinProceso
