
	SubProceso pedirdatos(nombre Por Referencia)
		Escribir "Ingrese su nombre: ";
		Leer nombre;
FinSubProceso
SubProceso copiarNombre(nombre)
	Definir tamanio,i Como Entero;
	tamanio<-Longitud(nombre);
	Para i<-1 Hasta tamanio Con Paso 1 Hacer
		Escribir Sin Saltar "*"; 
	FinPara
	Escribir "*";
	Escribir nombre;
	Para i<-1 Hasta tamanio Con Paso 1 Hacer
		Escribir Sin Saltar "*"; 
	FinPara
FinSubProceso
Proceso principal
	Definir nombre Como cadena;
	pedirdatos(nombre);
	copiarNombre(nombre);
	Escribir "*";
FinProceso
