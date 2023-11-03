Proceso sin_titulo
	Definir calificacion_promedio, calificacion_baja Como Entero;
	Definir calificacion,suma Como Real;;
	Definir i Como Entero;
	suma <- 0;
	calificacion_baja<- 9999;
	Para i<-1 Hasta 10 Con Paso 1 Hacer
		Escribir "Digite una calificacion:";
		Leer calificacion;
		suma <-suma +calificacion;	
		Si calificacion< calificacion_baja Entonces
			calificacion_baja<- calificacion;
		FinSi
		calificacion_promedio<- suma/10;
		
	FinPara
	Escribir " La calififcación promedio es:", calificacion_promedio;
	Escribir "La calificación mas baja es:", calificacion_baja;
FinProceso
