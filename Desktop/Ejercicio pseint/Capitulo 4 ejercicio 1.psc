Proceso Ejercicio_1_secuencial
	Definir segundos,minutos,horas Como Entero;
	Escribir "INGRESE UNA CANTIDAD DE SEG. Y MUESTRA LAS HOR. Y MIN. QUE EXISTEN.";
	Escribir "";
	
	Escribir Sin Saltar "Ingrese Cantidad en Segundos : ";
    Leer segundos;
    horas <- TRUNC(segundos/3600);
    minutos <- TRUNC((segundos - (horas*3600))/60);
    segundos <- TRUNC(segundos - ((horas * 3600)+ (minutos*60)));
    Escribir "";
    Escribir "Horas    : ", horas;
    Escribir "Minutos  : ", minutos;
    Escribir "Segundos : ", segundos;
FinAlgoritmo      

	
