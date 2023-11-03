// Determinar si un alumno aprueba o reprueba un curso,
//sabiendo que aprobará si su promedio de tres calificaciones es mayor o igual a 70; reprueba caso contrario. 
Proceso sin_titulo
	Definir calificacion_1,calificacion_2,calificacion_3 Como Entero;
	Definir promedio Como Entero;
	Escribir " Digite calificación";
	Leer calificacion_1;
	Escribir "Digite calificación";
	Leer calificacion_2;
	Escribir "Digite calificación";
	Leer calificacion_3;
	
	promedio <- calificacion_1 + calificacion_2 + calificacion_3;
	
    Si promedio >= 70 ENTONCES
		Escribir "el alumno ha aprobado";
	SiNo 
		Escribir " el alumno ha reprobado";
	FinSi
	
	
FinProceso
