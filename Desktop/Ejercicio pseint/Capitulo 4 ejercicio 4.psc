//Un profesor prepara tres cuestionarios para una evaluaci�n final: A, B y C. Se sabe que se tarda 5 minutos en revisar el cuestionario A, 8 en revisar el cuestionario B y 6 en el C. La cantidad de ex�menes de cada tipo se entran por teclado. �Cu�ntas horas y cu�ntos minutos se tardar� en revisar todas las evaluaciones? 
Proceso sin_titulo
	Definir cantidadA,cantidadB,cantidadC Como Entero;
	Definir tiempoA,tiempoB,tiempoC Como Entero;
	Definir tiempo_total, horas, minutos Como Entero;
	Escribir "Digite la cantidad de cuestionarios A";
	Leer cantidadA;
	Escribir "Digite la cantidad de cuestionarios B";
	Leer cantidadB;
	Escribir "Digite la cantidad de cuestionarios C";
	Leer cantidadC;
	tiempoA <- cantidadA * 5;
	tiempoB <- cantidadB* 5;
	tiempoC <- cantidadC* 5;
	tiempo_total <- tiempoA+ tiempoB+ tiempoC;
	horas <- trunc( tiempo_total/60);
	minutos <- tiempo_total mod 60;
	Escribir "Se tardar� ", horas, "Horas y ", minutos, "minutos";

	
FinProceso
