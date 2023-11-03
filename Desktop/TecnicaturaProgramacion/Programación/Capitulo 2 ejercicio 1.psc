Proceso cuadratica
	Definir a, b, c, x1, x2, discriminante Como Real;
	Escribir "ingrese un valor de a";
	Leer a;
	Escribir "ingrese un valor de b";
	Leer b;
	Escribir "ingrese un valor de c";
	Leer c;
	discriminante <- b^2-4*a*c;
	
	Si discriminante > 0 Entonces
		x1 <- (-b + Raiz(discriminante)) / (2 * a);
		x2 <- (-b - Raiz(discriminante)) / (2 * a);
		Escribir "Las soluciones de la ecuación son x1=", x1, " y x2=", x2;
	Sino Si  discriminante <-0 Entonces;
			x1 <- -b / (2 * a);
		FinSi
		
		Escribir "La solución de la ecuación es x1=", x1;
	 
		Escribir "La ecuación no tiene soluciones reales";
		FinSi
FinProceso
