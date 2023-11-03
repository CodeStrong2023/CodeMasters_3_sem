//Un maestro desea saber qué porcentaje de hombres y que porcentaje de mujeres hay en un grupo de estudiantes. 
Proceso ejerciocio
	Definir num_hombres,num_mujeres Como Entero;
	Definir total_estudiantes Como Entero;
	Definir porcentajeh,porcentajem Como Real;
	Escribir "Digite el número de hombres";
	Leer num_hombres;
	Escribir "Digite el número de mujeres";
	Leer num_mujeres;
	total_estudiantes <-  num_hombres + num_mujeres;
	porcentajeh <- num_hombres / total_estudiantes *100;
	porcentajem <-num_mujeres/ total_estudiantes*100;
	Escribir "El porcentaje de hombre es:",porcentajeh;
	Escribir "El porcentaje de mujeres es:",porcentajem;
	
	
	
	
	
	
FinProceso
